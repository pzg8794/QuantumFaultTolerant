#!/usr/bin/env python3
"""
Read-only Overleaf feedback crawler.

This opens an Overleaf project in a real Chromium browser, uses your existing
logged-in browser session, scans the visible review/comment UI, and exports a
JSON file plus a Markdown feedback queue.

This is not an official Overleaf API client. It is browser automation intended
for a small number of review comments. It does not resolve, delete, reply to, or
edit comments.

First-time setup:
    python -m pip install -r scripts/requirements-overleaf-crawler.txt
    python -m playwright install chromium

Example:
    python scripts/crawl_overleaf_feedback.py \
      --project-url https://www.overleaf.com/project/68ea344896594f27b427ca8f \
      --out-json feedback/overleaf_feedback_raw.json \
      --out-md feedback/overleaf_feedback_queue.md
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, sync_playwright

DEFAULT_PROJECT_URL = "https://www.overleaf.com/project/68ea344896594f27b427ca8f"
DEFAULT_USER_DATA_DIR = ".auth/overleaf-chromium"
DEFAULT_OUT_JSON = "feedback/overleaf_feedback_raw.json"
DEFAULT_OUT_MD = "feedback/overleaf_feedback_queue.md"

COMMENT_PANEL_BUTTONS = [
    re.compile(r"comments?", re.I),
    re.compile(r"review", re.I),
    re.compile(r"reviewing", re.I),
]

COMMENT_CANDIDATE_SELECTORS = [
    "[data-testid*='comment' i]",
    "[data-testid*='review' i]",
    "[class*='comment' i]",
    "[class*='review' i]",
    "[aria-label*='comment' i]",
    "[aria-label*='review' i]",
    "aside",
    "[role='complementary']",
]

EDITOR_CONTEXT_SELECTORS = [
    ".cm-activeLine",
    ".cm-line.cm-activeLine",
    ".cm-line[aria-selected='true']",
    ".CodeMirror-activeline pre",
    ".ace_active-line",
    "textarea:focus",
]

SOURCE_EXTENSIONS = {".tex", ".bib", ".md"}


@dataclass
class FeedbackItem:
    id: str
    status: str
    feedback: str
    reviewer: str | None = None
    timestamp: str | None = None
    file: str | None = None
    line: int | None = None
    content_in_question: str | None = None
    surrounding_context: str | None = None
    extraction_method: str = "visible_overleaf_dom"
    confidence: str = "needs_review"


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def is_noise(text: str) -> bool:
    if len(text) < 8:
        return True
    lowered = text.lower()
    noise_terms = [
        "project menu",
        "download",
        "recompile",
        "share",
        "submit",
        "history",
        "menu",
        "toolbar",
    ]
    if any(term == lowered for term in noise_terms):
        return True
    if len(text) > 5000:
        return True
    return False


def dedupe_preserve_order(texts: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for text in texts:
        key = re.sub(r"\s+", " ", text).strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append(text)
    return out


def try_click_review_panel(page: Page) -> None:
    """Best-effort open of Overleaf review/comment UI."""
    for regex in COMMENT_PANEL_BUTTONS:
        candidates = [
            page.get_by_role("button", name=regex),
            page.get_by_role("tab", name=regex),
            page.get_by_text(regex),
        ]
        for loc in candidates:
            try:
                if loc.count() == 0:
                    continue
                first = loc.first
                if first.is_visible(timeout=800):
                    first.click(timeout=1500)
                    page.wait_for_timeout(800)
                    return
            except PlaywrightTimeoutError:
                continue
            except Exception:
                continue


def wait_for_manual_login_if_needed(page: Page, project_url: str) -> None:
    """Let the user log in interactively if Overleaf redirects to login."""
    try:
        body_text = clean_text(page.locator("body").inner_text(timeout=5000)).lower()
    except Exception:
        body_text = ""

    login_signals = [
        "log in" in body_text and "overleaf" in body_text,
        "login" in page.url.lower(),
        "sessions/new" in page.url.lower(),
    ]
    if any(login_signals):
        print("\nOverleaf login appears to be required.")
        print("Log in in the opened browser window, open the project if needed, then press Enter here.")
        input("Press Enter after the project editor is visible... ")
        page.goto(project_url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)


def selected_text(page: Page) -> str | None:
    try:
        value = page.evaluate("() => window.getSelection ? window.getSelection().toString() : ''")
        value = clean_text(value)
        return value or None
    except Exception:
        return None


def active_editor_text(page: Page) -> str | None:
    snippets: list[str] = []
    for selector in EDITOR_CONTEXT_SELECTORS:
        try:
            loc = page.locator(selector)
            count = min(loc.count(), 5)
            for index in range(count):
                item = loc.nth(index)
                if item.is_visible(timeout=300):
                    text = clean_text(item.inner_text(timeout=700))
                    if text and not is_noise(text):
                        snippets.append(text)
        except Exception:
            continue
    snippets = dedupe_preserve_order(snippets)
    if snippets:
        return "\n".join(snippets)
    return None


def extract_visible_feedback_texts(page: Page) -> list[str]:
    texts: list[str] = []
    for selector in COMMENT_CANDIDATE_SELECTORS:
        try:
            loc = page.locator(selector)
            count = min(loc.count(), 200)
            for index in range(count):
                item = loc.nth(index)
                try:
                    if not item.is_visible(timeout=150):
                        continue
                    text = clean_text(item.inner_text(timeout=500))
                    if text and not is_noise(text):
                        texts.append(text)
                except Exception:
                    continue
        except Exception:
            continue

    # Fallback: collect body lines that look like comments/questions.
    if not texts:
        try:
            body = clean_text(page.locator("body").inner_text(timeout=5000))
            for block in re.split(r"\n\s*\n", body):
                block = clean_text(block)
                if "?" in block or re.search(r"\b(comment|resolve|reply|review)\b", block, re.I):
                    if not is_noise(block):
                        texts.append(block)
        except Exception:
            pass

    return dedupe_preserve_order(texts)


def click_candidates_and_capture_context(page: Page) -> dict[str, str | None]:
    """Click visible comment-like cards and capture active editor/selection context.

    The returned dictionary is keyed by normalized card text.
    """
    context_by_text: dict[str, str | None] = {}
    for selector in COMMENT_CANDIDATE_SELECTORS:
        try:
            handles = page.locator(selector).element_handles()
        except Exception:
            continue
        for handle in handles[:150]:
            try:
                if not handle.is_visible():
                    continue
                text = clean_text(handle.inner_text(timeout=500))
                if not text or is_noise(text):
                    continue
                key = re.sub(r"\s+", " ", text).strip().lower()
                if key in context_by_text:
                    continue
                handle.click(timeout=1000)
                page.wait_for_timeout(350)
                context_by_text[key] = selected_text(page) or active_editor_text(page)
            except Exception:
                continue
    return context_by_text


def guess_status(raw: str) -> str:
    lowered = raw.lower()
    if "resolved" in lowered and "unresolved" not in lowered:
        return "resolved"
    if "unresolved" in lowered or "resolve" in lowered:
        return "unresolved"
    return "unknown"


def guess_reviewer(raw: str) -> str | None:
    lines = [clean_text(line) for line in raw.splitlines() if clean_text(line)]
    if not lines:
        return None
    first = lines[0]
    if len(first) <= 40 and not first.endswith("?") and not first.startswith("\\"):
        if not re.search(r"\b(comment|resolve|reply|review|unresolved)\b", first, re.I):
            return first
    return None


def guess_feedback(raw: str) -> str:
    lines = [clean_text(line) for line in raw.splitlines() if clean_text(line)]
    if not lines:
        return raw

    filtered: list[str] = []
    for line in lines:
        if re.fullmatch(r"(resolve|resolved|reply|edit|delete|more|comments?)", line, re.I):
            continue
        if re.search(r"^\d+\s*(min|hour|day|week|month)s? ago$", line, re.I):
            continue
        filtered.append(line)

    # Prefer explicit question/comment lines.
    for line in filtered:
        if "?" in line and len(line) > 12:
            return line
    return "\n".join(filtered[:5]) if filtered else raw


def line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, max(0, offset)) + 1


def find_best_source_match(snippet: str | None, source_dir: Path) -> tuple[str | None, int | None, str | None]:
    if not snippet:
        return None, None, None
    snippet = clean_text(snippet)
    if len(snippet) < 10:
        return None, None, None

    files = [p for p in source_dir.rglob("*") if p.suffix in SOURCE_EXTENSIONS and ".git" not in p.parts]

    # Exact substring pass.
    for path in files:
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        offset = content.find(snippet)
        if offset >= 0:
            line = line_number_for_offset(content, offset)
            return str(path), line, snippet

    # Fuzzy line/window pass.
    best_score = 0.0
    best: tuple[str | None, int | None, str | None] = (None, None, None)
    normalized_snippet = re.sub(r"\s+", " ", snippet).strip()
    if not normalized_snippet:
        return best

    for path in files:
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        for i in range(len(lines)):
            window = " ".join(lines[i : i + 3]).strip()
            if not window:
                continue
            normalized_window = re.sub(r"\s+", " ", window)
            score = difflib.SequenceMatcher(None, normalized_snippet[:500], normalized_window[:700]).ratio()
            if score > best_score:
                best_score = score
                best = (str(path), i + 1, window)

    if best_score >= 0.72:
        return best
    return None, None, None


def build_items(page: Page, source_dir: Path) -> list[FeedbackItem]:
    try_click_review_panel(page)
    visible_texts = extract_visible_feedback_texts(page)
    context_by_text = click_candidates_and_capture_context(page)

    items: list[FeedbackItem] = []
    for idx, raw in enumerate(visible_texts, start=1):
        key = re.sub(r"\s+", " ", raw).strip().lower()
        context = context_by_text.get(key)
        file, line, matched = find_best_source_match(context, source_dir)
        content = context or matched
        if content and len(content) > 1200:
            content = content[:1200].rstrip() + " ..."

        items.append(
            FeedbackItem(
                id=f"OL-{idx:03d}",
                status=guess_status(raw),
                reviewer=guess_reviewer(raw),
                timestamp=None,
                feedback=guess_feedback(raw),
                file=file,
                line=line,
                content_in_question=content,
                surrounding_context=matched if matched != content else None,
                confidence="needs_review" if not content else "candidate_match",
            )
        )
    return items


def write_json(items: list[FeedbackItem], out_json: Path, project_url: str) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    payload: dict[str, object] = {
        "project_url": project_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "warning": "Read-only browser extraction. Verify all items before applying manuscript edits.",
        "items": [asdict(item) for item in items],
    }
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def md_quote(text: str | None) -> str:
    if not text:
        return "> _Not captured. Fill manually after review._"
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def write_markdown(items: list[FeedbackItem], out_md: Path, project_url: str) -> None:
    out_md.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Overleaf Feedback Queue")
    lines.append("")
    lines.append(f"**Project:** {project_url}")
    lines.append(f"**Generated:** {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append("> Read-only crawler output. Verify feedback, location, and content before editing the manuscript.")
    lines.append("")

    if not items:
        lines.append("No visible feedback items were extracted.")
        lines.append("")
        lines.append("Try running with the browser visible, opening the comments/review panel manually, then press Enter if prompted.")
    for index, item in enumerate(items, start=1):
        title_feedback = item.feedback.splitlines()[0][:80] if item.feedback else "Untitled feedback"
        lines.append(f"## Item {index} — {title_feedback}")
        lines.append("")
        lines.append("**Feedback**")
        lines.append("")
        lines.append(md_quote(item.feedback))
        lines.append("")
        lines.append("**Task**")
        lines.append("")
        lines.append("_To be written after reviewing the feedback._")
        lines.append("")
        lines.append("**Content in question**")
        lines.append("")
        lines.append(md_quote(item.content_in_question))
        lines.append("")
        lines.append("**Location**")
        lines.append("")
        location = item.file or "Unknown file"
        if item.line:
            location += f":{item.line}"
        lines.append(f"- {location}")
        lines.append(f"- Status: {item.status}")
        lines.append(f"- Confidence: {item.confidence}")
        if item.reviewer:
            lines.append(f"- Reviewer: {item.reviewer}")
        lines.append("")
        lines.append("**Proposed solution / new content**")
        lines.append("")
        lines.append("_Pending._")
        lines.append("")
        lines.append("**Evaluation of solution**")
        lines.append("")
        lines.append("_Pending._")
        lines.append("")
        lines.append("**Decision / applied modification**")
        lines.append("")
        lines.append("Pending.")
        lines.append("")
        lines.append("---")
        lines.append("")

    out_md.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only Overleaf feedback crawler")
    parser.add_argument("--project-url", default=DEFAULT_PROJECT_URL)
    parser.add_argument("--user-data-dir", default=DEFAULT_USER_DATA_DIR)
    parser.add_argument("--out-json", default=DEFAULT_OUT_JSON)
    parser.add_argument("--out-md", default=DEFAULT_OUT_MD)
    parser.add_argument("--source-dir", default=".", help="Local repo/source root used for fuzzy source matching")
    parser.add_argument("--headless", action="store_true", help="Run headless. Default is visible browser.")
    parser.add_argument("--pause-before-scrape", action="store_true", help="Pause so you can manually open the review panel before scraping")
    parser.add_argument("--slow-mo", type=int, default=0, help="Playwright slow_mo in milliseconds")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_url = args.project_url
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    source_dir = Path(args.source_dir)
    user_data_dir = Path(args.user_data_dir)
    user_data_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            headless=args.headless,
            slow_mo=args.slow_mo,
            viewport={"width": 1500, "height": 950},
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(project_url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        wait_for_manual_login_if_needed(page, project_url)

        if args.pause_before_scrape:
            print("\nOpen the Overleaf review/comment panel in the browser, then return here.")
            input("Press Enter to scrape visible feedback... ")

        items = build_items(page, source_dir)
        write_json(items, out_json, project_url)
        write_markdown(items, out_md, project_url)
        context.close()

    print(f"Extracted {len(items)} candidate feedback item(s).")
    print(f"JSON written to: {out_json}")
    print(f"Markdown written to: {out_md}")
    if not items:
        print("No items found. Re-run with --pause-before-scrape and manually open the Overleaf review panel before pressing Enter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
