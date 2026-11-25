#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes one sentence (1-200 chars) to /output/entry.txt: an alien tourist's
one-star review of Earth that still slips in a real compliment about the food
(five stars for the food, one star for everything non-food).

Usage:
    python3 main.py                 # Option 1 (default)
    python3 main.py --option 2      # Option 2
    python3 main.py --option 3      # Option 3
    ENTRY_TEXT="..." python3 main.py # override with custom text
"""

import os
import sys
from pathlib import Path

OPTIONS = {
    1: "One star for Earth — the traffic, the weather, and a Wi-Fi password longer than our flight — but five stars for the food, which alone was worth the invasion.",
    2: "One star: the planet's weather is broken, the queues are endless, and nobody told us the Wi-Fi needs a password — five stars for the noodles, the only reason we'd come back.",
    3: "Earth gets one star — rude weather, endless queues, and a moon that just stares — but the food gets five, and honestly the dumplings alone justify the abduction.",
}

MAX_CHARS = 200


def main() -> int:
    option = 1
    args = sys.argv[1:]
    if "--option" in args:
        idx = args.index("--option")
        try:
            option = int(args[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option N]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; valid: {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT", OPTIONS[option])

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")  # no trailing newline
    print(f"option {option}: {len(text)} chars -> {out}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
