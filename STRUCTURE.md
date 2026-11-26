# Structure of palestine-law

Folder names are in Arabic, the language people search Palestinian law in. Years and numbers use Western digits.
No folder holds more than 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `الفهرس/<السنة>/` | Catalogue of the texts listed in al-Waqa'i' al-Filastiniyya, 1994-2026 (facts only, no text) | one gazette item (`g039-001.md`) |
| `التشريعات/<السنة>/` | Laws, decree-laws, decisions, regulations and instructions as published in the Gazette | one instrument (`<النوع>-<الرقم>.md`, e.g. `قرار-بقانون-15.md`) |
| `الوقائع-الفلسطينية/<السنة>/` | Gazette issues, full text | one issue (`العدد-<n>.md`, `عدد-ممتاز-<n>.md`) |
| `الأحكام/<المحكمة>/<السنة>/<الشهر>/<اليوم>/` | Judgments, by the day they were given | one judgment (`<نوع-الدعوى>-<الرقم>-<السنة>.md`) |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

## Versions and dates

- One commit per instrument, per gazette issue and per judgment, in the order they took effect.
- The author date is 12:00 Palestine time (Asia/Hebron) on the in-force day: for an instrument, the day its own
  in-force clause gives (publication, issue, or a stated delay), or for a law or decree-law that is silent, 30 days
  after publication (Amended Basic Law 2003, art. 116); for an issue, its publication day; for a judgment, the day it
  was given. Before 1970 the date is 1970-01-01 and the real day starts the subject.
- Trailers on every commit: `Kind:` (law, decree-law, decision, regulation, gazette, judgment, layout, documentation),
  `In-force:`, `In-force-basis:` (the clause or field the day comes from) and `Source:`.
- A record whose day cannot be read is held, not committed.
- Judgments in protected cases (family and personal status, minors, sexual offences) are not committed. Party names
  are never in paths or trailers.

## Sources

- Maqam, the legal portal of An-Najah National University's Faculty of Law (maqam.najah.edu): the Gazette's own
  pages for each instrument (PDF), full gazette issues, and court judgments as published. Laws and judgments are
  official texts.
- The catalogue: Al-Muqtafi (Birzeit University), facts only.

`catalogue/` was renamed `الفهرس/` on 2026-11-26 (a rename only; no text changed), and its entries moved into one folder per Gazette year.
