from __future__ import annotations

import os.path
from unittest import mock
from strings import find_strings


def test_find_strings() -> None:
    """Tests greet() from the package."""
    filepath = os.path.join(os.path.dirname(__file__), "testfile.py")
    assert list(find_strings(filepath)) == [
        (6, "foo"),
        (17, "Some text\n"),
        (33, "annassign_value"),
        (36, "dict[str, int]"),
        (39, "ok but what about "),
        (39, " f-strings?"),
        (41, "they can infact "),
        (42, "have"),
        (42, "strings"),
        # Older parser reports f-strings' startline
        (mock.ANY, " inside them."),
    ]
