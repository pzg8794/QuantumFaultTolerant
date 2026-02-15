from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PdfInfo:
    title: str | None
    author: str | None
    creation_year: str | None


_KNOWN_HINTS: list[tuple[re.Pattern[str], tuple[str | None, str | None, str]]] = [
    # pattern -> (author_last, year, short_title_override)
    (re.compile(r"linkselfie", re.I), ("Liu", "2024", "LinkSelFiE_Link_Selection_and_Fidelity_Estimation")),
    (re.compile(r"quantum[_\s-]*bgp|qbgp", re.I), ("Liu", "2024", "Quantum_BGP_with_Online_Path_Selection")),
    (re.compile(r"learning[_\s-]*best[_\s-]*paths", re.I), ("Wang", "2025", "Learning_Best_Paths_in_Quantum_Networks")),
    (re.compile(r"quantum[_\s-]*bandit|icc2023", re.I), ("Chaudhary", "2023", "Learning_based_Route_Selection_in_Noisy_Quantum_Networks")),
    (re.compile(r"expneuralucb", re.I), ("Huang", "2024", "EXPNeuralUCB_Adversarial_Group_Neural_Bandits")),
    (re.compile(r"adversarial\s+group\s+neural\s+bandits", re.I), ("Huang", "2024", "EXPNeuralUCB_Adversarial_Group_Neural_Bandits")),
    (re.compile(r"quantum\s+entanglement\s+path\s+selection\s+and\s+qubit\s+allocation", re.I),
     ("Huang", "2024", "EXPNeuralUCB_Adversarial_Group_Neural_Bandits")),
    (re.compile(r"adaptive[_\s-]*user[-_\s]*centric[_\s-]*entanglement[_\s-]*routing", re.I),
     ("Wang", "2024", "Adaptive_User_Centric_Entanglement_Routing")),
    (re.compile(r"quarc|adaptive\s+clustering|cluster(ing|ed)\s+quantum\s+routing", re.I),
     ("Wang", "2024", "Efficient_Routing_on_Quantum_Networks_using_Adaptive_Clustering")),

    # Framework “backbone” naming conventions
    (re.compile(r"\bicmabs\b|cmab-comm|ga-paper--icmabs", re.I), ("Kar", "2024", "iCMABs_Replaces_EXP3")),
    (re.compile(r"\bexp3\b", re.I), (None, None, "EXP3_Framework_Inspiration")),

    # UDRM (Sheeraja)
    (re.compile(r"\budrm\b|uncertainty-driven\s+replay\s+memory|exploit-udrm", re.I), ("Sheeraja", "2026", "Exploit_UDRM")),

    # Springer IJTP COSP routing paper
    (re.compile(r"10\.1007/s10773-024-05874-7|collaboratively\s+optimized\s+selection\s+of\s+paths|\bCOSP\b", re.I),
     ("Huang", "2025", "COSP_Collaborative_Routing")),
]


def _known_overrides(hay: str) -> tuple[str | None, str | None, str | None]:
    for pattern, (author_last, year, title_override) in _KNOWN_HINTS:
        if pattern.search(hay):
            return author_last, year, title_override
    return None, None, None


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=False, text=True, capture_output=True)


def _safe_component(text: str, max_len: int = 80) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    if not text:
        return "Unknown"
    return text[:max_len]


_STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "using",
    "via",
    "with",
}


def _compact_title(title: str, *, max_words: int, max_len: int) -> str:
    # Goal: readable, short, filesystem-safe slug.
    words = [w for w in re.split(r"[^A-Za-z0-9]+", title) if w]
    if not words:
        return "Unknown"

    filtered: list[str] = []
    for w in words:
        wl = w.lower()
        if wl in _STOPWORDS:
            continue
        filtered.append(w)
        if len(filtered) >= max_words:
            break

    if not filtered:
        filtered = words[:max_words]

    slug = "_".join(filtered)
    return _safe_component(slug, max_len=max_len)


def _split_stem_and_parens(stem: str) -> tuple[str, str | None]:
    # Returns (base_stem, paren_content) when stem ends with " ( ... )".
    m = re.search(r"\s\(([^()]+)\)$", stem)
    if not m:
        return stem, None
    paren = m.group(1)
    base = stem[: m.start()].rstrip()
    return base, paren


def _shorten_provenance_prefix(prefix: str) -> str:
    # Common case: folder names like "Paper7-..." or "Paper2-...".
    if "-" in prefix:
        first = prefix.split("-", 1)[0]
        if first:
            return first
    # Fallback: keep a small, stable chunk.
    return prefix[:16] if len(prefix) > 16 else prefix


def _compact_paren_payload(payload: str) -> str:
    parts = [p.strip() for p in payload.split(";")]
    out: list[str] = []
    for part in parts:
        if not part:
            continue

        # Keyed provenance.
        m = re.match(r"^(testbed|tb)=(.+)$", part, flags=re.I)
        if m:
            val = m.group(2).strip()
            val = re.sub(r"\.pdf$", "", val, flags=re.I)
            if "__" in val:
                left, right = val.split("__", 1)
                left = _shorten_provenance_prefix(left)
                right = re.sub(r"\.pdf$", "", right, flags=re.I)
                out.append(f"tb={left}__{right}")
            else:
                out.append(f"tb={_shorten_provenance_prefix(val)}")
            continue

        # arXiv-ish prefixes embedded in the original stem.
        m = re.match(r"^(\d{4}\.\d{4,5}(?:v\d+)?)\b", part)
        if m:
            out.append(m.group(1))
            continue

        # Unkeyed "folder__file" patterns.
        if "__" in part:
            left, right = part.split("__", 1)
            left = _shorten_provenance_prefix(left)
            right = re.sub(r"\.pdf$", "", right, flags=re.I)
            out.append(f"{left}__{right}")
            continue

        out.append(part)

    # Keep it short-ish, but don’t destroy traceability.
    compact = "; ".join(out)
    if len(compact) > 140:
        compact = compact[:140].rstrip()
    return compact


def _pdfinfo(path: Path) -> PdfInfo:
    proc = _run(["pdfinfo", str(path)])
    if proc.returncode != 0:
        return PdfInfo(title=None, author=None, creation_year=None)

    title: str | None = None
    author: str | None = None
    year: str | None = None

    for line in proc.stdout.splitlines():
        if line.startswith("Title:"):
            val = line.split(":", 1)[1].strip()
            title = val if val and val.lower() not in {"none", "untitled"} else None
        elif line.startswith("Author:"):
            val = line.split(":", 1)[1].strip()
            author = val if val and val.lower() not in {"none", "unknown"} else None
        elif line.startswith("CreationDate:"):
            m = re.search(r"(20\d{2})", line)
            if m:
                year = m.group(1)

    return PdfInfo(title=title, author=author, creation_year=year)


def _first_page_text(path: Path) -> str:
    # pdftotext is already available in this environment.
    proc = _run(["pdftotext", "-f", "1", "-l", "1", "-layout", str(path), "-"])
    return proc.stdout if proc.returncode == 0 else ""


def _guess_title_from_text(text: str) -> str | None:
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln]
    if not lines:
        return None

    bad = re.compile(
        r"^(arxiv|preprint|draft|proceedings|ieee|acm|copyright|accepted|author\s*\(|this\s+paper\s+has\s+been)\b",
        re.I,
    )
    # Consider only the very top region.
    candidates: list[str] = []
    for ln in lines[:35]:
        if bad.search(ln):
            continue
        # Skip obvious author lines.
        if re.search(r"\b(university|institute|laboratory|department)\b", ln, re.I):
            continue
        if re.search(r"\b(email|@)\b", ln, re.I):
            continue
        # Keep plausible title-ish lines.
        word_count = len(ln.split())
        if 4 <= word_count <= 24:
            candidates.append(ln)

    if not candidates:
        return None

    def score(s: str) -> int:
        alpha = sum(ch.isalpha() for ch in s)
        # Prefer longer but not huge.
        return alpha - (20 if len(s) > 160 else 0)

    best = max(candidates, key=score)
    return best


def _guess_year(path: Path, info: PdfInfo, text: str) -> str | None:
    # First preference: pdfinfo creation year.
    if info.creation_year:
        return info.creation_year

    # arXiv IDs: YYMM.xxxxx => 20YY
    m = re.search(r"\b(\d{2})(\d{2})\.\d{4,5}\b", path.name)
    if m:
        yy = int(m.group(1))
        if 0 <= yy <= 99:
            return f"20{yy:02d}"

    # Scan first page for a year.
    m = re.search(r"\b(20\d{2})\b", text)
    if m:
        return m.group(1)
    return None


def _guess_author_last(path: Path, info: PdfInfo, title: str | None) -> str | None:
    # Known hints based on filename/title.
    hay = f"{path.stem} {title or ''}"
    author_last, _year, _title_override = _known_overrides(hay)
    if author_last:
        return author_last

    # Try metadata author.
    if info.author:
        # Take last token of first author if it's a list.
        first = info.author.split(";")[0].split(",")[0].strip()
        parts = [p for p in re.split(r"\s+", first) if p]
        if parts:
            return parts[-1]
    return None


def _short_title(path: Path, title: str | None) -> str:
    hay = f"{path.stem} {title or ''}"
    _author_last, _year, title_override = _known_overrides(hay)
    if title_override:
        return title_override
    return title or path.stem


def _unique_target(target: Path) -> Path:
    if not target.exists():
        return target
    base = target.stem
    suffix = target.suffix
    parent = target.parent
    for i in range(2, 100):
        cand = parent / f"{base}_{i}{suffix}"
        if not cand.exists():
            return cand
    raise RuntimeError(f"Could not find unique name for {target}")


def rename_pdfs(
    root: Path,
    *,
    apply: bool,
    reprocess: bool,
    max_title_words: int,
    max_title_len: int,
    compact_parens: bool,
) -> list[tuple[Path, Path]]:
    pdfs = sorted([p for p in root.rglob("*.pdf") if p.is_file()])
    renames: list[tuple[Path, Path]] = []
    for pdf in pdfs:
        base_stem, existing_paren = _split_stem_and_parens(pdf.stem)

        # If already renamed like "Author_Year_Title (orig).pdf", do nothing unless reprocess requested.
        if existing_paren and not reprocess:
            continue

        # Preserve traceability payload inside parentheses.
        orig_paren = existing_paren or pdf.stem
        if compact_parens:
            orig_paren = _compact_paren_payload(orig_paren)
        info = _pdfinfo(pdf)
        text = _first_page_text(pdf)

        # Allow known overrides to win over metadata/text.
        top_text = "\n".join(text.splitlines()[:60])
        hay = f"{pdf.stem}\n{top_text}"
        known_author, known_year, known_title = _known_overrides(hay)

        title = known_title or info.title or _guess_title_from_text(text)
        year = known_year or _guess_year(pdf, info, text) or "UnknownYear"
        author_last = known_author or _guess_author_last(pdf, info, title) or "Unknown"

        # Keep filenames short and readable.
        short_title_raw = _short_title(pdf, title)
        short_title = _compact_title(short_title_raw, max_words=max_title_words, max_len=max_title_len)
        author_last = _safe_component(author_last, max_len=40)

        new_name = f"{author_last}_{year}_{short_title} ({orig_paren}).pdf"
        target = pdf.with_name(new_name)
        if target == pdf:
            continue
        target = _unique_target(target)
        renames.append((pdf, target))

    if apply:
        for src, dst in renames:
            src.rename(dst)
    return renames


def main() -> int:
    parser = argparse.ArgumentParser(description="Rename reference PDFs to readable names, preserving prior identifier in parentheses.")
    parser.add_argument("--apply", action="store_true", help="Actually rename files (default is dry-run).")
    parser.add_argument(
        "--reprocess",
        action="store_true",
        help="Also rename PDFs that already have a '(...)' suffix (useful to shorten existing names).",
    )
    parser.add_argument(
        "--max-title-words",
        type=int,
        default=9,
        help="Max number of (non-stopword) words to keep in the title slug (default: 9).",
    )
    parser.add_argument(
        "--max-title-len",
        type=int,
        default=55,
        help="Max character length of the title slug component (default: 55).",
    )
    parser.add_argument(
        "--compact-parens",
        action="store_true",
        help="Compact long provenance inside '(...)' (e.g., shorten testbed tags and arXiv-style prefixes).",
    )
    parser.add_argument(
        "--root",
        default="references/pdfs",
        help="Root folder to scan recursively for PDFs (default: references/pdfs)",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root not found: {root}")

    renames = rename_pdfs(
        root,
        apply=args.apply,
        reprocess=args.reprocess,
        max_title_words=args.max_title_words,
        max_title_len=args.max_title_len,
        compact_parens=args.compact_parens,
    )
    for src, dst in renames:
        print(f"{'APPLY' if args.apply else 'DRY'}\t{src}\t->\t{dst}")
    print(f"TOTAL\t{len(renames)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
