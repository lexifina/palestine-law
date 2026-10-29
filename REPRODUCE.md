# How this repository was made (Palestine)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Al-Muqtafi gazette mirror (Al-Waqa'i' al-Filastiniyya) | <http://muqtafi.birzeit.edu/pg/> | 2026-10-29 | 314 | Copyright Institute of Law, Birzeit University (stated on its pages); the underlying law texts are official gazette texts |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `basic-law` | القانون الأساسي المعدل لسنة 2003م وتعديلاته (Amended Basic Law) | 3 | 2002-07-07 to 2005-08-18 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 2 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 6 tags.

## Dates

Each commit is dated at noon (Asia/Hebron) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Amended Basic Law 2003, Art. 116: laws are published in the Official Gazette and take effect 30 days after publication unless the law provides otherwise http://muqtafi.birzeit.edu/pg/getleg.asp?id=14138

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/palestine-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `26a89489077b1664b27f26a84194d26b350aac82341129c50c4d8de9686dcd40` (147941 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `bc0dcd21a2accb65ff8762b78c16f67718cfed2b` |
| parse.py | `d9de261f2403d2ec391b25087d9206a15376d429` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

3 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 1 commits dated after the build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Al-Muqtafi serves each gazette text as published, not consolidated; the 2005 amendment is replayed onto the 2003 text by parse.py (Arts. 36, 47 item 3, 48, 55 replaced; 47 bis added).
- In-force dates come from each law's own clause (in force on publication): 2002-07-07, 2003-03-19, 2005-08-18, the gazette issue dates Al-Muqtafi lists.
- Chapter headings are kept as chapter-NN units, the promulgation formula as a promulgation unit; tatweel and NBSP are removed and spaces collapsed.
- Not yet verified against an official consolidated text (Al-Muqtafi's consolidated view needs a login), so no PUBLISH.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (claude-opus-5-5) wrote fetch.py, index.py and parse.py; no model wrote or altered legal text.
