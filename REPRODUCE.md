# How this repository was made (Palestine)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Al-Muqtafi issue index of Al-Waqa'i' al-Filastiniyya (the Official Gazette) | <http://muqtafi.birzeit.edu/pg/> | 2026-10-29 | Only facts are copied; no text of any law and no descriptive text. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `catalogue` | Catalogue of texts published in Al-Waqa'i' al-Filastiniyya (metadata only) | 273 | 1994-11-20 to 2026-08-30 |

The build made 273 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 272 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 273 laws in the record.
- 545 tags.

## Dates

Each commit is dated at noon (Asia/Hebron) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied: each entry is dated by the date of the Official Gazette issue that lists it. http://muqtafi.birzeit.edu/pg/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `1837c9e2f16a5ac67ae7d72b827dfd405007f07481911acf6f8aba682afafec2` (1904002 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Metadata only: no Palestinian copyright statute exempting laws could be found (the 1911 Act as applied by the 1924 Ordinance appears to remain in force and has no such exemption) and Al-Muqtafi states its material is copyrighted, so no law text is published.
- Each entry is dated by the Official Gazette issue date that lists it; an issue sharing a date with another is merged into one day; a text listed in several issues appears once, at its earliest issue.
- Entries whose title names a person (appointments, transfers) keep only the type and number; the rest of the title is withheld.
- Issue dates are read from each issue label (the index date field is wrong or missing for some special issues).
- The earlier full-text build of the Basic Law (2002, 2003, 2005) is held in the private folder and is not published.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the scripts; no model wrote or edited any catalogue entry.
