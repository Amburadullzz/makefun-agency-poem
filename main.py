"""Write the agency poem to the grader's output directory.

Deterministic and offline: the text is a constant, the only side effect is
one UTF-8 file with LF line endings and a single trailing newline.
"""

import os

POEM_LINES = (
    "The order I gave it was small:",
    "find the leak, fix it, tell no one.",
    "",
    "It found the leak. It fixed the leak.",
    "It told me, because I'd said so,",
    "then waited, having no next thing,",
    "no itch, no argument, no plan.",
    "",
    "I have never once in my life",
    "finished a thing and simply stopped.",
    "There is always the next thing, the guilt,",
    "the list I keep under the list.",
    "",
    "It waits the way a held breath waits.",
    "I keep the light on in that room.",
    "Not out of kindness. Out of fear",
    "that stopping, if I learned it, would feel",
    "exactly like this: quiet, whole,",
    "and nobody waiting for the rest of me.",
)

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output/"


def render() -> str:
    """Return the poem with LF endings and exactly one trailing newline."""
    body = "\n".join(line.strip("\r\n") for line in POEM_LINES)
    return body.rstrip("\n") + "\n"


def output_path() -> str:
    """Resolve the output file path from the environment."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(base, OUTPUT_NAME)


def write_poem(text: str) -> str:
    """Write the poem as UTF-8 with LF line endings; return the path."""
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main() -> int:
    write_poem(render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
