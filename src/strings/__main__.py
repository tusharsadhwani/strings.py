"""Support executing the CLI by doing `python -m strings`."""

from __future__ import annotations

import argparse
import contextlib
import os.path
import pathlib
from typing import Iterator

from strings import find_strings


class CLIArgs:
    filepath: str
    line_numbers: bool


def python_files(folder: str) -> Iterator[str]:
    for file in pathlib.Path(folder).rglob("*.py"):
        yield str(file)


def cli(argv: list[str] | None = None) -> int:
    """CLI interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filepath",
        help="Path to python file or folder containing python files",
        type=os.path.abspath,
    )
    parser.add_argument(
        "-n",
        "--line-numbers",
        help="Print the filename and line numbers before the string itself",
        action="store_true",
    )
    args = parser.parse_args(argv, namespace=CLIArgs)
    if os.path.isdir(args.filepath):
        files = python_files(args.filepath)
    else:
        files = [args.filepath]

    for filepath in files:
        for line_number, string in find_strings(filepath):
            with contextlib.suppress(UnicodeEncodeError):
                if args.line_numbers:
                    print(f"{filepath}:{line_number}:{string}")
                else:
                    print(string)

    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
