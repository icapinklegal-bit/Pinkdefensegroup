# PinkDefense website

A static site with 275 pages, ready for GitHub and Vercel. There's no build step on Vercel: the HTML files at the root of this repo are the live site.

## Deploying (GitHub → Vercel)
1. In your GitHub repository, **delete the old HTTrack mirror files**: `Pink Defense/`, `hts-cache/`, `hts-log.txt`, `cookies.txt`, `backblue.gif`, `fade.gif`, and the old `index.html`.
2. Upload the full contents of this folder to the root of the repo, including `vercel.json`, `.vercelignore`, `robots.txt`, `sitemap.xml`, `llms.txt` and `llms-full.txt`. Then commit.
3. In Vercel, open Project → Settings → Build & Deployment and set:
   - **Framework Preset:** Other
   - **Build Command:** leave empty / override to blank
   - **Output Directory:** `.` (repository root)
4. Vercel redeploys on every push. Once your domain is connected, submit `https://YOUR-DOMAIN/sitemap.xml` to Google Search Console and Bing Webmaster Tools.

## Launch checklist
- [ ] **Activate the contact form.** Forms are delivered to Ishmael@PinkEsquire.com through FormSubmit. The first time the live form is submitted, FormSubmit emails an activation link to that inbox. Click it, and every submission after that arrives as an email.
- [ ] **Domain.** Canonical URLs, the sitemap and the schema all use `https://www.pinkdefense.com`. If your domain is different, rebuild with the correct one (see below).
- [ ] **Headshots.** Put the photos in `assets/img/team/` (filenames are listed in the README there). Until you do, Augustin's and Clement's photos load from walterjpink.com, and everyone else shows a monogram.
- [ ] **Analytics / GTM.** Send your snippet to be added, or set it in `_build/gen.py` (`ANALYTICS`) and rebuild.
- [ ] **Verify the of-counsel bios** with Ikenna Okoro and Femi Aborisade before launch. They were written from public sources.

## What's in it
- Every page has: the "Affiliate of Walter J. Pink & Pink Law Enterprises" banner; Houston and Fort Bend geo meta tags (`geo.region`, `geo.placename`, `geo.position`, `ICBM`); a canonical URL; Open Graph and Twitter tags; and JSON-LD schema (LegalService + LocalBusiness, WebPage, BreadcrumbList, plus Service, FAQPage or Person where they apply).
- AI and search discovery: `llms.txt`, `llms-full.txt`, a `robots.txt` that explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended and others, and `sitemap.xml`.
- `vercel.json` handles clean URLs and security headers, and redirects old WordPress, Kevin Bennett and walterjpink.com-style paths to the new pages.

## Editing / rebuilding
The source lives in `_build/`, which is excluded from deployment by `.vercelignore`. Page text is in `_build/content/*.py`.

```
cd _build
SITE_URL=https://www.yourdomain.com python3 gen.py ..
```
