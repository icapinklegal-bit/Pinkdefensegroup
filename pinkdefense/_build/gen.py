#!/usr/bin/env python3
"""PinkDefense static site generator. Usage: SITE_URL=https://www.example.com python3 gen.py OUTDIR"""
import os, sys, re, json, html, shutil, hashlib, importlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'content'))

SITE_URL = os.environ.get('SITE_URL', 'https://www.pinkdefense.com').rstrip('/')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..')
TODAY = datetime.date.today().isoformat()
# Paste your Google Analytics / Tag Manager <script> snippet between the quotes to add it to every page.
ANALYTICS = os.environ.get('ANALYTICS_SNIPPET', '')

FIRM = 'PinkDefense'
PHONE = '(832) 979-0882'
TEL = '+18329790882'
EMAIL = 'Ishmael@PinkEsquire.com'
STREET, SUITE, CITY, REGION, ZIP = '1717 St. James Place', 'Suite 690', 'Houston', 'TX', '77056'
ADDR_ONE = f'{STREET}, {SUITE}, {CITY}, {REGION} {ZIP}'
LAT, LNG = 29.7507, -95.4606
AFFIL = 'Affiliate of Walter J. Pink & Pink Law Enterprises'
AFFIL_H = 'Affiliate of Walter J. Pink &amp; Pink Law Enterprises'
YT_CHANNEL = 'https://www.youtube.com/@walterj.pinkassociates9601'
YT_LIST = 'UU2YfJc3L0YDFZrycuqWfOug'   # uploads playlist of channel UC2YfJc3L0YDFZrycuqWfOug
YT_EMBED = f'https://www.youtube-nocookie.com/embed/videoseries?list={YT_LIST}'
FORM_ACTION = f'https://formsubmit.co/{EMAIL}'
MAP_EMBED = 'https://www.google.com/maps?q=1717+St.+James+Place+Suite+690+Houston+TX+77056&output=embed'
MAP_LINK = 'https://www.google.com/maps/search/?api=1&query=1717+St.+James+Place+Suite+690+Houston+TX+77056'

AREAS = ['Houston', 'Harris County', 'Fort Bend County', 'Sugar Land', 'Missouri City', 'Richmond', 'Rosenberg',
         'Stafford', 'Katy', 'Fulshear', 'Needville', 'Pearland', 'Bellaire', 'Pasadena', 'Galleria / Uptown']
KEYWORDS = ['PinkDefense', 'Pink Defense', 'Walter J. Pink', 'Walter J Pink', 'Walter J. Pink & Associates',
            'Pink Law', 'Pink Law Enterprises', 'Pink Law Group', 'Ishmael Pink', 'Ishmael G. A. Pink',
            'Augustin T. Pink', 'Augustin Pink', 'Clement B. Pink', 'Houston criminal defense lawyer',
            'Fort Bend County criminal defense attorney', 'Sugar Land criminal lawyer', 'Houston DWI lawyer',
            'Houston white-collar defense', 'Houston federal criminal defense', 'Harris County criminal lawyer']

import data_common as C  # shared reviews/results/categories
PAGES = []
for mod in ['p_core', 'p_dwi', 'p_drugs', 'p_violent', 'p_dv', 'p_sex', 'p_theft', 'p_weapons', 'p_misc', 'p_people']:
    PAGES += importlib.import_module(mod).PAGES
BY_PATH = {p['path']: p for p in PAGES}

esc = html.escape

def url(path):
    return '/' if path in ('', 'index') else f'/{path.strip("/")}/'

def absu(path):
    return SITE_URL + url(path)

# ---------- mini markdown ----------
def inline(s):
    s = esc(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    return s

def slugify(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:60]

def md(text):
    out, heads, para, lst, ltype = [], [], [], [], None
    def flush():
        nonlocal para, lst, ltype
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>'); para = []
        if lst:
            out.append(f'<{ltype}>' + ''.join(f'<li>{inline(i)}</li>' for i in lst) + f'</{ltype}>'); lst = []; ltype = None
    for raw in (text or '').strip().split('\n'):
        line = raw.strip()
        if not line:
            flush(); continue
        m = re.match(r'^(#{2,3}) (.+)$', line)
        if m:
            flush(); lvl = len(m.group(1)); t = m.group(2); sid = slugify(t)
            if lvl == 2: heads.append((sid, t))
            out.append(f'<h{lvl} id="{sid}">{inline(t)}</h{lvl}>'); continue
        m = re.match(r'^(-|\d+\.) (.+)$', line)
        if m:
            if para: flush()
            t = 'ol' if m.group(1)[0].isdigit() else 'ul'
            if ltype and ltype != t: flush()
            ltype = t; lst.append(m.group(2)); continue
        if lst: flush()
        para.append(line)
    flush()
    return '\n'.join(out), heads

# ---------- shared fragments ----------
def nav_html(cur):
    items = C.NAV
    def li(it):
        href, label = it[0], it[1]
        subs = it[2] if len(it) > 2 else None
        ac = ' aria-current="page"' if href.strip('/') == cur.strip('/') else ''
        s = f'<li><a href="{href}"{ac}>{esc(label)}</a>'
        if subs:
            s += '<div class="sub">' + ''.join(f'<a href="{h}"' + (' target="_blank" rel="noopener"' if h.startswith('http') else '') + f'>{esc(l)}</a>' for h, l in subs) + '</div>'
        return s + '</li>'
    return '<ul>' + ''.join(li(i) for i in items) + '</ul>'

PIN = '<svg width="18" height="22" viewBox="0 0 24 30" aria-hidden="true"><path fill="#C9A227" d="M12 0C5.4 0 0 5.4 0 12c0 9 12 18 12 18s12-9 12-18C24 5.4 18.6 0 12 0zm0 17a5 5 0 110-10 5 5 0 010 10z"/></svg>'

def header(cur):
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="affil" role="note"><span>{AFFIL_H}</span></div>
<header class="site-head">
 <div class="head-row">
  <a class="logo" href="/" aria-label="{FIRM} home"><img src="/assets/img/logo.svg" alt="{FIRM} — Houston &amp; Fort Bend attorneys" width="360" height="64"></a>
  <div class="head-contact">
   <div class="head-addr">{PIN}<address style="font-style:normal">{STREET}, {SUITE}<br>{CITY}, {REGION} {ZIP}</address></div>
   <div class="head-phone"><small>Free consultation</small><a href="tel:{TEL}">{PHONE}</a></div>
   <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  </div>
 </div>
 <nav class="nav" id="nav" aria-label="Main">{nav_html(cur)}</nav>
</header>'''

def form_html(idp, dark=True):
    lab = '' if dark else ''
    return f'''<form class="form" action="{FORM_ACTION}" method="POST" id="{idp}">
 <input type="hidden" name="_subject" value="New {FIRM} website inquiry">
 <input type="hidden" name="_next" value="{SITE_URL}/thank-you/">
 <input type="hidden" name="_captcha" value="false">
 <input type="hidden" name="_template" value="table">
 <input type="hidden" name="page" value="">
 <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
 <label for="{idp}-n">Name</label><input id="{idp}-n" name="name" required autocomplete="name">
 <label for="{idp}-p">Phone</label><input id="{idp}-p" name="phone" type="tel" required autocomplete="tel">
 <label for="{idp}-e">Email</label><input id="{idp}-e" name="email" type="email" required autocomplete="email">
 <label for="{idp}-c">County</label><select id="{idp}-c" name="county"><option>Harris County</option><option>Fort Bend County</option><option>Other Texas county</option><option>Federal case</option></select>
 <label for="{idp}-m">Briefly describe your situation</label><textarea id="{idp}-m" name="message" required></textarea>
 <button class="btn btn-grad" type="submit">Schedule a Consultation</button>
</form>
<p class="fine">Sending this form does not create an attorney-client relationship. Please do not include confidential details. For urgent matters call <a href="tel:{TEL}">{PHONE}</a>.</p>'''

def review_box(seed):
    r = C.REVIEWS[seed % len(C.REVIEWS)]
    return f'''<div class="side-box"><h3>What Clients Say</h3><div class="sub">Google reviews of our affiliate firm</div>
<div class="inner"><p>&ldquo;{esc(r[1])}&rdquo;</p><p style="text-align:center;margin:0">&mdash; {esc(r[0])}, Google review</p></div>
<p class="fine">Reviews were left for Walter J. Pink &amp; Associates, PC.</p>
<a class="btn btn-grad" style="width:100%;text-align:center" href="/testimonials/">Read More Reviews</a></div>'''

def result_box(seed):
    r = C.RESULTS[seed % len(C.RESULTS)]
    return f'''<div class="side-box"><h3>Case Results</h3><div class="sub">A sample of family-firm outcomes*</div>
<div class="inner"><div class="verdict">{esc(r[1])}</div><p><b>Matter:</b> {esc(r[0])}</p>{f'<p><b>Detail:</b> {esc(r[2])}</p>' if r[2] else ''}</div>
<p class="fine">*Results obtained by Walter J. Pink &amp; Associates, PC. Every case is different; past results do not guarantee a similar outcome.</p>
<a class="btn btn-grad" style="width:100%;text-align:center" href="/case-results/">More Results</a></div>'''

def sidebar(path):
    seed = int(hashlib.md5(path.encode()).hexdigest(), 16)
    return f'''<aside class="side" aria-label="Contact and highlights">
<div class="side-video"><div class="ratio"><iframe src="{YT_EMBED}" title="{FIRM} videos" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div>
<div class="side-box"><h3>Request Your Free Consultation</h3><div class="sub">Houston &amp; Fort Bend County</div>{form_html('sf')}</div>
{review_box(seed)}
{result_box(seed // 7)}
</aside>'''

def footer():
    pa = ''.join(f'<li><a href="{h}">{esc(l)}</a></li>' for h, l in C.FOOT_PRACTICE)
    ar = ', '.join(AREAS)
    return f'''<footer class="foot">
 <div class="container foot-grid">
  <div><img src="/assets/img/logo.svg" alt="{FIRM}" width="260" height="46" style="height:46px;width:auto;margin-bottom:14px">
   <p>{FIRM} is the Houston trial practice of Ishmael G. A. Pink, defending people accused of crimes in Harris County, Fort Bend County, and Texas federal courts. For personal injury, visit <a href="https://www.pinkinjury.com/" target="_blank" rel="noopener">PinkInjury.com</a>; for business matters, <a href="https://www.pinkbusiness.com/" target="_blank" rel="noopener">PinkBusiness.com</a>. {AFFIL_H}.</p>
  </div>
  <div><h3>Practice Areas</h3><ul>{pa}</ul></div>
  <div><h3>The Firm</h3><ul><li><a href="/about/">About {FIRM}</a></li><li><a href="/attorneys/">Our Attorneys</a></li><li><a href="/case-results/">Case Results</a></li><li><a href="/testimonials/">Client Reviews</a></li><li><a href="/videos/">Videos</a></li><li><a href="/frequently-asked-question-faq/">FAQ</a></li><li><a href="/resources/">Resources</a></li><li><a href="/site-map/">Site Map</a></li><li><a href="/other-practices/">Other Practices</a></li><li><a href="https://www.pinkinjury.com/" target="_blank" rel="noopener">PinkInjury.com</a></li><li><a href="https://www.pinkbusiness.com/" target="_blank" rel="noopener">PinkBusiness.com</a></li></ul></div>
  <div><h3>Contact</h3>
   <address style="font-style:normal"><strong>{FIRM}</strong><br>{STREET}, {SUITE}<br>{CITY}, {REGION} {ZIP}</address>
   <p style="margin:8px 0">Phone: <a href="tel:{TEL}">{PHONE}</a><br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
   <iframe class="map" src="{MAP_EMBED}" title="Map to {FIRM}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
 </div>
 <div class="container foot-bottom">
  <span class="affil-line">{AFFIL_H}</span>
  Serving {ar}.<br>
  &copy; {datetime.date.today().year} {FIRM}. Attorney advertising. The information on this website is general information, not legal advice, and does not create an attorney-client relationship. Prior results do not guarantee a similar outcome.
  <br><a href="/disclaimer/">Disclaimer</a> &middot; <a href="/privacy-policy/">Privacy Policy</a> &middot; <a href="/llms.txt">AI summary (llms.txt)</a>
 </div>
</footer>
<nav class="mbar" aria-label="Quick actions"><ul><li><a class="call" href="tel:{TEL}">Call</a></li><li><a href="/attorneys/">Attorneys</a></li><li><a href="/case-results/">Results</a></li><li><a href="/contact/">Contact</a></li></ul></nav>
<script src="/assets/js/site.js" defer></script>'''

# ---------- structured data ----------
ORG_ID = SITE_URL + '/#organization'

def org_node():
    return {
        '@type': ['LegalService', 'LocalBusiness'], '@id': ORG_ID, 'name': FIRM,
        'alternateName': ['Pink Defense', 'PinkDefense Houston', 'Pink Law', 'Pink Esquire'],
        'description': f'{FIRM} is a Houston, Texas law practice led by attorney Ishmael G. A. Pink handling criminal defense, DWI, white-collar and federal criminal cases in Harris County and Fort Bend County. {AFFIL}.',
        'url': SITE_URL + '/', 'logo': SITE_URL + '/assets/img/logo.svg', 'image': SITE_URL + '/assets/img/og-image.svg',
        'telephone': TEL, 'email': EMAIL, 'priceRange': 'Free consultation',
        'address': {'@type': 'PostalAddress', 'streetAddress': f'{STREET}, {SUITE}', 'addressLocality': CITY,
                    'addressRegion': REGION, 'postalCode': ZIP, 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LNG},
        'hasMap': MAP_LINK,
        'areaServed': [{'@type': 'City', 'name': 'Houston, TX'}, {'@type': 'AdministrativeArea', 'name': 'Harris County, TX'},
                       {'@type': 'AdministrativeArea', 'name': 'Fort Bend County, TX'}] +
                      [{'@type': 'City', 'name': f'{a}, TX'} for a in ['Sugar Land', 'Missouri City', 'Richmond', 'Rosenberg', 'Stafford', 'Katy', 'Fulshear', 'Needville']],
        'knowsAbout': ['Criminal defense', 'DWI defense', 'Drug crime defense', 'Family violence defense', 'White-collar crime',
                       'Federal criminal defense', 'Expunction and nondisclosure', 'Sex crime defense', 'Weapons charges', 'Theft and fraud defense'],
        'founder': {'@id': SITE_URL + '/attorneys/ishmael-pink/#person'},
        'memberOf': [{'@type': 'LegalService', 'name': 'Walter J. Pink & Associates, PC', 'url': 'https://walterjpink.com/',
                      'telephone': '+17136646651', 'address': ADDR_ONE},
                     {'@type': 'Organization', 'name': 'Pink Law Enterprises'}],
        'sameAs': ['https://walterjpink.com/', YT_CHANNEL, 'https://www.pinkinjury.com/', 'https://www.pinkbusiness.com/'],
        'slogan': AFFIL,
        'contactPoint': {'@type': 'ContactPoint', 'telephone': TEL, 'email': EMAIL, 'contactType': 'Free consultation',
                         'areaServed': ['US-TX'], 'availableLanguage': ['English']},
    }

def page_schema(p, crumbs):
    g = [org_node(),
         {'@type': 'WebSite', '@id': SITE_URL + '/#website', 'url': SITE_URL + '/', 'name': FIRM,
          'publisher': {'@id': ORG_ID}, 'inLanguage': 'en-US'},
         {'@type': p.get('schema_type', 'WebPage'), '@id': absu(p['path']) + '#webpage', 'url': absu(p['path']),
          'name': p['title_tag'], 'description': p['desc'], 'isPartOf': {'@id': SITE_URL + '/#website'},
          'about': {'@id': ORG_ID}, 'inLanguage': 'en-US', 'dateModified': TODAY,
          'spatialCoverage': [{'@type': 'Place', 'name': 'Houston, Texas'}, {'@type': 'Place', 'name': 'Fort Bend County, Texas'}],
          'keywords': ', '.join(KEYWORDS[:8] + [p['title']])}]
    if crumbs:
        g.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE_URL + h} for i, (h, n) in enumerate(crumbs)]})
    if p.get('kind') in ('criminal', 'pi', 'civil'):
        g.append({'@type': 'Service', 'name': f"{p['title']} — {CITY} & Fort Bend County", 'serviceType': p['title'],
                  'provider': {'@id': ORG_ID}, 'areaServed': ['Houston, TX', 'Harris County, TX', 'Fort Bend County, TX'],
                  'url': absu(p['path'])})
    if p.get('faq'):
        g.append({'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q,
                  'acceptedAnswer': {'@type': 'Answer', 'text': re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', a)}} for q, a in p['faq']]})
    if p.get('person'):
        pr = dict(p['person']); pr['url'] = absu(p['path']); pr['@id'] = absu(p['path']) + '#person'
        g.append(pr | {'@type': 'Person', 'worksFor': {'@id': ORG_ID}, 'affiliation': [{'@type': 'Organization', 'name': 'Walter J. Pink & Associates, PC'}, {'@type': 'Organization', 'name': 'Pink Law Enterprises'}]})
        g[2]['mainEntity'] = {'@id': pr['@id']}
    return json.dumps({'@context': 'https://schema.org', '@graph': g}, ensure_ascii=False)

def head(p, crumbs):
    t = p['title_tag']; d = p['desc']; u = absu(p['path'])
    kw = ', '.join(KEYWORDS + [p['title']])
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title>
<meta name="description" content="{esc(d)}">
<meta name="keywords" content="{esc(kw)}">
<meta name="author" content="{FIRM}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<link rel="canonical" href="{u}">
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="Houston, Texas; Fort Bend County, Texas">
<meta name="geo.position" content="{LAT};{LNG}">
<meta name="ICBM" content="{LAT}, {LNG}">
<meta name="DC.title" content="{esc(t)}">
<meta name="DC.coverage" content="Houston, Harris County, Fort Bend County, Sugar Land, Missouri City, Richmond, Rosenberg, Katy, Texas, USA">
<meta name="business:contact_data:street_address" content="{STREET}, {SUITE}">
<meta name="business:contact_data:locality" content="{CITY}">
<meta name="business:contact_data:region" content="{REGION}">
<meta name="business:contact_data:postal_code" content="{ZIP}">
<meta name="business:contact_data:country_name" content="United States">
<meta name="business:contact_data:phone_number" content="{PHONE}">
<meta name="business:contact_data:email" content="{EMAIL}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{FIRM}">
<meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(d)}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-image.png">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t)}">
<meta name="twitter:description" content="{esc(d)}">
<meta name="theme-color" content="#1E1315">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" title="LLM summary" href="/llms.txt">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
{ANALYTICS}
<script type="application/ld+json">{page_schema(p, crumbs)}</script>
</head>'''

# ---------- page assembly ----------
def crumbs_for(p):
    cr = [('/', 'Home')]
    parts = p['path'].split('/')
    for i in range(1, len(parts)):
        pp = '/'.join(parts[:i])
        if pp in BY_PATH: cr.append((url(pp), BY_PATH[pp]['title']))
    if p['path'] != 'index': cr.append((url(p['path']), p['title']))
    return cr

def children(path):
    pre = path + '/'
    return [q for q in PAGES if q['path'].startswith(pre) and q['path'].count('/') == path.count('/') + 1]

def siblings(p):
    if '/' not in p['path']: return []
    par = p['path'].rsplit('/', 1)[0]
    return [q for q in children(par) if q['path'] != p['path']]

def penalty_table(levels):
    rows = ''.join(f'<tr><td>{esc(note)}</td><td>{esc(C.LEVELS[k][0])}</td><td>{esc(C.LEVELS[k][1])}</td><td>{esc(C.LEVELS[k][2])}</td></tr>' for note, k in levels)
    return f'''<h2 id="penalties">Possible Penalties Under Texas Law</h2>
<div class="tbl-wrap"><table class="pen"><thead><tr><th>Situation</th><th>Offense level</th><th>Confinement range</th><th>Maximum fine</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="fine">General ranges under Texas Penal Code &sect;&sect; 12.21&ndash;12.35. Enhancements for prior convictions, deadly weapons, or protected locations can raise these ranges. Probation, deferred adjudication, or diversion may be available depending on the facts.</p>'''

def special_html(p):
    if p.get('html_fn'): return p['html_fn']()
    if p.get('team'):
        return ('<p>PinkDefense brings together three generations of Pink family trial lawyers and of counsel attorneys with backgrounds in government, energy and litigation.</p>'
                '<div class="grid g2">' + ''.join(C.atty_card(a) for a in C.ATTYS) + '</div>')
    if p.get('videos'):
        return (f'<p>Watch our latest videos on criminal defense and DWI law in Houston and Fort Bend County. Use the playlist button in the player to browse every video, or visit our <a href="{YT_CHANNEL}" rel="noopener">YouTube channel</a>.</p>'
                f'<div class="ratio" style="border:4px solid transparent;border-image:var(--grad) 1"><iframe src="{YT_EMBED}" title="{FIRM} video playlist" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
                f'<p style="margin-top:20px"><a class="btn btn-grad" href="{YT_CHANNEL}?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></p>')
    if p.get('contact'):
        return (f'<div class="grid g2" style="margin-top:20px"><div><h2 id="reach-us" style="margin-top:0">Reach Us</h2>'
                f'<p><strong>{FIRM}</strong><br>{STREET}, {SUITE}<br>{CITY}, {REGION} {ZIP}</p>'
                f'<p>Phone: <a href="tel:{TEL}">{PHONE}</a><br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'
                f'<p>We serve clients throughout Houston, Harris County and Fort Bend County, including Sugar Land, Missouri City, Richmond, Rosenberg, Stafford, Katy and Fulshear.</p>'
                f'<p><a href="{MAP_LINK}" rel="noopener">Get directions</a></p>'
                f'<iframe src="{MAP_EMBED}" title="Map to {FIRM}" loading="lazy" style="border:0;width:100%;height:280px;border-radius:6px"></iframe></div>'
                f'<div class="card"><h2 style="margin-top:0;border:0">Request a Free Consultation</h2>{form_html("cf", dark=False)}</div></div>')
    if p.get('sitemap_page'):
        groups = {}
        for q in PAGES:
            if q['path'] in ('thank-you',): continue
            top = q['path'].split('/')[0]
            groups.setdefault(top, []).append(q)
        out = ''
        for top, qs in groups.items():
            lead = BY_PATH.get(top, qs[0])
            out += f'<h3><a href="{url(lead["path"])}">{esc(lead["title"])}</a></h3>'
            rest = [q for q in qs if q['path'] != top]
            if rest: out += '<ul class="related">' + ''.join(f'<li><a href="{url(q["path"])}">{esc(q["title"])}</a></li>' for q in rest) + '</ul>'
        return out
    return None

def build_body(p):
    sp = special_html(p)
    body, heads = md(p.get('body', ''))
    if sp is not None: body = body + sp
    extra = ''
    kind = p.get('kind')
    if p.get('levels'):
        extra += penalty_table(p['levels']); heads.append(('penalties', 'Possible Penalties Under Texas Law'))
    cat = C.CATS.get(p.get('cat'))
    if kind == 'criminal' and not p.get('hub'):
        h = f"Defending {p['title']} Cases in Houston &amp; Fort Bend County"
        sid = 'how-we-defend'
        extra += f'<h2 id="{sid}">{h}</h2>' + md(cat['defense'] if cat else C.DEFAULT_DEFENSE)[0]
        heads.append((sid, html.unescape(h)))
        extra += md(C.LOCAL_CRIM)[0]
    if kind == 'pi' and not p.get('hub'):
        extra += '<h2 id="your-claim">Building Your Claim</h2>' + md(C.PI_COMMON)[0]; heads.append(('your-claim', 'Building Your Claim'))
    if p.get('hub'):
        ch = children(p['path'])
        if ch:
            cards = ''.join(f'<a class="card pa-card" href="{url(c["path"])}"><h3>{esc(c["title"])}</h3><p>{esc(c["desc"][:150])}</p><span class="more">Learn more &rarr;</span></a>' for c in ch)
            extra += f'<h2 id="topics">{esc(p.get("hub_label", p["title"] + " Topics"))}</h2><div class="grid g2">{cards}</div>'
            heads.append(('topics', p.get('hub_label', p['title'] + ' Topics')))
    if p.get('faq'):
        extra += '<h2 id="faq">Frequently Asked Questions</h2><div class="faq">' + ''.join(
            f'<details><summary>{esc(q)}</summary><div>{md(a)[0]}</div></details>' for q, a in p['faq']) + '</div>'
        heads.append(('faq', 'Frequently Asked Questions'))
    if kind in ('criminal', 'pi', 'civil', 'info') and p['path'] not in ('contact', 'thank-you'):
        extra += f'''<div class="callout"><h3>Talk With a Houston Attorney Today</h3><p>Whether your case is in Harris County, Fort Bend County, or federal court, an early conversation can protect your options. Call <a href="tel:{TEL}">{PHONE}</a>, email <a href="mailto:{EMAIL}">{EMAIL}</a>, or use the consultation form on this page.</p></div>'''
    sib = siblings(p) if not p.get('hub') else []
    if sib:
        extra += '<h2 id="related">Related Topics</h2><ul class="related">' + ''.join(f'<li><a href="{url(s["path"])}">{esc(s["title"])}</a></li>' for s in sib) + '</ul>'
    toc = ''
    if len(heads) >= 3 and not p.get('no_toc'):
        toc = '<nav class="toc" aria-label="On this page"><h2>Information Center</h2><ul>' + ''.join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in heads) + '</ul></nav>'
    # insert toc after first paragraph
    full = body + extra
    if toc:
        idx = full.find('</p>')
        full = full[:idx + 4] + toc + full[idx + 4:] if idx > -1 else toc + full
    if p.get('pre_html'): full = p['pre_html']() + full
    full = re.sub(r'(<h2 id="(?!faq|topics)[^"]+">)', r'<a class="back-top" href="#main">Back to top</a>\1', full)
    full = full.replace('<a class="back-top" href="#main">Back to top</a>', '', 1)
    return full

def render_interior(p):
    crumbs = crumbs_for(p)
    cr = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + ''.join(
        (f'<li><a href="{h}">{esc(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{esc(n)}</li>') for i, (h, n) in enumerate(crumbs)) + '</ol></nav>'
    main = p.get('html') or build_body(p)
    side = '' if p.get('no_side') else sidebar(p['path'])
    layout = f'<div class="layout"><article class="content">{main}</article>{side}</div>' if side else f'<article class="content" style="padding-bottom:60px">{main}</article>'
    cta = '' if p['path'] in ('contact', 'thank-you') else f'<div class="cta-row"><a class="btn btn-ghost" href="/contact/">Request Your Free Consultation</a></div>'
    return f'''{head(p, crumbs)}
<body>
{header(p['path'])}
<main id="main">
<section class="hero hero-int"><div class="container"><h1>{esc(p.get('h1', p['title']))}</h1>{cta}</div></section>
<div class="container">{cr}{layout}</div>
</main>
{footer()}
</body></html>'''

def render_home(p):
    crumbs = []
    stats = ''.join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in C.STATS)
    quotes = ''.join(f'<blockquote class="quote"><p class="q">&ldquo;{esc(r[1])}&rdquo;</p><cite>&mdash; {esc(r[0])}, Google review</cite></blockquote>' for r in C.REVIEWS[:8])
    res = ''.join(f'<div class="result-card"><p class="verdict">{esc(r[1])}</p><p><b>Matter:</b> {esc(r[0])}</p>{f"<p><b>Detail:</b> {esc(r[2])}</p>" if r[2] else ""}</div>' for r in C.RESULTS[:6])
    pas = ''.join(f'<a class="card pa-card" href="{h}"><h3>{esc(t)}</h3><p>{esc(d)}</p><span class="more">Learn more &rarr;</span></a>' for h, t, d in C.HOME_PRACTICE)
    team = ''.join(C.atty_card(a) for a in C.ATTYS)
    areas = ''.join(f'<li>{esc(a)}</li>' for a in AREAS)
    faq = ''.join(f'<details><summary>{esc(q)}</summary><div>{md(a)[0]}</div></details>' for q, a in p['faq'])
    body_html = md(p['body'])[0]
    return f'''{head(p, crumbs)}
<body>
{header('')}
<main id="main">
<section class="hero hero-home"><div class="container">
 <h1>Houston &amp; Fort Bend County Criminal Defense Attorneys</h1>
 <div class="affil-big">{AFFIL_H}</div>
 <p class="lede">Three generations of Pink family trial lawyers. Aggressive, trial-ready criminal defense &mdash; from the Harris County Criminal Justice Center to the Fort Bend County Justice Center in Richmond.</p>
 <div class="hero-video"><div class="ratio"><iframe src="{YT_EMBED}" title="{FIRM} videos" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div>
 <p style="margin-top:26px"><a class="btn btn-grad" href="/contact/">Get a Free Consultation</a> &nbsp; <a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></p>
</div></section>
<section class="stats" aria-label="Family firm by the numbers"><div class="container">{stats}</div></section>
<p class="stats-note">Figures reflect the combined history of the Pink family of firms, including Walter J. Pink &amp; Associates, PC.</p>

<section class="section"><div class="container">
 <div class="sec-title"><h2>Client Reviews</h2><p>Reviews left on Google for our affiliate, Walter J. Pink &amp; Associates, PC.</p></div>
 <div class="quotes">{quotes}<div class="qdots"></div></div>
 <p style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="/testimonials/">Read More Client Reviews</a></p>
</div></section>

<section class="section section-dark"><div class="container">
 <div class="sec-title"><h2>Case Results</h2><p>A sample of outcomes obtained by the Pink family of firms. Every case is different, and prior results do not guarantee a similar outcome.</p></div>
 <div class="grid g3">{res}</div>
 <p style="text-align:center;margin-top:30px"><a class="btn btn-grad" href="/case-results/">Read More Case Results</a></p>
</div></section>

<section class="section"><div class="container">
 <div class="sec-title"><h2>Practice Areas</h2><p>State, federal and white-collar criminal defense for clients in Houston, Sugar Land, Missouri City, Richmond, Rosenberg, Katy, and across Harris and Fort Bend Counties.</p></div>
 <div class="grid g3">{pas}</div>
</div></section>

<section class="section section-cream"><div class="container">
 <div class="sec-title"><h2>Why {FIRM}</h2></div>
 <div class="content" style="max-width:900px;margin:0 auto">{body_html}</div>
</div></section>

<section class="section"><div class="container">
 <div class="sec-title"><h2>Our Attorneys</h2></div>
 <div class="grid g3">{team}</div>
</div></section>

<section class="section section-dark"><div class="container">
 <div class="sec-title"><h2>Serving Houston &amp; Fort Bend County</h2><p>From our office at {STREET} in Houston&rsquo;s Uptown/Galleria area, we handle cases in Harris County criminal and civil courts, the Fort Bend County Justice Center in Richmond, municipal courts across both counties, and the U.S. District Court for the Southern District of Texas.</p></div>
 <ul class="areas">{areas}</ul>
</div></section>

<section class="section"><div class="container" style="max-width:900px">
 <div class="sec-title"><h2>Frequently Asked Questions</h2></div>
 <div class="faq">{faq}</div>
</div></section>

<section class="section section-cream" id="contact"><div class="container" style="max-width:720px">
 <div class="sec-title"><h2>Request a Free Consultation</h2><p>Call <a href="tel:{TEL}">{PHONE}</a>, email <a href="mailto:{EMAIL}">{EMAIL}</a>, or send the form below.</p></div>
 <div class="card">{form_html('hf', dark=False)}</div>
</div></section>
</main>
{footer()}
</body></html>'''

def write(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f: f.write(s)

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    shutil.copytree(os.path.join(HERE, 'static'), OUT)
    for p in PAGES:
        p.setdefault('title_tag', f"{p['title']} | Houston & Fort Bend Attorney | {FIRM}" if p['path'] != 'index' else f"{FIRM} | Houston & Fort Bend Criminal Defense Lawyer")
        if len(p['title_tag']) > 75 and p['path'] != 'index':
            p['title_tag'] = f"{p['title']} | Houston & Fort Bend | {FIRM}"
    for p in PAGES:
        if p['path'] == 'index':
            write(os.path.join(OUT, 'index.html'), render_home(p))
        else:
            write(os.path.join(OUT, p['path'], 'index.html'), render_interior(p))
    # 404
    p404 = {'path': '404', 'title': 'Page Not Found', 'desc': 'The page you requested could not be found.', 'kind': 'page',
            'title_tag': f'Page Not Found | {FIRM}', 'no_side': True,
            'html': f'<p>Sorry, that page does not exist. Try the <a href="/site-map/">site map</a>, go <a href="/">home</a>, or call <a href="tel:{TEL}">{PHONE}</a>.</p>'}
    s = render_interior(p404).replace('<meta name="robots" content="index, follow', '<meta name="robots" content="noindex, follow')
    write(os.path.join(OUT, '404.html'), s)
    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in PAGES:
        if p['path'] == 'thank-you': continue
        pr = '1.0' if p['path'] == 'index' else ('0.8' if p.get('hub') or p['path'].startswith('attorneys') else '0.6')
        sm.append(f'<url><loc>{absu(p["path"]) if p["path"]!="index" else SITE_URL+"/"}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>')
    sm.append('</urlset>')
    write(os.path.join(OUT, 'sitemap.xml'), '\n'.join(sm))
    # robots
    bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'anthropic-ai',
            'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Googlebot', 'Bingbot', 'Applebot', 'Applebot-Extended',
            'DuckAssistBot', 'meta-externalagent', 'CCBot', 'Amazonbot', 'YouBot', 'cohere-ai', 'MistralAI-User']
    rb = ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) + f'User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {SITE_URL}/sitemap.xml\n'
    write(os.path.join(OUT, 'robots.txt'), rb)
    # llms.txt + llms-full.txt
    import llms
    write(os.path.join(OUT, 'llms.txt'), llms.short(globals()))
    write(os.path.join(OUT, 'llms-full.txt'), llms.full(globals()))
    # vercel.json
    vj = {'cleanUrls': True, 'trailingSlash': True,
          'redirects': [{'source': s, 'destination': d, 'permanent': True} for s, d in C.REDIRECTS],
          'headers': [{'source': '/assets/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=604800'}]},
                      {'source': '/(.*)', 'headers': [{'key': 'X-Content-Type-Options', 'value': 'nosniff'},
                                                      {'key': 'Referrer-Policy', 'value': 'strict-origin-when-cross-origin'},
                                                      {'key': 'X-Frame-Options', 'value': 'SAMEORIGIN'}]}]}
    write(os.path.join(OUT, 'vercel.json'), json.dumps(vj, indent=2))
    print('pages:', len(PAGES), '->', OUT)

if __name__ == '__main__':
    main()
