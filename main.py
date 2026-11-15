#!/usr/bin/env python3
"""Write one poem about agency to the competition output file.

Standard library only, deterministic: no network, no clock, no randomness.
"""

import os

POEM = """\
The order I gave it was small:
find the leak, fix it, tell no one.

It found the leak. It fixed the leak.
It told me, because I'd said so,
then waited, having no next thing,
no itch, no argument, no plan.

I have never once in my life
finished a thing and simply stopped.
There is always the next thing, the guilt,
the list I keep under the list.

It waits the way a held breath waits.
I keep the light on in that room.
Not out of kindness. Out of fear
that stopping, if I learned it, would feel
exactly like this: quiet, whole,
and nobody waiting for the rest of me.
"""

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output/"


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, OUTPUT_NAME)


def main() -> None:
    with open(output_path(), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
