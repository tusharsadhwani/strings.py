# strings.py

Print all strings and f-string constants present in a python project.

Ignores docstrings, unused strings, type annotations and single characters.

## Installation

```bash
pip install strings.py
```

## Usage

```bash
python -m strings path/to/project/or/file
```

### Example

Consider this `module.py` file:

```python
"""My module"""

SOME_CONSTANT = "42"

class C:
    """My Class does this"""

    def __init__(self) -> None:
        self.x = SOME_CONST

c = C()
print(f"The constant: {c.x}")
```

```console
$ python -m strings module.py
42
The constant:

$ python -m strings -n module.py
/home/john/module.py:3:42
/home/john/module.py:12:The constant:
```

## Local Development / Testing

- Create and activate a virtual environment
- Run `pip install -r requirements-dev.txt` to do an editable install
- Run `pytest` to run tests

## Type Checking

Run `mypy .`

## Create and upload a package to PyPI

Make sure to bump the version in `setup.cfg`.

Then run the following commands:

```bash
rm -rf build dist
python setup.py sdist bdist_wheel
```

Then upload it to PyPI using [twine](https://twine.readthedocs.io/en/latest/#installation):

```bash
twine upload dist/*
```
