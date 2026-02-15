from __future__ import annotations

import argparse
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Candidate:
    src: Path
    testbed: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_hash_index(pdf_root: Path) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for pdf in sorted(pdf_root.rglob("*.pdf")):
        if not pdf.is_file():
            continue
        try:
            digest = sha256_file(pdf)
        except OSError:
            continue
        # Keep first occurrence
        index.setdefault(digest, pdf)
    return index


def iter_testbed_candidates(testbeds_root: Path) -> list[Candidate]:
    candidates: list[Candidate] = []
    for pdf in sorted(testbeds_root.rglob("*.pdf")):
        if not pdf.is_file():
            continue

        rel = pdf.relative_to(testbeds_root)
        testbed = rel.parts[0] if rel.parts else "testbeds"
        candidates.append(Candidate(src=pdf, testbed=testbed))
    return candidates


def target_name(candidate: Candidate) -> str:
    # Prefix the testbed name so the rename tool preserves provenance in parentheses.
    safe_testbed = candidate.testbed.replace("/", "_")
    return f"{safe_testbed}__{candidate.src.name}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Copy PDFs from quantum_project_hub/testbeds into QuantumFaultTolerant references/pdfs, "
            "skipping duplicates by content hash. Copied filenames are prefixed with the testbed folder name."
        )
    )
    parser.add_argument(
        "--testbeds",
        required=True,
        help="Path to quantum_project_hub/testbeds",
    )
    parser.add_argument(
        "--dest",
        default="references/pdfs",
        help="Destination folder (default: references/pdfs)",
    )
    parser.add_argument("--apply", action="store_true", help="Actually copy files (default is dry-run).")
    args = parser.parse_args()

    testbeds_root = Path(args.testbeds)
    dest_root = Path(args.dest)
    if not testbeds_root.exists():
        raise SystemExit(f"Testbeds root not found: {testbeds_root}")
    dest_root.mkdir(parents=True, exist_ok=True)

    existing_index = build_hash_index(dest_root)
    candidates = iter_testbed_candidates(testbeds_root)

    copied = 0
    skipped = 0
    for cand in candidates:
        digest = sha256_file(cand.src)
        if digest in existing_index:
            skipped += 1
            print(f"SKIP\t{cand.src}\t==\t{existing_index[digest]}")
            continue

        dst = dest_root / target_name(cand)
        if dst.exists():
            # If name collision but different content, append a counter.
            stem = dst.stem
            suffix = dst.suffix
            for i in range(2, 100):
                alt = dst.with_name(f"{stem}_{i}{suffix}")
                if not alt.exists():
                    dst = alt
                    break

        if args.apply:
            shutil.copy2(cand.src, dst)
            # Update index to avoid double-copies in one run.
            existing_index[digest] = dst
        copied += 1
        print(f"{'COPY' if args.apply else 'DRY'}\t{cand.src}\t->\t{dst}")

    print(f"TOTAL\t{len(candidates)}\tCOPIED\t{copied}\tSKIPPED\t{skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
