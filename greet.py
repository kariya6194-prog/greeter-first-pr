"""A tiny greeting utility used as a first-pull-request practice project."""

import sys


def greet(name: str) -> str:
    """Return a friendly greeting for the given name.

    Falls back to a generic greeting when the name is empty or whitespace.
    """
    name = name.strip()
    if not name:
        return "Hello, friend!"
    return f"Hello, {name}!"


def main(argv: list[str]) -> int:
    name = " ".join(argv[1:]) if len(argv) > 1 else ""
    print(greet(name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
