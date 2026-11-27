#!/usr/bin/env python3
"""Builds the static site for Walter J. Pink & Associates, P.C. into ../site"""
import os, json

OUT = os.path.join(os.path.dirname(__file__), "..")
FIRM = "Walter J. Pink &amp; Associates, P.C."
PHONE = "(713) 664-6651"
TEL = "+17136646651"
ADDR1 = "1717 St. James Place, Suite 690"
ADDR2 = "Houston, TX 77056"
MAPS = "https://www.google.com/maps/search/?api=1&query=1717+St.+James+Place+Suite+690+Houston+TX+77056"
# Replace with your Formspree (or similar) form endpoint so the form emails you.
FORM_ACTION = "https://formspree.io/f/YOUR_FORM_ID"
SITE_URL = "https://walterjpink.com"

CRIMINAL = [
    ("criminal-defense.html", "Criminal defense overview"),
    ("dwi.html", "DWI / DUI"),
    ("drug-charges.html", "Drug charges"),
    ("domestic-violence.html", "Domestic &amp; family violence"),
    ("murder-homicide.html", "Murder &amp; homicide"),
    ("weapons.html", "Weapons charges"),
    ("federal-crimes.html", "Federal crimes"),
    ("theft.html", "Theft"),
    ("robbery.html", "Robbery"),
    ("burglary.html", "Burglary"),
    ("expunction.html", "Expunction &amp; record sealing"),
]
ABOUT = [
    ("about.html", "Our history"),
    ("attorneys.html", "Our attorneys"),
    ("augustin-t-pink.html", "Augustin T. Pink"),
    ("ishmael-g-a-pink.html", "Ishmael G.A. Pink"),
    ("results.html", "Case results"),
    ("faq.html", "Criminal law FAQ"),
]

MARK = """<svg class="brand-mark" viewBox="0 0 48 48" aria-hidden="true"><rect x="1.5" y="1.5" width="45" height="45" fill="none" stroke="#B8892B" stroke-width="3"/><text x="24" y="31" text-anchor="middle" font-family="Zilla Slab, Georgia, serif" font-weight="700" font-size="17" fill="#fff">WJP</text></svg>"""


def head(title, desc, path):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE_URL}/{'' if path == 'index.html' else path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&family=Zilla+Slab:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">{json.dumps({
  "@context": "https://schema.org", "@type": "LegalService",
  "name": "Walter J. Pink & Associates, P.C.", "telephone": "+1-713-664-6651",
  "url": SITE_URL,
  "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Houston",
              "addressRegion": "TX", "postalCode": "77056", "addressCountry": "US"},
  "areaServed": ["Harris County", "Fort Bend County", "Houston"]})}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def dropdown(label, items, current):
    lis = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in items)
    return f'<li class="has-sub"><button class="navlink" aria-expanded="false">{label}</button><ul class="sub">{lis}</ul></li>'


def header(current):
    return f"""<div class="topbar"><div class="wrap"><span>Free, confidential consultations. Call or text any time.</span><a href="tel:{TEL}">{PHONE}</a></div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">{MARK}<span class="brand-text"><strong>Walter J. Pink</strong><small>&amp; Associates, P.C. &nbsp;|&nbsp; Houston criminal defense</small></span></a>
<button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="nav" id="site-nav" aria-label="Main">
<ul>
{dropdown("Criminal defense", CRIMINAL, current)}
<li><a href="dwi.html">DWI defense</a></li>
<li><a href="results.html">Case results</a></li>
{dropdown("About", ABOUT, current)}
<li><a href="contact.html">Contact</a></li>
</ul>
<a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a>
</nav>
</div></header>
"""


def band():
    return f"""<section class="band"><div class="wrap"><div><h2>Charged with a crime in Houston?</h2><p>Talk to an attorney today. The consultation is free and confidential.</p></div>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-brass" href="tel:{TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="contact.html">Request a consultation</a></div></div></section>
"""


def footer():
    crim = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in CRIMINAL[:8])
    about = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in ABOUT)
    return f"""<footer class="site-footer">
<div class="wrap">
<div><a class="brand" href="index.html">{MARK}<span class="brand-text"><strong>Walter J. Pink</strong><small>&amp; Associates, P.C.</small></span></a>
<p style="margin-top:18px">{ADDR1}<br>{ADDR2}<br><a href="{MAPS}" target="_blank" rel="noopener">Get directions</a></p>
<p><a href="tel:{TEL}" style="font-weight:700;font-size:1.15rem">{PHONE}</a><br>Office visits by appointment.</p></div>
<div><h4>Criminal defense</h4><ul>{crim}</ul></div>
<div><h4>About the firm</h4><ul>{about}</ul></div>
<div><h4>Courts we serve</h4><ul><li>Harris County</li><li>Fort Bend County</li><li>Brazoria &amp; Galveston Counties</li><li>Montgomery County</li><li>Southern District of Texas (federal)</li></ul></div>
</div>
<div class="legal"><div class="wrap"><span>&copy; <span id="year">2026</span> {FIRM} All rights reserved. Attorney advertising.</span><span><a href="disclaimer.html">Disclaimer</a> &nbsp;|&nbsp; <a href="disclaimer.html#privacy">Privacy</a></span></div></div>
</footer>
<script src="js/main.js"></script>
</body></html>
"""


def write(path, title, desc, body):
    html = head(title, desc, path) + header(path) + '<main id="main">' + body + "</main>" + band() + footer()
    with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
        f.write(html)


def sidebar(current, extra_nav=None):
    items = extra_nav or CRIMINAL
    lis = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in items)
    return f"""<aside class="sidebar">
<div class="side-cta"><h3>Free consultation</h3><p>Tell us what happened. An attorney will review your case and explain your options.</p>
<a class="phone" href="tel:{TEL}">{PHONE}</a><a class="btn btn-brass" href="contact.html" style="width:100%">Request a consultation</a></div>
<nav class="side-nav" aria-label="Practice areas"><h3>{'Criminal defense' if not extra_nav else 'About the firm'}</h3><ul>{lis}</ul></nav>
</aside>"""


def interior(path, title, desc, h1, lede, prose, crumb="Criminal defense", nav=None):
    body = f"""<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / {crumb}</div><h1>{h1}</h1><p>{lede}</p></div></section>
<div class="wrap content-grid"><article class="prose">{prose}</article>{sidebar(path, nav)}</div>"""
    write(path, title, desc, body)


def faq_block(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in items) + "</div>"


def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="penalties"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


RESULTS_DISCLAIMER = ("Every case is different. Past results do not guarantee a similar outcome in any other matter, "
                      "and they depend on the facts and law of each case.")

# ---------------------------------------------------------------- HOME
HOME_FAQ = [
    ("Do I need a lawyer if I haven't been charged yet?",
     "Yes. The earlier we are involved, the more we can do. Before charges are filed we can speak with detectives, prepare a grand jury packet, and preserve evidence such as video that may be overwritten within days."),
    ("Should I talk to the police if I'm innocent?",
     "Not without a lawyer. Give your name and identification, then say you want an attorney. Statements are easily taken out of context, and recorded jail calls are routinely used by prosecutors."),
    ("How much will my case cost?",
     "Criminal cases are handled on a flat fee, so you know the cost up front. The fee depends on the charge, whether it is a misdemeanor or felony, and whether the case is likely to go to trial. Payment plans are available."),
    ("Can the alleged victim drop the charges?",
     "No. In Texas, the State decides whether to prosecute. A complainant who no longer wants to proceed can still matter, and we know how to present that to prosecutors properly."),
    ("Will my case go to trial?",
     "Most cases are resolved before trial through dismissal, reduction, or a negotiated outcome. Prosecutors make better offers to attorneys they know are ready to try the case, and our attorneys have tried hundreds."),
    ("Can I get my arrest off my record?",
     "Often, yes. A dismissal or acquittal may qualify for expunction, which destroys the records. Deferred adjudication may qualify for an order of nondisclosure, which seals the record from most public view."),
    ("What courts do you handle?",
     "We appear daily in Harris County and Fort Bend County courts, and handle cases in Brazoria, Galveston, Montgomery and other Texas counties, as well as the federal Southern District of Texas."),
]

home = f"""
<section class="hero"><div class="wrap">
<div>
<h1>Three generations defending Houston.</h1>
<p class="lede">For more than 50 years the Pink family has stood beside people accused of crimes in Harris County, Fort Bend County and federal court. If you or someone you love has been arrested, we can start on your case today.</p>
<div class="hero-actions"><a class="btn btn-brass" href="tel:{TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="contact.html">Request a free consultation</a></div>
</div>
<div class="hero-card">
<h2>Arrested or under investigation?</h2>
<p>Don't answer questions or explain yourself to police. Call us first. We can help with bond, jail release and the first court setting.</p>
<a class="phone" href="tel:{TEL}">{PHONE}</a>
<p style="margin:0">{ADDR1}, {ADDR2}</p>
</div>
</div></section>

<section class="record" aria-label="Firm record"><div class="wrap">
<div><b>50+</b><span>years in practice</span></div>
<div><b>25,000+</b><span>cases handled</span></div>
<div><b>600+</b><span>criminal trials</span></div>
<div><b>3,000+</b><span>dismissals</span></div>
</div></section>

<section class="section"><div class="wrap legacy">
<blockquote>He traded his boxing gloves for the gloves of freedom and justice.<cite>The story of our founder, Walter Jerome Pink</cite></blockquote>
<div>
<h2>A firm built by a fighter</h2>
<p>Walter J. Pink was a heavyweight boxer known as &ldquo;The Tobasco Kid&rdquo; and a college professor at 28 when two injustices on the same day changed his course. He watched a student wrongfully arrested, and his wife, Betty, was discriminated against at a local business. He decided the battles that mattered most to his community would be fought in court.</p>
<p>Over more than 30 years he handled over 20,000 criminal cases, tried more than 600 of them, and was recognized by the Texas Senate for his work. His son Augustin and grandson Ishmael carry that same fight into Houston courtrooms today.</p>
<a class="btn btn-outline" href="about.html">Read our history</a>
</div>
</div></section>

<section class="section alt"><div class="wrap">
<div class="section-head"><h2>Recent criminal case results</h2><p>A few outcomes from our results page. Many of these clients were told to expect the worst.</p></div>
<div class="results">
<div class="result"><div class="outcome">Dismissed</div><div class="body"><h3>Capital murder</h3><p>Self-defense case that stayed open for years. The State dismissed close to trial after our motions and evidentiary challenges.</p></div></div>
<div class="result"><div class="outcome">No bill</div><div class="body"><h3>Murder</h3><p>Our client shot a man who was trying to stab him. We prepared him, spoke with detectives, and the grand jury declined to indict.</p></div></div>
<div class="result"><div class="outcome">Dismissed</div><div class="body"><h3>DWI, nearly 3&times; the limit</h3><p>Our client refused testing, and police got a warrant for a blood draw. The case was dismissed anyway.</p></div></div>
</div>
<p class="fineprint" style="margin-top:22px">{RESULTS_DISCLAIMER}</p>
<a class="btn btn-primary" href="results.html">See all case results</a>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>What clients say</h2><p>Summaries of client reviews from the cases they hired us for.</p></div>
<div class="reviews">
<!-- Replace each summary below with the client's exact review text before publishing. -->
<article class="review"><div class="stars" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>Got a bond set within 24 hours, and the case ended with no jail time.</p><footer>Bahira S.<small>Criminal case</small></footer></article>
<article class="review"><div class="stars" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>Facing as much as nine years in a federal case, the sentence came down to five.</p><footer>Traveon A.<small>Federal case</small></footer></article>
<article class="review"><div class="stars" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>Acquitted of aggravated robbery after a strong fight in the courtroom.</p><footer>Michael D.<small>Jury trial</small></footer></article>
</div>
</div></section>

<section class="section alt"><div class="wrap">
<div class="section-head"><h2>How we handle your case</h2><p>The work starts the day you call, not the week before trial.</p></div>
<ol class="steps">
<li><h3>Get you out and protect your rights</h3><p>We move on bond and jail release, and we make sure you stop talking to anyone but your lawyer.</p></li>
<li><h3>Preserve the evidence</h3><p>Surveillance video, phone records, texts and witness names disappear fast. We secure them early.</p></li>
<li><h3>Test the State's case</h3><p>We review the stop, the search, the lab work and every statement for constitutional and procedural problems.</p></li>
<li><h3>Negotiate from strength</h3><p>Prosecutors know we try cases. That leverage is what produces dismissals, reductions and no-bills.</p></li>
<li><h3>Try the case when it should be tried</h3><p>If the right answer is a jury, we are ready. Three generations of this family have tried more than 600 cases.</p></li>
<li><h3>Clear your record afterward</h3><p>When your case qualifies, we pursue expunction or nondisclosure so the arrest stops following you.</p></li>
</ol>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Criminal cases we handle</h2><p>State and federal charges, misdemeanor through capital felony.</p></div>
<div class="practice-grid">
<a href="dwi.html"><h3>DWI / DUI</h3><p>First DWI, felony DWI, intoxication assault and manslaughter, ALR hearings.</p></a>
<a href="drug-charges.html"><h3>Drug charges</h3><p>Possession, intent to deliver, manufacturing and trafficking.</p></a>
<a href="domestic-violence.html"><h3>Family violence</h3><p>Assault family violence, impeding breath, protective orders.</p></a>
<a href="murder-homicide.html"><h3>Murder &amp; homicide</h3><p>Capital murder, murder, manslaughter and self-defense cases.</p></a>
<a href="weapons.html"><h3>Weapons charges</h3><p>Unlawful carrying, felon in possession, prohibited weapons.</p></a>
<a href="federal-crimes.html"><h3>Federal crimes</h3><p>Drug, firearm, fraud and cyber cases in the Southern District of Texas.</p></a>
<a href="theft.html"><h3>Theft</h3><p>Shoplifting, embezzlement, theft of services, stolen property.</p></a>
<a href="robbery.html"><h3>Robbery</h3><p>Robbery and aggravated robbery with a deadly weapon.</p></a>
<a href="burglary.html"><h3>Burglary</h3><p>Burglary of a habitation, building or vehicle, criminal trespass.</p></a>
</div>
</div></section>

<section class="section alt"><div class="wrap split">
<div class="portrait" style="max-width:420px">AP<!-- <img src="img/augustin-t-pink.jpg" alt="Augustin T. Pink"> --></div>
<div>
<h2>Meet Augustin T. Pink</h2>
<p class="attorney-role" style="color:var(--oxblood);font-weight:700">Partner and lead criminal defense strategist</p>
<p>Augustin Pink has practiced law since 1992. In more than 30 years in Texas and federal courts, he has won dismissals, jury acquittals and reduced federal sentences for clients facing the most serious charges in Houston.</p>
<p>He learned the work from his father, Walter J. Pink, and has carried the firm's criminal practice forward alongside his nephew, Ishmael G.A. Pink. His practice has also taken him through legal systems in Africa and South America.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="augustin-t-pink.html">Read Augustin's bio</a><a class="btn btn-outline" href="attorneys.html">Meet the whole team</a></div>
</div>
</div></section>

<section class="section dark"><div class="wrap">
<div class="section-head"><h2>Arrested for DWI? The clock has already started.</h2><p>A DWI arrest creates two cases: the criminal charge and a separate fight over your driver's license. We handle both.</p></div>
<div class="tiles">
<div class="tile"><h3>License hearing (ALR)</h3><p>Request the hearing in time or your license is suspended automatically.</p></div>
<div class="tile"><h3>Breath and blood tests</h3><p>Calibration, maintenance, blood handling and chain of custody all get examined.</p></div>
<div class="tile"><h3>Field sobriety tests</h3><p>Uneven roads, medical issues and poor instructions undermine the results.</p></div>
<div class="tile"><h3>Drivers under 21</h3><p>Any detectable alcohol is a DUI for minors. A first offense may be expunged later.</p></div>
</div>
<div class="deadline"><b>15</b><p><strong>days to request your ALR hearing.</strong> Miss it and your license is suspended without a fight. Call us the same day you are released.</p></div>
<p style="margin-top:26px"><a class="btn btn-brass" href="dwi.html">Learn about DWI defense</a></p>
</div></section>

<section class="section" id="consult"><div class="wrap contact-grid">
<div>
<h2>Request a free consultation</h2>
<p>Tell us briefly what happened. An attorney will contact you to discuss your case.</p>
<form class="consult" action="{FORM_ACTION}" method="POST">
<div class="row2"><div class="field"><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div>
<div class="field"><label for="p">Phone</label><input id="p" name="phone" type="tel" autocomplete="tel" required></div></div>
<div class="field"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email"></div>
<div class="field"><label for="c">Type of charge</label><select id="c" name="charge"><option>DWI / DUI</option><option>Drug charge</option><option>Family violence</option><option>Murder / homicide</option><option>Weapons</option><option>Federal charge</option><option>Theft / robbery / burglary</option><option>Other</option></select></div>
<div class="field"><label for="m">Brief description</label><textarea id="m" name="message" placeholder="County, court date if you have one, and a short summary"></textarea></div>
<button class="btn btn-primary" type="submit">Send my request</button>
<p class="form-note">Sending this form does not create an attorney-client relationship. Please don't include confidential details. We'll discuss those privately.</p>
</form>
</div>
<div class="office" style="background:var(--navy);padding:36px">
<h3>Our office</h3>
<p>{ADDR1}<br>{ADDR2}</p>
<a class="big" href="tel:{TEL}">{PHONE}</a>
<p>Office visits by appointment. Call or text any time, including nights and weekends.</p>
<p><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></p>
<iframe class="map-frame" title="Map to our office" loading="lazy" src="https://www.google.com/maps?q=1717+St.+James+Place+Suite+690+Houston+TX+77056&output=embed"></iframe>
</div>
</div></section>

<section class="section alt"><div class="wrap">
<div class="section-head"><h2>Houston criminal defense lawyers</h2></div>
<div class="prose" style="max-width:52em">
<p>A criminal charge in Harris County moves through one of 24 felony district courts or 16 county criminal courts at law at the Criminal Justice Center on Franklin Street. In Fort Bend County, cases are heard in Richmond, including the 240th, 268th and 400th District Courts. Knowing these courts, their judges and their prosecutors matters, and we are in them every week.</p>
<p>We defend people charged with <a href="dwi.html">DWI</a>, <a href="drug-charges.html">drug offenses</a>, <a href="domestic-violence.html">family violence</a>, <a href="weapons.html">weapons charges</a>, <a href="murder-homicide.html">homicide</a> and <a href="federal-crimes.html">federal crimes</a>. Criminal cases are handled on a flat fee, and every consultation is free.</p>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Frequently asked questions</h2></div>
{faq_block(HOME_FAQ)}
<p style="margin-top:24px"><a href="faq.html">More criminal law questions</a></p>
</div></section>
"""
write("index.html", "Houston Criminal Defense Lawyers | Walter J. Pink & Associates, P.C.",
      "Three generations of Houston criminal defense lawyers. 50+ years, 25,000+ cases, 600+ trials. Free consultation: (713) 664-6651.",
      home)

# ---------------------------------------------------------------- ABOUT / HISTORY
about = f"""
<h2>The Tobasco Kid</h2>
<p>Before he was a lawyer, Walter Jerome Pink was a heavyweight boxer. They called him &ldquo;The Tobasco Kid,&rdquo; and he was known for the power in his hands. He was also a college professor, teaching by the age of 28.</p>
<p>Then came a single day that changed everything. He witnessed a student arrested wrongfully and illegally. That same day, his wife, Betty Pink, was discriminated against at a business. He came away convinced that the fights that mattered most for his community would be won or lost in the legal system, and he went to law school to fight them.</p>
<div class="callout"><p>In his own words, he traded his boxing gloves for the &ldquo;gloves of freedom and justice.&rdquo;</p></div>

<h2>A career in the courtroom</h2>
<p>Walter J. Pink became known in Houston as a civil rights advocate and a lawyer who would take on any fight. Over more than three decades of practice, he:</p>
<ul>
<li>handled more than 20,000 criminal cases</li>
<li>tried more than 600 criminal cases to verdict</li>
<li>was formally recognized by the Texas Senate for his work</li>
</ul>

<h2>Three generations</h2>
<ol class="timeline">
<li><h3>Walter J. Pink, founder</h3><p>Boxer, professor and civil rights lawyer who built the firm on trial work and refusing to back down.</p></li>
<li><h3>Augustin T. Pink and Clement B. Pink</h3><p>His sons. Augustin, licensed in 1992, leads the criminal defense practice. Clement leads civil litigation and personal injury.</p></li>
<li><h3>Ishmael G.A. Pink</h3><p>His grandson. A two-time University of Texas graduate who rose from law clerk to partner, with a focus on DWI and serious criminal charges.</p></li>
</ol>

<h2>The firm today</h2>
<p>{FIRM} practices from {ADDR1} in Houston's Galleria area. Across five decades, the family has handled more than 25,000 cases and more than 600 trials. We take criminal cases on a flat fee, we answer the phone, and we still believe what the founder believed: every case is worth fighting.</p>
<p><a class="btn btn-primary" href="attorneys.html">Meet our attorneys</a></p>
"""
interior("about.html", "Our History | Walter J. Pink & Associates, P.C.",
         "The story of Walter J. Pink, the boxer and civil rights lawyer who founded a three-generation Houston criminal defense firm.",
         "From the boxing ring to the courtroom", "How a heavyweight boxer and college professor built a Houston law firm that has defended Texans for more than 50 years.",
         about, crumb="About", nav=ABOUT)

# ---------------------------------------------------------------- ATTORNEYS
attorneys = f"""
<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / About</div><h1>Our attorneys</h1><p>A family of trial lawyers, now in its third generation.</p></div></section>
<section class="section"><div class="wrap">
<div class="team">
<article class="attorney"><div class="portrait">AP<!-- <img src="img/augustin-t-pink.jpg" alt="Augustin T. Pink"> --></div><div class="body"><h3>Augustin T. Pink</h3><div class="role">Partner, lead criminal defense strategist</div><p>Practicing since 1992. More than 30 years winning dismissals, acquittals and reduced federal sentences.</p><a href="augustin-t-pink.html">Full bio</a></div></article>
<article class="attorney"><div class="portrait">IP<!-- <img src="img/ishmael-g-a-pink.jpg" alt="Ishmael G.A. Pink"> --></div><div class="body"><h3>Ishmael G.A. Pink</h3><div class="role">Partner</div><p>University of Texas undergraduate and law graduate. Defends serious criminal charges, with a focus on DWI.</p><a href="ishmael-g-a-pink.html">Full bio</a></div></article>
<article class="attorney"><div class="portrait">CP<!-- <img src="img/clement-b-pink.jpg" alt="Clement B. Pink"> --></div><div class="body"><h3>Clement B. Pink</h3><div class="role">Partner, civil litigation &amp; personal injury</div><p>Leads the firm's civil and injury practice, with more than $25 million recovered in settlements. Former NCAA Division I basketball player.</p></div></article>
</div>
</div></section>
"""
write("attorneys.html", "Our Attorneys | Walter J. Pink & Associates, P.C.",
      "Meet Augustin T. Pink, Ishmael G.A. Pink and Clement B. Pink, Houston trial lawyers.", attorneys)

augustin = f"""
<h2>Lead criminal defense strategist</h2>
<p>Augustin T. Pink is a partner at {FIRM} and leads the firm's criminal defense practice. He was licensed in 1992 and has spent more than 30 years in Texas state courts and federal court defending people accused of crimes.</p>
<p>His work has produced the outcomes clients come to the firm for: cases dismissed, juries returning not-guilty verdicts, and federal sentences reduced well below what the government sought.</p>

<h2>Carrying the founder's fight forward</h2>
<p>Augustin is the son of the firm's founder, Walter J. Pink, and learned trial work in his father's practice. He brings the same approach to every file: investigate early, challenge everything the State cannot prove, and be ready to try the case.</p>
<p>His practice has also taken him beyond Texas, navigating legal systems in Africa and South America.</p>

<h2>Practice areas</h2>
<ul>
<li><a href="murder-homicide.html">Murder and homicide</a></li>
<li><a href="dwi.html">DWI / DUI</a></li>
<li><a href="drug-charges.html">Drug charges</a></li>
<li><a href="federal-crimes.html">Federal criminal defense</a></li>
<li><a href="theft.html">Theft</a> and <a href="burglary.html">burglary</a></li>
</ul>
<!-- Add: law school, bar admissions, memberships and awards here. -->
"""
interior("augustin-t-pink.html", "Augustin T. Pink | Houston Criminal Defense Attorney",
         "Augustin T. Pink, partner and lead criminal defense strategist at Walter J. Pink & Associates. Practicing since 1992.",
         "Augustin T. Pink", "Partner and lead criminal defense strategist. Practicing law since 1992.", augustin, crumb="Attorneys", nav=ABOUT)

ishmael = f"""
<h2>The next generation</h2>
<p>Ishmael G.A. Pink is a partner at {FIRM} and the grandson of its founder, Walter J. Pink. He earned both his undergraduate degree and his Doctor of Jurisprudence from the University of Texas.</p>
<p>He started at the firm as a law clerk and worked his way to partner, learning the practice from inside a family that has defended Houstonians for more than 50 years. He pairs that tradition with a modern, forward-looking approach to case strategy.</p>

<h2>Practice focus</h2>
<ul>
<li>Defense of people facing serious criminal charges, with a particular focus on <a href="dwi.html">DWI and DUI</a></li>
<li>Complex negotiations with prosecutors and opposing parties</li>
<li>Personal injury claims against large insurance companies</li>
<li>Business formation and planning</li>
</ul>

<h2>How he works</h2>
<p>Ishmael's clients describe counsel that is both strategic and compassionate. He keeps clients informed, explains each step in plain terms, and prepares every case as if it will be tried.</p>
<!-- Add: graduation years, bar admission, memberships and awards here. -->
"""
interior("ishmael-g-a-pink.html", "Ishmael G.A. Pink | Houston Criminal Defense & DWI Attorney",
         "Ishmael G.A. Pink, partner at Walter J. Pink & Associates. University of Texas graduate focused on DWI and serious criminal charges.",
         "Ishmael G.A. Pink", "Partner. Two-time University of Texas graduate, third generation of the Pink family in law.", ishmael, crumb="Attorneys", nav=ABOUT)

# ---------------------------------------------------------------- RESULTS
crim_results = [
    ("Dismissed", "Capital murder", "Self-defense against someone the client trusted. The case stayed open for years; the State dismissed near trial after our motions and evidentiary challenges."),
    ("No bill", "Murder", "Client defended himself and his friends. We prepared and presented a grand jury packet, and no charges were filed."),
    ("No bill", "Murder", "Client shot a man who was trying to stab him. We prepared him and spoke with detectives on his behalf."),
    ("4 years", "Intoxication manslaughter", "The State sought 15 years at a PSI hearing after the client's passenger and best friend died. Sentence: 4 years, parole-eligible after 2."),
    ("Dismissed", "DWI", "Client was driving on the wrong side of the road and blew more than double the legal limit."),
    ("Dismissed", "DWI", "Client refused testing; police obtained a blood warrant showing nearly three times the legal limit."),
    ("Dismissed", "DWI", "Client totaled his vehicle after hitting a city bus, with a BAC about double the limit."),
    ("Dismissed", "Family violence, impeding breath (felony)", "Photos showed bruising on the complainant's neck. We showed the client did not cause it."),
    ("Dismissed", "Domestic violence", "The complainant falsely claimed the client bit her. We proved the allegation was fabricated."),
    ("Dismissed", "Domestic violence", "The complainant bit the client's back, then told police he was the aggressor."),
    ("Dismissed", "Burglary and domestic violence", "The complainant locked the client out, then told police he broke in to attack her."),
    ("Dismissed", "Terroristic threat (family)", "The threat was fabricated by the client's boyfriend, and we disproved it."),
    ("Dismissed", "Aggravated assault with a deadly weapon", "Client picked up a metal pipe to defend himself from the aggressor."),
    ("Dismissed", "Aggravated assault with a deadly weapon", "Others displayed guns; a witness falsely said our client directed them to shoot."),
    ("Dismissed", "Assault on a peace officer and retaliation", "Both charges dismissed after a wrongful stop. The client kept a clean record."),
    ("Deferred", "Assault on a peace officer", "Before we were hired, the offer was 2 years in TDCJ. Result: 5 years deferred probation, with no conviction."),
]
cards = "".join(f'<div class="result"><div class="outcome">{o}</div><div class="body"><h3>{c}</h3><p>{d}</p></div></div>' for o, c, d in crim_results)
results = f"""
<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Case results</div><h1>Criminal case results</h1><p>Dismissals, no-bills and reduced sentences, including cases where clients were told there was no way out.</p></div></section>
<section class="section"><div class="wrap">
<div class="results">{cards}</div>
<p class="fineprint" style="margin-top:28px">{RESULTS_DISCLAIMER} Results shown are criminal matters handled by the firm.</p>
</div></section>
"""
write("results.html", "Criminal Case Results | Walter J. Pink & Associates, P.C.",
      "Dismissed capital murder, murder no-bills, dismissed DWIs and more from a Houston criminal defense firm.", results)

# ---------------------------------------------------------------- CRIMINAL OVERVIEW
overview = f"""
<h2>What a defense lawyer does from day one</h2>
<p>A good defense starts long before trial. From the first call, we look at how police gathered the evidence and what the witnesses actually saw. We talk to prosecutors before the first hearing and appear at every setting from arraignment through resolution. The earlier we are involved, the more we can change.</p>

<h2>Protect yourself before you say another word</h2>
<ul>
<li><strong>Stay silent.</strong> Identify yourself, then ask for a lawyer. Jail calls are recorded and prosecutors use them.</li>
<li><strong>Write it down.</strong> While your memory is fresh, note what happened, the officers involved and anyone who saw it.</li>
<li><strong>Save the evidence.</strong> Keep texts, photos, receipts and arrest and bond paperwork. Nearby camera footage is often overwritten within days.</li>
<li><strong>Call a defense attorney now,</strong> not after your first court date.</li>
</ul>

<h2>How a Texas criminal case moves</h2>
<ol class="timeline">
<li><h3>Arrest and bond</h3><p>A magistrate sets bail. We can ask the court to lower bond or change release conditions.</p></li>
<li><h3>First appearance</h3><p>The charges are read and a plea is entered. If bail wasn't set earlier, the judge sets it here.</p></li>
<li><h3>Pretrial</h3><p>We review the State's evidence, file motions to suppress and negotiate. Many cases are dismissed or reduced at this stage.</p></li>
<li><h3>Trial</h3><p>The State must prove every element beyond a reasonable doubt. If the case should be tried, we try it.</p></li>
</ol>

<h2>Texas offense levels</h2>
{table(["Offense level", "Punishment range"], [
    ["Class C misdemeanor", "Fine up to $500"],
    ["Class B misdemeanor", "Up to 180 days in jail and/or fine up to $2,000"],
    ["Class A misdemeanor", "Up to 1 year in jail and/or fine up to $4,000"],
    ["State jail felony", "180 days to 2 years in state jail, fine up to $10,000"],
    ["Third-degree felony", "2 to 10 years in prison, fine up to $10,000"],
    ["Second-degree felony", "2 to 20 years in prison, fine up to $10,000"],
    ["First-degree felony", "5 to 99 years or life, fine up to $10,000"],
    ["Capital felony", "Life without parole or death"],
])}

<h2>The courts we work in</h2>
<p><strong>Harris County:</strong> felonies are heard in 24 criminal district courts and misdemeanors in 16 county criminal courts at law, at the Criminal Justice Center, 1201 Franklin Street.</p>
<p><strong>Fort Bend County:</strong> felonies go to district courts including the 240th, 268th and 400th, and misdemeanors to the county courts at law at the Justice Center in Richmond. We represent clients from Sugar Land, Missouri City and Rosenberg.</p>
<p>We also handle cases in Brazoria, Galveston, Montgomery and other Texas counties, and in <a href="federal-crimes.html">federal court</a>.</p>

<h2>Consequences beyond the sentence</h2>
<p>A conviction can affect your job, professional license, housing and right to own a firearm. A felony suspends your right to vote until the sentence is fully discharged. For non-citizens, many convictions carry immigration consequences. Some cases can be sealed or erased afterward through <a href="expunction.html">expunction or nondisclosure</a>.</p>

<h2>What it costs</h2>
<p>We handle criminal cases on a flat fee, so you know the cost before we start. The fee depends on the charge and whether the case is likely to be tried. Payment plans are available, and the consultation is free.</p>
"""
interior("criminal-defense.html", "Houston Criminal Defense Attorney | Walter J. Pink & Associates",
         "Houston criminal defense for misdemeanors, felonies and federal charges in Harris and Fort Bend County. Free consultation.",
         "Houston criminal defense attorneys", "Misdemeanor to capital felony, state and federal. Here's what to do now and how your case will move.", overview)

# ---------------------------------------------------------------- DWI
dwi = f"""
<h2>DWI and DUI are not the same charge</h2>
<p><strong>DWI</strong> applies to any driver who has lost the normal use of their mental or physical faculties, or who has a blood alcohol concentration of 0.08 or more. <strong>DUI</strong> applies only to drivers under 21, and any detectable amount of alcohol is enough. Adults face DWI; minors can face either.</p>

<h2>DWI penalties in Texas</h2>
{table(["Offense", "Level", "Range"], [
    ["First DWI", "Class B misdemeanor", "72 hours to 180 days in jail, fine up to $2,000, license suspension up to 1 year"],
    ["First DWI, BAC 0.15 or higher", "Class A misdemeanor", "Up to 1 year in jail, fine up to $4,000"],
    ["Second DWI", "Class A misdemeanor", "30 days to 1 year in jail, fine up to $4,000, suspension up to 2 years"],
    ["Third DWI or more", "Third-degree felony", "2 to 10 years in prison, fine up to $10,000"],
    ["DWI with a child passenger (under 15)", "State jail felony", "180 days to 2 years in state jail"],
    ["Intoxication assault", "Third-degree felony", "2 to 10 years in prison"],
    ["Intoxication manslaughter", "Second-degree felony", "2 to 20 years in prison"],
])}
<p>A conviction can also bring an ignition interlock, annual costs, higher insurance and a permanent record.</p>

<h2>Your license: the 15-day deadline</h2>
<p>Texas has implied consent. If you refuse a breath or blood test after a DWI arrest, or test over the limit, your license faces an automatic Administrative License Revocation (ALR). A first refusal means a 180-day suspension, and up to two years with a prior.</p>
<div class="callout"><p><strong>You have 15 days from the notice of suspension to request an ALR hearing.</strong> If you miss it, the suspension takes effect without a hearing. The hearing is also our first chance to cross-examine the arresting officer.</p></div>

<h2>If you're stopped</h2>
<ul>
<li>Provide license, registration and insurance calmly.</li>
<li>You don't have to answer questions about where you've been or what you drank.</li>
<li>Roadside field sobriety tests and the portable breath test are voluntary.</li>
<li>Stay respectful. Body and dash cameras record everything.</li>
</ul>

<h2>How DWI cases are won</h2>
<ul>
<li><strong>The stop.</strong> Police need reasonable suspicion. Evidence from an unlawful stop can be suppressed.</li>
<li><strong>Field sobriety tests.</strong> Improper instructions, bad surfaces, footwear and medical conditions all affect results.</li>
<li><strong>Breath and blood testing.</strong> We examine calibration and maintenance records, how blood was drawn and stored, and the chain of custody.</li>
<li><strong>Rising BAC.</strong> Alcohol still absorbing at the time of the stop can make a later test read higher than your level while driving.</li>
<li><strong>Medical explanations.</strong> Acid reflux, diabetes, certain diets, fatigue and illness can cause false readings or look like impairment.</li>
</ul>

<h2>Drivers under 21</h2>
<p>A first DUI for a minor is a Class C misdemeanor, with a fine up to $500, community service, a license suspension and alcohol awareness classes. A minor with one DUI who completes all conditions may be able to have it expunged after turning 21. A second conviction ends that option.</p>

<h2>Results</h2>
<p>We have had DWIs dismissed for clients who tested at about twice the limit, at nearly three times the limit after a blood warrant, and after a crash with a city bus. See more on our <a href="results.html">results page</a>.</p>
"""
interior("dwi.html", "Houston DWI Lawyer | Walter J. Pink & Associates",
         "Houston DWI and DUI defense. Dismissals at 2x and 3x the limit. 15-day ALR deadline. Free consultation: (713) 664-6651.",
         "Houston DWI &amp; DUI defense", "A DWI arrest puts your license, your record and possibly your freedom at stake. You have 15 days to protect your license.", dwi)

# ---------------------------------------------------------------- DRUGS
drugs = f"""
<h2>Drug charges we defend</h2>
<p>We defend cases involving marijuana, cocaine, heroin, methamphetamine, fentanyl, MDMA, LSD, prescription opioids and Xanax. How serious the charge is depends on the substance, its penalty group, the weight and the circumstances of the arrest.</p>
<ul>
<li><strong>Possession.</strong> The State must prove you knew about the drugs and controlled them. Drugs found in a shared car or home are often contested.</li>
<li><strong>Possession with intent to deliver.</strong> Prosecutors try to infer intent from quantity, packaging, scales or cash. Personal use is a common defense.</li>
<li><strong>Delivery.</strong> Selling, transferring, transporting or offering to sell.</li>
<li><strong>Manufacturing.</strong> Often built on chemicals, equipment, residue testing and surveillance.</li>
<li><strong>Paraphernalia.</strong> Frequently added onto other charges.</li>
<li><strong>Trafficking.</strong> Large-scale cases may be prosecuted in state or <a href="federal-crimes.html">federal court</a>.</li>
</ul>

<h2>Possible penalties</h2>
{table(["Level", "Range"], [
    ["Misdemeanor (e.g., small amounts of marijuana)", "Fine and up to 1 year in county jail"],
    ["State jail felony (e.g., under 1 gram, Penalty Group 1)", "180 days to 2 years in state jail"],
    ["Second- and third-degree felonies", "2 to 20 years in prison"],
    ["First-degree and enhanced felonies", "5 to 99 years or life"],
])}
<p>Prior convictions, drug-free zones and weapons can raise the level. Ask us how the specific weight and penalty group affect your case.</p>

<h2>How drug cases are defended</h2>
<ul>
<li><strong>Illegal search and seizure.</strong> Warrantless searches, bad warrants and unlawful traffic stops can lead to evidence being thrown out.</li>
<li><strong>Knowledge and control.</strong> Being near drugs is not the same as possessing them.</li>
<li><strong>Lab testing.</strong> We review testing methods, contamination and chain of custody.</li>
<li><strong>Statements.</strong> Statements taken in violation of your right to silence or counsel can be excluded.</li>
</ul>

<h2>Alternatives to conviction</h2>
<p>Depending on your history and the charge, options may include drug court, treatment programs, pretrial diversion, deferred adjudication or community supervision. Many of these can protect your record.</p>
"""
interior("drug-charges.html", "Houston Drug Charge Lawyer | Walter J. Pink & Associates",
         "Defense for drug possession, intent to deliver, manufacturing and trafficking in Houston. Free consultation.",
         "Houston drug charge defense", "Possession through trafficking, state and federal. Most drug cases turn on the search, and that's where we start.", drugs)

# ---------------------------------------------------------------- FAMILY VIOLENCE
dv = f"""
<h2>What Texas calls family violence</h2>
<p>Texas law uses the term &ldquo;family violence.&rdquo; It covers people related by blood or marriage, members of the same household, and people who are or were in a dating relationship, even if they never lived together.</p>

<h2>Charges and penalties</h2>
{table(["Charge", "Level", "Range"], [
    ["Assault causing bodily injury (family)", "Class A misdemeanor", "Up to 1 year in jail, fine up to $4,000"],
    ["Assault family violence with a prior", "Third-degree felony", "2 to 10 years in prison"],
    ["Assault by impeding breath or circulation", "Third-degree felony", "2 to 10 years, even with no visible injury"],
    ["Impeding breath with a prior family violence conviction", "Second-degree felony", "2 to 20 years in prison"],
    ["Continuous violence against the family (2+ in 12 months)", "Third-degree felony", "2 to 10 years in prison"],
])}

<h2>What happens right after the arrest</h2>
<p>Family violence cases move fast. A judge, not a standard bail schedule, sets bond. An emergency protective order is often issued at the first appearance and can keep you out of your own home and away from your children for 31 to 91 days. Violating it, even accidentally, is a separate crime. Getting a lawyer involved before that hearing can shape the conditions you live under for months.</p>

<h2>What you should do now</h2>
<ul>
<li>Have no contact with the complainant, directly or through others.</li>
<li>Write down your account while it's fresh.</li>
<li>Save texts, voicemails, photos and anything else that shows what really happened.</li>
<li>Stay off social media.</li>
<li>Talk about the case only with your lawyer. Other conversations are not privileged.</li>
</ul>

<h2>Defenses</h2>
<ul>
<li><strong>Self-defense.</strong> Texas law allows force to protect yourself. Several of our dismissals involved clients who were the ones attacked.</li>
<li><strong>False or exaggerated allegations.</strong> Many cases rest almost entirely on one person's word. We test it against the evidence.</li>
<li><strong>Non-cooperation.</strong> A complainant can't drop the case, but their position matters, and we know how to present it.</li>
<li><strong>Investigation errors.</strong> Unlawful arrests and improper procedures can lead to suppressed evidence.</li>
<li><strong>Enhancements.</strong> We challenge prior convictions used to raise a misdemeanor to a felony.</li>
</ul>

<h2>The long-term stakes</h2>
<p>Federal law permanently bars anyone convicted of misdemeanor domestic violence from owning a firearm. A conviction can also affect custody, housing, employment, professional licenses and immigration status.</p>
"""
interior("domestic-violence.html", "Houston Domestic Violence Lawyer | Walter J. Pink & Associates",
         "Defense for assault family violence, impeding breath and protective orders in Houston. Free consultation.",
         "Houston domestic &amp; family violence defense", "One accusation can cost you your home, your children and your gun rights before you ever see a jury. We move fast.", dv)

# ---------------------------------------------------------------- HOMICIDE
homicide = f"""
<h2>Homicide offenses in Texas</h2>
{table(["Offense", "Level", "Range"], [
    ["Capital murder", "Capital felony", "Life without parole or death"],
    ["Murder (including felony murder)", "First-degree felony", "5 to 99 years or life, fine up to $10,000"],
    ["Manslaughter (reckless)", "Second-degree felony", "2 to 20 years, fine up to $10,000"],
    ["Intoxication manslaughter", "Second-degree felony", "2 to 20 years, possible restitution"],
    ["Criminally negligent homicide", "State jail felony", "180 days to 2 years in state jail"],
])}
<p><strong>Capital murder</strong> includes killing a police officer or firefighter, murder for hire, multiple victims, a child under 15, and murder during certain felonies such as robbery or kidnapping. <strong>Murder</strong> can apply even without intent to kill, if the person intended serious bodily injury. <strong>Felony murder</strong> can apply to anyone involved in a felony where a death occurs.</p>

<h2>Before charges are filed</h2>
<p>Some of our strongest results came before an indictment. When a client acted in self-defense, we can prepare them, speak with detectives and present a grand jury packet. In two recent murder investigations, that work led grand juries to return a no-bill, and no charges were filed.</p>

<h2>How we defend homicide cases</h2>
<ul>
<li><strong>Self-defense and defense of others.</strong> Texas law protects people who use deadly force when it's reasonably necessary.</li>
<li><strong>Mistaken identity.</strong> We scrutinize eyewitness identifications, video and phone location data.</li>
<li><strong>Intent.</strong> The difference between murder and manslaughter can be decades in prison.</li>
<li><strong>The evidence.</strong> We challenge forensic findings, statements and anything obtained unlawfully, and we retain our own experts.</li>
<li><strong>Persistence.</strong> One of our capital murder cases stayed open for years. We kept filing and challenging until the State dismissed it near trial.</li>
</ul>
<div class="callout"><p>If police want to talk to you about a death, don't go in without a lawyer, even as a &ldquo;witness.&rdquo; Call us first.</p></div>
"""
interior("murder-homicide.html", "Houston Murder Defense Lawyer | Walter J. Pink & Associates",
         "Defense for capital murder, murder, manslaughter and self-defense cases in Houston. Free consultation.",
         "Houston murder &amp; homicide defense", "Capital murder dismissed. Murder investigations no-billed. When the stakes are this high, experience at trial matters.", homicide)

# ---------------------------------------------------------------- WEAPONS
weapons = f"""
<h2>Gun rights come with rules</h2>
<p>Texas allows most adults to carry a handgun without a license, but there are still places you can't carry and people who can't possess a firearm at all. Weapons charges are often added on top of another charge. &ldquo;Weapon&rdquo; can also mean knives, clubs and explosive or chemical devices, not just guns.</p>

<h2>Common weapons charges</h2>
{table(["Charge", "Level", "Range"], [
    ["Unlawful carrying of a weapon (e.g., while intoxicated or committing another crime)", "Class A misdemeanor", "Up to 1 year in jail, fine up to $4,000"],
    ["Carrying in a prohibited place (schools, courts, polling places, bars, etc.)", "Class A misdemeanor to third-degree felony", "Up to 10 years depending on location"],
    ["Unlawful possession of a firearm by a felon", "Third-degree felony", "2 to 10 years in prison, fine up to $10,000"],
    ["Possession of a prohibited weapon", "Third-degree felony (most items)", "2 to 10 years in prison"],
])}

<h2>Felons and firearms</h2>
<p>Under Texas law, a person with a felony conviction may not possess a firearm until five years after release from prison or supervision, whichever is later, and after that only at their home. Federal law is stricter and generally bars felons from possessing firearms anywhere. We regularly defend both state and <a href="federal-crimes.html">federal</a> felon-in-possession cases.</p>

<h2>How we defend weapons charges</h2>
<ul>
<li><strong>Lawful possession.</strong> Many people charged were legally entitled to carry where they were.</li>
<li><strong>Knowledge.</strong> A gun in a shared car or apartment isn't automatically yours.</li>
<li><strong>The search.</strong> Firearms found through an unlawful stop or search can be suppressed.</li>
</ul>
<p>We've obtained dismissals in Harris, Fort Bend, Brazoria, Galveston, Montgomery, Dallas and Travis counties.</p>
"""
interior("weapons.html", "Houston Weapons Charge Lawyer | Walter J. Pink & Associates",
         "Defense for unlawful carrying, felon in possession and prohibited weapons charges in Houston.",
         "Houston weapons charge defense", "Unlawful carrying, felon in possession and prohibited weapons, in state and federal court.", weapons)

# ---------------------------------------------------------------- FEDERAL
federal = f"""
<h2>When a case becomes federal</h2>
<p>Federal charges come from conduct that crosses state lines, involves a federal agency or federal money, happens on federal property, or violates a federal statute. Houston cases are prosecuted in the U.S. District Court for the Southern District of Texas at the Bob Casey Courthouse, one of the busiest federal trial courts in the country.</p>

<h2>Federal cases we handle</h2>
<ul>
<li>Drug trafficking and distribution, including multi-agency and cartel-linked investigations</li>
<li>Federal firearms offenses, often charged alongside drug cases</li>
<li>Wire fraud, mail fraud, money laundering and embezzlement</li>
<li>Illegal reentry and human smuggling</li>
<li>Identity theft, computer fraud and other cybercrimes</li>
</ul>
<p>Investigating agencies include the FBI, DEA, ATF, IRS Criminal Investigation and Homeland Security Investigations.</p>

<h2>Call before you're indicted</h2>
<p>Federal agents often build a case for months using wiretaps, informants, financial records and surveillance before anyone is arrested. If you've received a target letter, been contacted by an agent or had a search warrant executed, that is the time to hire counsel.</p>

<h2>The federal process</h2>
<ol class="timeline">
<li><h3>Investigation</h3><p>Agents gather evidence, often for months or years.</p></li>
<li><h3>Grand jury</h3><p>A panel of 16 to 23 citizens decides whether to indict. The defense is not in the room.</p></li>
<li><h3>Arraignment and detention hearing</h3><p>The government may ask to hold you until trial. Protecting your release is an early priority.</p></li>
<li><h3>Discovery and motions</h3><p>We review the government's evidence and move to suppress anything obtained unlawfully.</p></li>
<li><h3>Plea or trial</h3><p>Most federal cases end in a plea agreement. The terms of that agreement, and the sentencing guideline calculation, are where good defense work pays off.</p></li>
</ol>

<h2>Federal sentencing</h2>
<p>There is no parole in the federal system, so defendants serve at least 85 percent of the sentence imposed. Many drug and firearm offenses carry mandatory minimums, and federal gun sentences often run consecutively. A defense lawyer can challenge the guideline calculation, pursue reductions and, in the right case, negotiate cooperation that allows a sentence below the mandatory minimum. One client facing nine years left with five.</p>

<h2>Common questions</h2>
<p><strong>Can I be charged federally after my state case was dismissed?</strong> Yes. The state and federal governments are separate sovereigns, so double jeopardy doesn't prevent it.</p>
<p><strong>Can the government take my property before I'm convicted?</strong> It can try, through civil asset forfeiture, which runs separately from the criminal case and should be fought separately.</p>
"""
interior("federal-crimes.html", "Houston Federal Criminal Defense Lawyer | Walter J. Pink & Associates",
         "Federal criminal defense in the Southern District of Texas: drugs, firearms, fraud and cybercrime.",
         "Houston federal criminal defense", "Federal prosecutors win most of their cases before trial. Your defense should start before the indictment.", federal)

# ---------------------------------------------------------------- THEFT
theft = f"""
<h2>What counts as theft</h2>
<p>Under Texas Penal Code &sect; 31.03, theft means taking property without the owner's effective consent, intending to deprive them of it. That includes shoplifting, theft of services, embezzlement, receiving stolen property and borrowing something you never meant to return. If force or threats are involved, the charge becomes <a href="robbery.html">robbery</a>.</p>

<h2>Theft is graded by value</h2>
{table(["Value of property", "Level", "Range"], [
    ["Under $100", "Class C misdemeanor", "Fine up to $500"],
    ["$100 to under $750", "Class B misdemeanor", "Up to 180 days in jail, fine up to $2,000"],
    ["$750 to under $2,500", "Class A misdemeanor", "Up to 1 year in jail, fine up to $4,000"],
    ["$2,500 to under $30,000", "State jail felony", "180 days to 2 years, fine up to $10,000"],
    ["$30,000 to under $150,000", "Third-degree felony", "2 to 10 years, fine up to $10,000"],
    ["$150,000 to under $300,000", "Second-degree felony", "2 to 20 years, fine up to $10,000"],
    ["$300,000 or more", "First-degree felony", "5 to 99 years or life, fine up to $10,000"],
])}
<p>Prior theft convictions and certain victims, like the elderly, can raise the level.</p>

<h2>Defenses</h2>
<ul>
<li>No intent to deprive the owner</li>
<li>Consent, ownership or a good-faith claim to the property</li>
<li>Mistaken identity and unclear surveillance video</li>
<li>Challenging the claimed value, which can drop a felony to a misdemeanor</li>
<li>Abandoned property, alibi or insufficient evidence</li>
</ul>
<p>For a first offense, pretrial diversion or deferred adjudication may keep a theft off your record, which matters because a theft conviction is treated as a crime of dishonesty by employers.</p>
"""
interior("theft.html", "Houston Theft Lawyer | Walter J. Pink & Associates",
         "Houston theft defense: shoplifting, embezzlement, theft of services and stolen property.",
         "Houston theft defense", "A theft conviction follows you to every job application. Many theft cases can be reduced, diverted or dismissed.", theft)

# ---------------------------------------------------------------- ROBBERY
robbery = f"""
<h2>Robbery under Texas law</h2>
<p>Robbery is theft plus force or threat. Under Texas Penal Code &sect; 29.02, a person commits robbery if, while committing theft, they cause bodily injury or threaten or place someone in fear of imminent injury or death. The force doesn't have to be serious, and it can happen before, during or right after the taking, including while running away.</p>

<h2>Robbery and aggravated robbery</h2>
{table(["Charge", "Level", "Range"], [
    ["Robbery", "Second-degree felony", "2 to 20 years in prison, fine up to $10,000"],
    ["Aggravated robbery", "First-degree felony", "5 to 99 years or life, fine up to $10,000"],
])}
<p>Robbery becomes <strong>aggravated</strong> when it involves serious bodily injury, using or showing a deadly weapon, or injuring or threatening someone 65 or older or disabled. A &ldquo;deadly weapon&rdquo; can be almost anything, depending on how it was used. Restitution may also be ordered.</p>

<h2>Defenses</h2>
<ul>
<li>Mistaken identity, a common problem with stranger eyewitness identifications</li>
<li>Alibi</li>
<li>No theft occurred, or there was a right or permission to take the property</li>
<li>No force or threat, which reduces robbery to theft</li>
<li>No deadly weapon, which reduces aggravated robbery to robbery</li>
<li>Lack of probable cause and civil rights violations</li>
</ul>
<p>We recently won a jury acquittal for a client charged with aggravated robbery.</p>
"""
interior("robbery.html", "Houston Robbery Defense Lawyer | Walter J. Pink & Associates",
         "Defense for robbery and aggravated robbery charges in Houston. Free consultation.",
         "Houston robbery defense", "Robbery and aggravated robbery carry years to life in prison. We've won acquittals at trial.", robbery)

# ---------------------------------------------------------------- BURGLARY
burglary = f"""
<h2>What the State has to prove</h2>
<p>Under Texas Penal Code &sect; 30.02, burglary means entering a home, or a building not open to the public, without the owner's consent and with intent to commit a felony, theft or assault. It also covers hiding inside with that intent, or entering and then committing or attempting one of those crimes. Nothing has to be taken; the offense is complete on entry.</p>

<h2>Types of burglary and penalties</h2>
{table(["Charge", "Level", "Range"], [
    ["Burglary of a vehicle", "Class A misdemeanor", "Up to 1 year in jail; minimum 6 months with a prior"],
    ["Burglary of a building", "State jail felony", "180 days to 2 years, fine up to $10,000"],
    ["Burglary of a habitation", "Second-degree felony", "2 to 20 years, fine up to $10,000"],
    ["Burglary of a habitation intending a felony other than theft", "First-degree felony", "5 to 99 years or life"],
    ["Criminal trespass", "Class B or Class A misdemeanor", "Up to 180 days or up to 1 year"],
])}
<p>A habitation includes houses, apartments, hotel rooms and anything used for sleeping overnight, like an RV. Breaking into a pharmacy or a building storing controlled substances raises a building burglary to a felony with up to 10 years.</p>

<h2>Defenses</h2>
<ul>
<li>Consent to be there, including a right to enter a shared home</li>
<li>No intent to commit a crime inside, which may reduce the charge to criminal trespass</li>
<li>Mistaken identity and weak forensic evidence</li>
<li>Duress or necessity</li>
</ul>
<div class="callout"><p>In one of our cases, a client was locked out of his own home and then accused of breaking in to attack the complainant. Both the burglary and assault charges were dismissed.</p></div>
"""
interior("burglary.html", "Houston Burglary Defense Lawyer | Walter J. Pink & Associates",
         "Defense for burglary of a habitation, building and vehicle in Houston. Free consultation.",
         "Houston burglary defense", "Burglary of a home is a felony carrying up to 20 years, even if nothing was taken.", burglary)

# ---------------------------------------------------------------- EXPUNCTION
exp = f"""
<h2>Two ways to clear a record</h2>
<p><strong>Expunction</strong> destroys the records of an arrest. It's generally available when a case was dismissed, you were acquitted, or charges were never filed, and for some Class C offenses after deferred disposition.</p>
<p><strong>An order of nondisclosure</strong> seals a record from most public view, including most employers and landlords. It's often available after you successfully complete deferred adjudication, and for some first-time misdemeanors.</p>

<h2>Why it matters even without a conviction</h2>
<p>An arrest that was dismissed can still show up on background checks for jobs, apartments and professional licenses. Clearing it lets you legally deny the arrest in most situations.</p>

<h2>Waiting periods and eligibility</h2>
<p>Eligibility depends on the offense, the outcome and your history, and some cases have waiting periods. Bring us your case information and we'll tell you whether you qualify and when.</p>
"""
interior("expunction.html", "Houston Expunction & Record Sealing Lawyer | Walter J. Pink & Associates",
         "Expunctions and orders of nondisclosure in Houston to clear arrests and dismissed cases from your record.",
         "Expunction &amp; record sealing", "A dismissed case can still cost you a job. We can often clear it.", exp)

# ---------------------------------------------------------------- FAQ
faq_items = [
    ("Do I really need a lawyer for a criminal case?", "Yes. Your freedom and record are at stake. Get counsel before an indictment if you can, and never talk to law enforcement without one."),
    ("If I did it, do I still need a lawyer?", "Yes. A lawyer can find legal problems with the stop, search or evidence, challenge what the State can prove, and negotiate a far better outcome than you'd get alone."),
    ("What is an indictment?", "The formal charging document in a felony case, returned by a grand jury that found probable cause. In misdemeanor cases, the charging document is called an information."),
    ("Police never read me my rights. Is my case dismissed?", "Not automatically. Miranda warnings are required before custodial interrogation. Statements taken without them may be suppressed, but volunteered statements can still be used, and the rest of the case continues."),
    ("When can police search me, my home or my car?", "With a warrant, within its scope; incident to a lawful arrest, covering you and the area within your reach; with consent; and in other limited situations. Items in plain view may be seized. A legally towed car can be inventoried, but police can't impound a car just to search it."),
    ("How long will my case take?", "There's no set timeline. Cases take from a few months to a few years, depending on lab results, witnesses, plea negotiations and co-defendants."),
    ("Will my case go to trial?", "Probably not. More than 90 percent of state cases end without a trial, through dismissal, reduction or plea. Being ready to try the case is what produces good results without one."),
    ("Can I get a charge off my record?", "Often. Dismissals, acquittals and completed deferred adjudication may qualify for expunction or nondisclosure. See our <a href=\"expunction.html\">record sealing page</a>."),
    ("I'm innocent. Can I just explain things to the police?", "Please don't. Innocent people's statements get taken out of context, and nerves cause mistakes. Talk to a lawyer first."),
    ("What's the difference between a misdemeanor and a felony?", "Misdemeanors carry up to a year in county jail. Felonies carry state jail or prison time, up to life or death for capital felonies. See the full ranges on our <a href=\"criminal-defense.html\">criminal defense page</a>."),
    ("What's the difference between state and federal crimes?", "Federal cases usually involve interstate activity, federal property, federal agencies or federal funds. They follow different rules and sentencing. See <a href=\"federal-crimes.html\">federal crimes</a>."),
    ("I just found out I have a warrant. What do I do?", "Call a lawyer before you do anything else. We can advise on bond options and, in some cases, arrange to have the warrant handled without you sitting in jail."),
]
faqpage = f"""
<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / FAQ</div><h1>Criminal law FAQ</h1><p>Straight answers to the questions we hear most. For advice about your case, call us.</p></div></section>
<section class="section"><div class="wrap">{faq_block(faq_items)}</div></section>
"""
write("faq.html", "Criminal Law FAQ | Walter J. Pink & Associates, P.C.",
      "Answers to common Texas criminal law questions: searches, Miranda, warrants, expunction and more.", faqpage)

# ---------------------------------------------------------------- CONTACT
contact = f"""
<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Contact</div><h1>Contact us</h1><p>Call or text {PHONE} any time, or send the form and an attorney will contact you.</p></div></section>
<section class="section"><div class="wrap contact-grid">
<form class="consult" action="{FORM_ACTION}" method="POST">
<div class="row2"><div class="field"><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div>
<div class="field"><label for="p">Phone</label><input id="p" name="phone" type="tel" autocomplete="tel" required></div></div>
<div class="field"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email"></div>
<div class="field"><label for="co">County</label><input id="co" name="county" placeholder="Harris, Fort Bend, etc."></div>
<div class="field"><label for="m">Brief description</label><textarea id="m" name="message"></textarea></div>
<button class="btn btn-primary" type="submit">Send my request</button>
<p class="form-note">Sending this form does not create an attorney-client relationship. Please don't include confidential details.</p>
</form>
<div class="office" style="background:var(--navy);padding:36px">
<h3>Office</h3><p>{ADDR1}<br>{ADDR2}</p>
<a class="big" href="tel:{TEL}">{PHONE}</a>
<p>Office visits by appointment.</p>
<iframe class="map-frame" title="Map to our office" loading="lazy" src="https://www.google.com/maps?q=1717+St.+James+Place+Suite+690+Houston+TX+77056&output=embed"></iframe>
</div>
</div></section>
"""
write("contact.html", "Contact | Walter J. Pink & Associates, P.C.",
      "Contact Walter J. Pink & Associates, 1717 St. James Place, Suite 690, Houston. (713) 664-6651.", contact)

# ---------------------------------------------------------------- DISCLAIMER
disc = f"""
<h2>Attorney advertising</h2>
<p>This website is attorney advertising by {FIRM}. It provides general information about Texas law and is not legal advice. Reading this site or contacting us does not create an attorney-client relationship.</p>
<p>Case results and client reviews describe specific matters. {RESULTS_DISCLAIMER}</p>
<p>Unless otherwise stated, the attorneys of this firm are not certified by the Texas Board of Legal Specialization.</p>
<p>Principal office: {ADDR1}, {ADDR2}.</p>
<h2 id="privacy">Privacy</h2>
<p>If you send us information through this site, we use it only to respond to your inquiry. We don't sell your information. Please don't send confidential details through the website form.</p>
"""
interior("disclaimer.html", "Disclaimer | Walter J. Pink & Associates, P.C.", "Legal disclaimer and privacy notice.",
         "Disclaimer &amp; privacy", "Please read before relying on anything on this site.", disc, crumb="Disclaimer", nav=ABOUT)

# ---------------------------------------------------------------- 404, favicon, sitemap
write("404.html", "Page not found | Walter J. Pink & Associates", "Page not found.",
      f'<section class="page-hero"><div class="wrap"><h1>That page doesn&rsquo;t exist</h1><p>Go to the <a href="index.html" style="color:#B8892B">home page</a> or call {PHONE}.</p></div></section>')

with open(os.path.join(OUT, "img", "favicon.svg"), "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="#14213D"/><rect x="3" y="3" width="42" height="42" fill="none" stroke="#B8892B" stroke-width="3"/><text x="24" y="31" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="16" fill="#fff">WJP</text></svg>')

pages = sorted(p for p in os.listdir(OUT) if p.endswith(".html") and p != "404.html")
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in pages:
        f.write(f"  <url><loc>{SITE_URL}/{'' if p == 'index.html' else p}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("built", len(pages) + 1, "pages")
