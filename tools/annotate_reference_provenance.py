from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_testbed_hash_tags(testbeds_root: Path) -> dict[str, str]:
    tags: dict[str, str] = {}
    for pdf in sorted(testbeds_root.rglob("*.pdf")):
        if not pdf.is_file():
            continue
        rel = pdf.relative_to(testbeds_root)
        testbed = rel.parts[0] if rel.parts else "testbeds"
        tag = f"testbed={testbed}__{pdf.name}"
        try:
            digest = sha256_file(pdf)
        except OSError:
            continue
        # Keep first-seen tag per hash.
        tags.setdefault(digest, tag)
    return tags


def inject_tag(filename: str, tag: str) -> str:
    # If already tagged, no change.
    if tag in filename:
        return filename

    if filename.lower().endswith(".pdf"):
        base = filename[:-4]
        ext = ".pdf"
    else:
        base = filename
        ext = ""

    # If base ends with " (something)", inject before close paren.
    m = re.search(r"\s\(([^()]*)\)$", base)
    if m:
        inside = m.group(1).strip()
        if inside:
            inside = f"{inside}; {tag}"
        else:
            inside = tag
        new_base = re.sub(r"\s\([^()]*\)$", f" ({inside})", base)
        return new_base + ext

    return f"{base} ({tag}){ext}"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    base = path.stem
    suffix = path.suffix
    for i in range(2, 100):
        cand = path.with_name(f"{base}_{i}{suffix}")
        if not cand.exists():
            return cand
    raise RuntimeError(f"Could not find unique name for {path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Annotate existing reference PDFs with their originating testbed in the parentheses suffix, "
            "without creating duplicates. Matches are done by sha256 content hash."
        )
    )
    parser.add_argument("--testbeds", required=True, help="Path to quantum_project_hub/testbeds")
    parser.add_argument("--refs", default="references/pdfs", help="Path to reference PDF folder")
    parser.add_argument(
        "--exclude-subdir",
        default="from_main_tex",
        help="Subdir under refs to skip (default: from_main_tex)",
    )
    parser.add_argument("--apply", action="store_true", help="Actually rename files")
    args = parser.parse_args()

    testbeds_root = Path(args.testbeds)
    refs_root = Path(args.refs)
    if not testbeds_root.exists():
        raise SystemExit(f"Testbeds root not found: {testbeds_root}")
    if not refs_root.exists():
        raise SystemExit(f"Refs root not found: {refs_root}")

    exclude = (refs_root / args.exclude_subdir).resolve()
    hash_to_tag = build_testbed_hash_tags(testbeds_root)

    renamed = 0
    for pdf in sorted(refs_root.rglob("*.pdf")):
        if not pdf.is_file():
            continue
        if str(pdf.resolve()).startswith(str(exclude)):
            continue

        try:
            digest = sha256_file(pdf)
        except OSError:
            continue
        tag = hash_to_tag.get(digest)
        if not tag:
            continue

        new_name = inject_tag(pdf.name, tag)
        if new_name == pdf.name:
            continue
        target = unique_path(pdf.with_name(new_name))
        print(f"{'APPLY' if args.apply else 'DRY'}\t{pdf}\t->\t{target}")
        if args.apply:
            pdf.rename(target)
        renamed += 1

    print(f"TOTAL\t{renamed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
