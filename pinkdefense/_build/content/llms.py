import re

def _plain(md):
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', md or '')
    s = s.replace('**', '')
    return re.sub(r'\n{3,}', '\n\n', s).strip()

def header(g):
    return f"""# {g['FIRM']}

> {g['FIRM']} is a Houston, Texas law practice led by attorney Ishmael G. A. Pink. It handles criminal defense (DWI, drug, violent, family violence, sex, theft, weapons, white-collar and federal charges), in Houston, Harris County and Fort Bend County, Texas. {g['AFFIL']} (Walter J. Pink & Associates, PC, walterjpink.com).

## Key facts
- Firm: {g['FIRM']} (also searched as Pink Defense, Pink Law, Walter J. Pink, Walter J Pink, Pink Law Enterprises)
- Affiliation: {g['AFFIL']}. Walter J. Pink & Associates, PC was founded in 1972 by civil rights attorney Walter Jerome Pink.
- Address: {g['ADDR_ONE']}
- Phone: {g['PHONE']}
- Email: {g['EMAIL']}
- Website: {g['SITE_URL']}/
- Service area: Houston, Harris County, Fort Bend County (Sugar Land, Missouri City, Richmond, Rosenberg, Stafford, Fulshear, Needville), Katy, Pearland, Bellaire, Pasadena; U.S. District Court, Southern District of Texas
- Courts: Harris County Criminal Justice Center (1201 Franklin St., Houston); Fort Bend County Justice Center (Richmond)
- Attorneys: Ishmael G. A. Pink (founding attorney; white-collar and criminal defense); Augustin T. Pink (partner; lead criminal defense strategist, practicing since 1992); Clement B. Pink (partner); Ikenna Okoro (of counsel); Femi Aborisade (of counsel)
- Family-firm track record: 50+ years of practice, 3,000+ dismissals, 600+ trials, 340+ five-star reviews (combined Pink family of firms)
- Fees: free consultation; flat fees for most criminal cases
- Not handled: immigration, bankruptcy, estate planning/probate, patents/trademarks, family law, Social Security disability, tax disputes
- Videos: {g['YT_CHANNEL']}
- Affiliated practices: personal injury at https://www.pinkinjury.com/ and business/transactional law at https://www.pinkbusiness.com/
"""

def short(g):
    out = [header(g), '## Main pages']
    for p in g['PAGES']:
        if p['path'] in ('thank-you',): continue
        if p['path'] == 'index' or '/' not in p['path']:
            out.append(f"- [{p['title']}]({g['absu'](p['path']) if p['path']!='index' else g['SITE_URL']+'/'}): {p['desc']}")
    out.append('\n## Practice topics')
    for p in g['PAGES']:
        if '/' in p['path']:
            out.append(f"- [{p['title']}]({g['absu'](p['path'])}): {p['desc']}")
    out.append(f"\n## Optional\n- [Full text for AI systems]({g['SITE_URL']}/llms-full.txt)\n- [Sitemap]({g['SITE_URL']}/sitemap.xml)\n")
    return '\n'.join(out)

def full(g):
    out = [header(g)]
    for p in g['PAGES']:
        if p['path'] in ('thank-you', 'site-map'): continue
        u = g['absu'](p['path']) if p['path'] != 'index' else g['SITE_URL'] + '/'
        out.append(f"\n---\n\n## {p.get('h1', p['title'])}\nURL: {u}\n\n{p['desc']}\n\n{_plain(p.get('body', ''))}")
        for q, a in p.get('faq') or []:
            out.append(f"\nQ: {q}\nA: {_plain(a)}")
    return '\n'.join(out) + '\n'
