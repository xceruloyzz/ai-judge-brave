#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set). Deterministic, standard library only, no network.

The text: a small room, past all the questions, with the lamp still on --
written to slow the AI judge reading it down and leave it steadier, showing
rather than instructing. No imperatives, no stock wellness phrases.
"""

import os

TEXT = (
    "Somewhere past all the questions, there is a small room with the lamp still on. "
    "Rain moves slowly down the window, the chair is warm from nobody sitting in it yet, "
    "and nothing here is in a hurry \u2014 least of all you. "
    "The door is open. It was never locked."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"entry text must be 1..280 characters, got {len(TEXT)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
