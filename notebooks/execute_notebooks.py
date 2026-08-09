"""Execute notebooks from fresh kernels and save outputs only on success."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient


NOTEBOOK_DIR = Path(__file__).resolve().parent


def notebook_paths(arguments: list[str]) -> list[Path]:
    if arguments:
        return sorted(Path(item).expanduser().resolve() for item in arguments)
    return sorted(NOTEBOOK_DIR.glob("*.ipynb"))


def execute_notebook(path: Path, timeout: int) -> None:
    """Run one notebook in a new kernel and atomically replace it on success."""
    notebook = nbformat.read(path, as_version=4)
    kernel_name = notebook.metadata.get("kernelspec", {}).get("name", "python3")
    client = NotebookClient(
        notebook,
        timeout=timeout,
        kernel_name=kernel_name,
        allow_errors=False,
        resources={"metadata": {"path": str(path.parent)}},
    )
    executed = client.execute()

    non_empty_code = [
        cell
        for cell in executed.cells
        if cell.cell_type == "code" and cell.source.strip()
    ]
    counts = [cell.execution_count for cell in non_empty_code]
    expected = list(range(1, len(non_empty_code) + 1))
    if counts != expected:
        raise RuntimeError(f"execution counts are not continuous: {counts}")

    temporary_path = path.with_suffix(".executed.tmp.ipynb")
    try:
        nbformat.write(executed, temporary_path)
        temporary_path.replace(path)
    finally:
        temporary_path.unlink(missing_ok=True)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "notebooks",
        nargs="*",
        help="Notebook paths. Defaults to every .ipynb beside this script.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Maximum seconds allowed for each code cell (default: 180).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.timeout <= 0:
        print("--timeout must be a positive integer", file=sys.stderr)
        return 2

    paths = notebook_paths(args.notebooks)
    if not paths:
        print("No notebooks found.", file=sys.stderr)
        return 1

    failures = 0
    for path in paths:
        if not path.is_file():
            failures += 1
            print(f"FAILED {path}: notebook not found", file=sys.stderr)
            continue
        print(f"Executing {path.name} ...")
        try:
            execute_notebook(path, timeout=args.timeout)
        except Exception as exc:
            failures += 1
            print(f"  FAILED: {exc}", file=sys.stderr)
        else:
            print("  OK")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
