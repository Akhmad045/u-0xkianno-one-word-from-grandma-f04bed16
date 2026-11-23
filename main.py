#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty entry.

Writes the single word our grandma would text about AI to /output/entry.txt.

The word: "Aiiiii" — the letters A-I themselves, stretched the way a grandma
thumb-types a bewildered, delighted gasp at the robot grandchild. It is a
typo she would actually make, warm and a little baffled, tied to AI by its
very letters, and it lands without a caption. Five vowels of stretch keep it
a gasp, not a shout; any longer and it would read as noise, any shorter and
it would read as the plain acronym.

Standard library only, no network, deterministic.
"""

import os

WORD = "Aiiiii"

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 30


def validate(word: str) -> str:
    """Gate check: 1-30 chars, UTF-8, not only whitespace, exactly one word,
    no control characters and no internal whitespace of any kind."""
    assert isinstance(word, str), "word must be a string"
    assert MIN_CHARS <= len(word) <= MAX_CHARS, (
        f"word must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(word)}"
    )
    assert word.strip(), "word must not be only whitespace"
    assert not any(ch.isspace() for ch in word), "word must contain no whitespace"
    assert not any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word), (
        "word must contain no control characters"
    )
    assert len(word.split()) == 1, "entry must be exactly one word"
    word.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return word


def main() -> None:
    word = validate(WORD)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)

    # Verify the file on disk round-trips through the same gate.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert validate(written) == word, "written file does not match the gated word"


if __name__ == "__main__":
    main()
