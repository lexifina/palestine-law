"""Write corpus.json for Palestine: a catalogue of facts (title, type, number, year, gazette issue, date) from
gazette_index.json, which lists each issue of Al-Waqa'i' al-Filastiniyya. No law text is copied (FIRST-BUILDS.md Phase 3b).
    python -X utf8 scripts/palestine-law/catalogue.py
"""
import json, os, re
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
RETRIEVED = '2026-10-29'
PERSON = re.compile(r'السيد|السيدة|الأستاذ|الاستاذ|الدكتور|الدكتورة|المهندس|المهندسة|القاضي|المستشار')


def main():
    idx = json.load(open(os.path.join(HERE, 'gazette_index.json'), encoding='utf-8'))
    seen, by_date, skipped_undated, labels = set(), {}, [], {}
    def idate(it):
        m = re.search(r'(\d{1,2})-(\d{1,2})-(\d{4})\s*\)', it['label'])
        return datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    for it in sorted(idx, key=idate):
        d = idate(it).strftime('%Y-%m-%d')
        m = re.search(r'issue=(\w+)', it['url'])
        issue = m.group(1) if m else 'sp' + re.sub(r'\D', '', it['url'].split('/pg/')[1].split('/')[0]) + 'z' + re.sub(r'\W|\d', '', it['url'].split('/')[-1].replace('.html', ''))
        labels[issue] = re.sub(r'\s*\(.*','',it['label']).strip()
        for n, t in enumerate(it['texts'], 1):
            if t['id'] in seen:
                continue
            seen.add(t['id'])
            by_date.setdefault(d, []).append((issue, n, t))
    laws, versions = {}, []
    withheld = 0
    for d in sorted(by_date):
        key = 'catalogue-' + d
        laws[key] = {'label': 'Catalogue entries of ' + d, 'title': 'Laws listed in the Official Gazette issue(s) dated ' + d,
                     'kind': 'publisher', 'enacted': d, 'published': d, 'url': 'http://muqtafi.birzeit.edu/pg/',
                     'temporary_until': None, 'restores': None, 'note': 'Facts only: title, type, number, year and gazette issue of each text listed; no law text.'}
        changes, credits = {}, {}
        for issue, n, t in by_date[d]:
            title = re.sub(r'\s+', ' ', re.sub(r'\(A\d+\)', '', t['title'])).strip()
            if PERSON.search(title):
                withheld += 1
                m = re.split(r'\s+(?:بشأن|بتعيين|بنقل|بإحالة|بتكليف|بترقية)', title, 1)
                title = m[0] + ' (rest of title withheld: it names a person)'
            m = re.search(r'\((\d+)\)\s*(?:لسنة|لعام)\s*(\d{4})', title)
            typ = re.split(r'\s+(?:رقم|\()', title, 1)[0] if m else ''
            k = 'g%s-%03d' % (issue.zfill(3), n)
            lines = ['# ' + title, 'Type: ' + typ if typ else 'Type: unclassified']
            if m:
                lines.append('Number and year: %s/%s' % (m.group(1), m.group(2)))
            lines.append('Gazette issue: %s (dated %s)' % (labels[issue], d))
            lines.append('Muqtafi record: http://muqtafi.birzeit.edu/pg/getleg.asp?id=%d' % t['id'])
            changes[k] = {'label': 'Gazette %s, item %d' % (issue.lstrip('0'), n), 'kind': 'entry', 'text': '\n'.join(lines) + '\n'}
            credits[k] = [key]
        v = {'from': d, 'source_url': 'http://muqtafi.birzeit.edu/pg/', 'credits': credits}
        v['units' if not versions else 'changes'] = changes
        if not versions:
            v['sha256'] = None
        versions.append(v)
    for v in versions:
        v.pop('sha256', None)
    first = versions[0]
    corpus = {
        'country': {
            'code': 'PS', 'name': 'Palestine', 'slug': 'palestine', 'lang': 'ar', 'tz': 'Asia/Hebron', 'future_branch': 'future',
            'publisher': {'name': "Al-Muqtafi index of Al-Waqa'i' al-Filastiniyya (Institute of Law, Birzeit University)", 'email': 'muqtafi@birzeit.invalid'},
            'default_in_force_rule': {'text': 'Not applied: each entry is dated by the date of the Official Gazette issue that lists it.',
                                      'source': 'http://muqtafi.birzeit.edu/pg/'},
            'licence_note': 'Metadata only, no law text. Facts (titles, numbers, years, issue dates) listed in the issue index of Al-Muqtafi, Institute of Law, Birzeit University.'},
        'sources': [{'name': "Al-Muqtafi issue index of Al-Waqa'i' al-Filastiniyya (the Official Gazette)", 'url': 'http://muqtafi.birzeit.edu/pg/',
                     'retrieved': RETRIEVED, 'licence': 'Only facts are copied; no text of any law and no descriptive text.',
                     'notes': 'Al-Muqtafi states that its material is copyrighted; for that reason no law text is published here.'}],
        'laws': laws,
        'acts': [{'slug': 'catalogue', 'short': 'CAT', 'title': "Catalogue of texts published in Al-Waqa'i' al-Filastiniyya (metadata only)",
                  'url': 'http://muqtafi.birzeit.edu/pg/', 'first_law': None, 'earlier_laws': [], 'versions': versions}],
        'applies': [],
        'decisions': [
            'Metadata only: no Palestinian copyright statute exempting laws could be found (the 1911 Act as applied by the 1924 Ordinance appears to remain in force and has no such exemption) and Al-Muqtafi states its material is copyrighted, so no law text is published.',
            'Each entry is dated by the Official Gazette issue date that lists it; an issue sharing a date with another is merged into one day; a text listed in several issues appears once, at its earliest issue.',
            'Entries whose title names a person (appointments, transfers) keep only the type and number; the rest of the title is withheld.',
            'Issue dates are read from each issue label (the index date field is wrong or missing for some special issues).',
            'The earlier full-text build of the Basic Law (2002, 2003, 2005) is held in the private folder and is not published.',
        ],
        'ai_use': ['Claude Code wrote the scripts; no model wrote or edited any catalogue entry.'],
    }
    first.setdefault('note', "Oldest version available: the first issue in the index (20 November 1994).")
    tmp = os.path.join(HERE, 'corpus.json.tmp')
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=1)
        f.write('\n')
    os.replace(tmp, os.path.join(HERE, 'corpus.json'))
    print('versions', len(versions), 'entries', len(seen), 'withheld', withheld, 'undated', skipped_undated)


if __name__ == '__main__':
    main()
