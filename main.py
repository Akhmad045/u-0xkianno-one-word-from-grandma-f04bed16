#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty entry.

Writes the single word our grandma would text about AI to /output/entry.txt.

The word: "Aiiiii" — the letters A-I themselves, stretched the way a grandma
thumb-types a bewildered, delighted gasp at the robot grandchild. It is a
typo she would actually make, warm and a little baffled, tied to AI by its
very letters, and it lands without a caption.

Standard library only, no network, deterministic.
"""

WORD = "Aiiiii"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    word = WORD

    # Gate check: 1-30 characters, UTF-8, not only whitespace, a single word.
    assert isinstance(word, str)
    assert 1 <= len(word) <= 30, f"word must be 1-30 chars, got {len(word)}"
    assert word.strip(), "word must not be only whitespace"
    assert len(word.split()) == 1, "entry must be exactly one word"
    word.encode("utf-8")  # raises if not valid UTF-8-encodable text

    import os

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
