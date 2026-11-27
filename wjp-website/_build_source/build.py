#!/usr/bin/env python3
"""Builds the static site for Pink Esquire into .."""
import os, json

OUT = os.path.join(os.path.dirname(__file__), "..")
FIRM = "Pink Esquire"
PHONE = "(832) 979-0228"
TEL = "+18329790228"
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
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&family=Zilla+Slab:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">{json.dumps({
  "@context": "https://schema.org", "@type": "LegalService",
  "name": "Pink Esquire", "telephone": "+1-832-979-0228",
  "url": SITE_URL,
  "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Houston", "addressRegion": "TX", "postalCode": "77056", "addressCountry": "US"},
  "areaServed": ["Harris County", "Fort Bend County", "Houston"]
})}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def dropdown(label, items, current):
    lis = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in items)
    return f'<li class="has-sub"><button class="navlink" aria-expanded="false">{label}</button><ul class="sub">{lis}</ul></li>'


def header(current):
    return f"""<div class="topbar"><div class="wrap"><span>Affiliate of Walter J. Pink &amp; Pink Esquire Enterprises &nbsp;|&nbsp; Free, confidential consultations. Call or text any time.</span><a href="tel:{TEL}">{PHONE}</a></div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">{MARK}<span class="brand-text"><strong>Pink Esquire</strong><small>&nbsp;|&nbsp; Houston criminal defense</small></span></a>
<button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="nav" id="site-nav" aria-label="Main">
<ul>
{dropdown("Criminal defense", CRIMINAL, current)}
{dropdown("Attorneys", ABOUT, current)}
<li><a class="navlink" href="results.html"{" aria-current=\"page\"" if current == "results.html" else ""}>Case results</a></li>
<li><a class="navlink" href="about.html"{" aria-current=\"page\"" if current == "about.html" else ""}>About us</a></li>
<li><a class="navlink" href="faq.html"{" aria-current=\"page\"" if current == "faq.html" else ""}>FAQ</a></li>
<li><a class="navlink" href="contact.html"{" aria-current=\"page\"" if current == "contact.html" else ""}>Contact</a></li>
</ul>
<a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a>
</nav>
</div></header>
"""


def hero(eyebrow, h1, lead, actions, card):
    act_html = "".join(actions)
    card_html = f'<div class="hero-card">{card}</div>' if card else ""
    return f"""<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">{eyebrow}</span>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
<div class="actions">{act_html}</div>
</div>
{card_html}
</div></section>"""


def cta_band(title, text):
    return f"""<section class="callout-band"><div class="wrap text-center">
<h2>{title}</h2>
<p>{text}</p>
<a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a>
</div></section>"""


def footer():
    return f"""<footer class="site-footer"><div class="wrap footer-grid">
<div>
<a class="brand" href="index.html"><span class="brand-text"><strong>Pink Esquire</strong></span></a>
<p>Dedicated criminal defense across Houston and all of Texas.</p>
<p>&copy; Pink Esquire. All rights reserved.</p>
</div>
<div>
<h4>Contact</h4>
<p>{ADDR1}<br>{ADDR2}</p>
<p>Phone: <a href="tel:{TEL}" style="font-weight:700;font-size:1.15rem">{PHONE}</a></p>
</div>
<div>
<h4>Practice Areas</h4>
<ul>
<li><a href="dwi.html">DWI / DUI</a></li>
<li><a href="drug-charges.html">Drug Charges</a></li>
<li><a href="domestic-violence.html">Domestic Violence</a></li>
<li><a href="federal-crimes.html">Federal Crimes</a></li>
<li><a href="expunction.html">Expunctions</a></li>
</ul>
</div>
</div></footer>
<script src="js/main.js"></script>
</body>
</html>"""
