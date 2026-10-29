# Palestine: law history in git (metadata only)

The law of Palestine (PS) as a git history. **This repository holds no law text: it is a catalogue of facts about each text published in the Official Gazette, Al-Waqa'i' al-Filastiniyya.** It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ps/`. Language: Arabic (right-to-left).

| Folder | Text | Versions | History |
| --- | --- | ---: | --- |
| `catalogue/` | One file per text listed in the Gazette: title, type, number and year, gazette issue and date, and the record's address at Al-Muqtafi | 273 | One commit per gazette issue date, from issue 1 (20 November 1994) to issue 241 (30 August 2026); 3,367 entries |

**Why metadata only.** The texts are served by Al-Muqtafi (Institute of Law, Birzeit University), whose pages state that the material is copyrighted and may not be copied without permission. Palestinian copyright is still governed, as far as could be established, by the 1911 Copyright Act as applied by the 1924 Ordinance, and no exemption for laws was found, so the texts cannot be published on the strength of the law alone. Titles, numbers and dates are facts and are the only things copied. An earlier build of the Basic Law (2002, 2003 and 2005 texts) is not published for the same reason.

Each entry is dated by the Gazette issue that lists it, not by the day the text took effect: a text usually takes effect 30 days after publication unless it says otherwise (Amended Basic Law 2003, Art. 116), which this catalogue does not apply. Entries whose title names a person keep only the type and number. The index lists the Gazette's special issues too; their dates are read from each issue's label.

**Source:** [Al-Muqtafi, issue index of Al-Waqa'i' al-Filastiniyya](http://muqtafi.birzeit.edu/pg/), retrieved 29 October 2026. See `LICENSE` and `REPRODUCE.md`.

This repository is not legal advice; for anything that matters, read the original.
