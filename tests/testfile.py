"""Docstrings should be ignored"""

import typing


SOME_CONST = "foo"


class C:
    "Yet another docstring"

    def __init__(self) -> None:
        """This is also a docstring believe it or not."""
        self.x = SOME_CONST


multiline = """\
Some text
"""

"""
If some string is just sitting there, that also shouldn't count
"""

"""Like this supposed docstring used by some documentation libraries"""
x: int = 1

y: bool
"""Maybe it was below."""

# What about type annotations?
z1: "C"
z2: "str" = "annassign_value"

# This one is questionable, but for now we keep it.
typing.cast("dict[str, int]", x)


f"ok but what about {2 + 2}={4} f-strings?"

f"""they can infact {
    'have' + 'strings'
} inside them."""
