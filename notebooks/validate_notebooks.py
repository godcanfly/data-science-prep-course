"""Validate notebook structure, syntax, outputs, and execution order."""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path
from typing import Iterable

import nbformat
from IPython.core.inputtransformer2 import TransformerManager


NOTEBOOK_DIR = Path(__file__).resolve().parent


def notebook_paths(arguments: list[str]) -> list[Path]:
    """Resolve explicit notebook paths, or all notebooks beside this script."""
    if arguments:
        return sorted(Path(item).expanduser().resolve() for item in arguments)
    return sorted(NOTEBOOK_DIR.glob("*.ipynb"))


def validate_notebook(path: Path) -> list[str]:
    """Return user-facing validation errors for one notebook."""
    errors: list[str] = []
    try:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
    except Exception as exc:  # nbformat exposes several parse/schema exceptions
        return [f"cannot read a valid v4 notebook: {exc}"]

    transformer = TransformerManager()
    kernel_language = str(
        notebook.metadata.get("kernelspec", {}).get(
            "language", notebook.metadata.get("language_info", {}).get("name", "")
        )
    ).lower()
    is_python_kernel = kernel_language.startswith("python")
    code_cells = [
        (index, cell)
        for index, cell in enumerate(notebook.cells, start=1)
        if cell.cell_type == "code" and cell.source.strip()
    ]

    if is_python_kernel:
        for index, cell in code_cells:
            try:
                transformed = transformer.transform_cell(cell.source)
                compile(
                    transformed,
                    f"{path.name}:cell-{index}",
                    "exec",
                    flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT,
                )
            except SyntaxError as exc:
                location = f"line {exc.lineno}" if exc.lineno else "unknown line"
                errors.append(f"cell {index} has invalid Python syntax ({location}): {exc.msg}")
            except Exception as exc:
                errors.append(f"cell {index} cannot be parsed: {type(exc).__name__}: {exc}")

    for index, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type != "code":
            continue
        for output in cell.get("outputs", []):
            if output.output_type == "error":
                errors.append(
                    f"cell {index} saved an error output: "
                    f"{output.get('ename', 'Error')}: {output.get('evalue', '')}"
                )
            elif output.output_type == "stream":
                stream_text = output.get("text", "")
                if output.get("name") == "stderr" and str(stream_text).strip():
                    errors.append(f"cell {index} has non-empty stderr output")
            elif output.output_type == "execute_result":
                if output.get("execution_count") != cell.execution_count:
                    errors.append(
                        f"cell {index} execute_result count "
                        f"{output.get('execution_count')} does not match cell count "
                        f"{cell.execution_count}"
                    )
                if not output.get("data"):
                    errors.append(f"cell {index} has an empty execute_result output")
            elif output.output_type == "display_data" and not output.get("data"):
                errors.append(f"cell {index} has an empty display_data output")

    actual_counts = [cell.execution_count for _, cell in code_cells]
    expected_counts = list(range(1, len(code_cells) + 1))
    if actual_counts != expected_counts:
        errors.append(
            "non-empty code cells must have continuous execution counts "
            f"1..{len(code_cells)}; found {actual_counts}"
        )

    return errors


def validate_all(paths: Iterable[Path]) -> int:
    """Validate paths and return a process-style status code."""
    failures = 0
    for path in paths:
        errors = validate_notebook(path)
        if errors:
            failures += 1
            print(f"{path.name:50} INVALID")
            for error in errors:
                print(f"  - {error}")
        else:
            notebook = nbformat.read(path, as_version=4)
            print(f"{path.name:50} cells: {len(notebook.cells):3}  valid")
    return 1 if failures else 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "notebooks",
        nargs="*",
        help="Notebook paths. Defaults to every .ipynb beside this script.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    paths = notebook_paths(args.notebooks)
    if not paths:
        print("No notebooks found.", file=sys.stderr)
        return 1
    missing = [path for path in paths if not path.is_file()]
    if missing:
        for path in missing:
            print(f"Notebook not found: {path}", file=sys.stderr)
        return 1
    return validate_all(paths)


if __name__ == "__main__":
    raise SystemExit(main())
