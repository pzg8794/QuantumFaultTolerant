from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PdfItem:
    path: Path
    digest: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Deduplicate PDFs within a references directory by sha256. "
            "Preference is to keep files not under a specified 'drop' subdir."
        )
    )
    parser.add_argument("--root", default="references/pdfs", help="Root folder to scan (default: references/pdfs)")
    parser.add_argument(
        "--drop-subdir",
        default="from_main_tex",
        help="If duplicates exist, delete copies under this subdir first (default: from_main_tex)",
    )
    parser.add_argument("--apply", action="store_true", help="Actually delete duplicates (default dry-run)")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root not found: {root}")

    drop_dir = (root / args.drop_subdir).resolve()

    by_digest: dict[str, list[Path]] = {}
    for pdf in sorted(root.rglob("*.pdf")):
        if not pdf.is_file():
            continue
        try:
            digest = sha256_file(pdf)
        except OSError:
            continue
        by_digest.setdefault(digest, []).append(pdf)

    removed = 0
    kept = 0
    for digest, paths in sorted(by_digest.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(paths) <= 1:
            continue

        # Choose keep: prefer outside drop_dir; else keep shortest path.
        outside = [p for p in paths if not str(p.resolve()).startswith(str(drop_dir))]
        if outside:
            keep = sorted(outside, key=lambda p: (len(str(p)), str(p)))[0]
        else:
            keep = sorted(paths, key=lambda p: (len(str(p)), str(p)))[0]

        kept += 1
        for p in paths:
            if p == keep:
                continue
            if args.apply:
                p.unlink(missing_ok=True)
            removed += 1
            print(f"{'DEL' if args.apply else 'DRY-DEL'}\t{p}\t(dup of {keep})")

    print(f"SUMMARY\tduplicate_groups={kept}\tremoved={removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
