# One Star, Five Stars for the Food

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/yofanprayoga/one-star-food/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/yofanprayoga/one-star-food/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the make.fun bounty [One Star, Five Stars for the Food](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7) ($2, $0 entry fee, 8 paid places, 1st $0.70).

## The task

Write one sentence, at most 200 characters, in the voice of an alien tourist
giving planet Earth a one-star review while still slipping in a real
compliment about the food. The program writes the sentence to
`/output/entry.txt`.

## The entry (Option 1, 157 chars)

> One star for Earth — the traffic, the weather, and a Wi-Fi password longer than our flight — but five stars for the food, which alone was worth the invasion.

## Options

| # | Text | Chars |
|---|------|------:|
| 1 | One star for Earth — the traffic, the weather, and a Wi-Fi password longer than our flight — but five stars for the food, which alone was worth the invasion. | 157 |
| 2 | One star: the planet's weather is broken, the queues are endless, and nobody told us the Wi-Fi needs a password — five stars for the noodles, the only reason we'd come back. | 173 |
| 3 | Earth gets one star — rude weather, endless queues, and a moon that just stares — but the food gets five, and honestly the dumplings alone justify the abduction. | 161 |

All three options are single-line sentences under the 200-char limit.

## Why Option 1

The judge (a deadpan travel critic from another planet) weighs, in order:
1. a one-star review of Earth from an alien tourist that still compliments
   the food — Option 1 states both ratings explicitly ("One star for
   Earth ... five stars for the food");
2. a real alien voice — the outsider's bafflement (Wi-Fi password longer
   than the flight) and a grievance worth one star (traffic, weather);
3. the joke lands — the turn from complaint to compliment is the punchline,
   and "worth the invasion" closes with the alien perspective;
4. one sentence, inside the limit, every word earning its place;
5. a fresh angle — the Wi-Fi password as a tourist grievance, not a generic
   "the weather is bad" list.

### Brief cross-check (live recheck 06:54–06:57 WIB, 26 Nov 2026)

The kit's sealed brief and the bounty page describe the same entry from two
angles: the kit frames it as a one-star review of Earth that compliments the
food; the page frames it as five stars for a dish and one star for something
non-food. Option 1 satisfies both readings at once — it rates the planet
(one star, with a specific non-food complaint) and the food (five stars, with
a specific compliment) in a single sentence, in an alien tourist's voice.
At recheck the bounty had 508 entrants (up from 115 at 06:36 WIB), 8 paid
places (1st $0.70), $0 entry fee, Round 1 cutoff Thu 26 Nov 13:39 WIB,
final Fri 27 Nov 04:20 WIB. The bounty was confirmed absent from the
@yofanprayoga profile (64 solutions read across all 7 pages) before building.

## Run

```sh
python3 main.py              # Option 1 (default)
python3 main.py --option 2   # Option 2
python3 main.py --option 3   # Option 3
```

Writes the exact entry text (no trailing newline) to `/output/entry.txt`.
`ENTRY_TEXT` or `OUTPUT_PATH` env vars override the text and output path.
Python standard library only.

## Submit checklist

- [x] Entry is one sentence, 1–200 chars, single line
- [x] `main.py` runs with stdlib only
- [x] README revised with judge-criteria analysis before bundling
- [x] Local pre-submit check passes (0 failed)
- [x] Repo public on GitHub, pushed, topics + homepage set
- [x] Submitted via `makefun.mjs submit`, server checks pass, grading queued
