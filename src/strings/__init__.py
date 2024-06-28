"""strings.py - Find all string values used in a python project."""

from __future__ import annotations

import ast
import warnings


class StringFinder(ast.NodeVisitor):
    def __init__(self) -> None:
        self.strings: list[tuple[int, str]] = []

    def visit_Expr(self, node: ast.Expr) -> None:
        """
        This is to avoid adding string constants that are just sitting there,
        unassigned and pretty much discarded ones.

        for eg:

        '''Random documentation of x'''
        x: int
        """
        if isinstance(node.value, ast.Constant):
            return

        self.visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        """Skip the target and annotation, only visit the value."""
        if node.value is not None:
            self.visit(node.value)

    def visit_Constant(self, node: ast.Constant) -> None:
        """Add all regular strings, and string parts of f-strings."""
        if not isinstance(node.value, str):
            return

        if len(node.value) == 1:
            # we're skipping single characters.
            return

        self.strings.append((node.lineno, node.value))


def find_strings(filepath: str) -> list[tuple[int, str]]:
    """Find all strings, and their corresponding line numbers in a file."""
    with open(filepath, "rb") as file:
        content = file.read()

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            tree = ast.parse(content)
    except (SyntaxError, ValueError):
        return []

    string_finder = StringFinder()
    string_finder.visit(tree)
    return string_finder.strings
