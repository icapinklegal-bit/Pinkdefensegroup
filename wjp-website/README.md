# Walter J. Pink & Associates, P.C. — website

A static site (plain HTML/CSS/JS) built to host on GitHub Pages.

## Put it live

1. Create a new **public** repository on GitHub (for example `firm-website`).
2. Upload everything in this folder: on the repo page, click **Add file → Upload files**, drag in all the files and folders, then click **Commit changes**.
3. Go to **Settings → Pages → Source: Deploy from a branch → main / (root) → Save**.
4. After 1–5 minutes, the site is live at `https://YOURUSERNAME.github.io/firm-website/`.

## Before you launch

- **Contact form:** create a free form at formspree.io and replace `YOUR_FORM_ID` in `index.html` and `contact.html`, or change `FORM_ACTION` in the build script.
- **Photos:** add attorney headshots to `img/` (`augustin-t-pink.jpg`, `ishmael-g-a-pink.jpg`, `clement-b-pink.jpg`), then uncomment the `<img>` tag in each portrait block.
- **Reviews:** the three review cards on the homepage are summaries. Replace them with each client's exact words.
- **Bios:** add law school, bar admission year and memberships where the `<!-- Add: ... -->` comments are.

## Custom domain

Under **Settings → Pages → Custom domain**, enter your domain. At your registrar, add these records:

- `CNAME`: `www` → `YOURUSERNAME.github.io`
- `A`: `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`

When DNS finishes updating, check **Enforce HTTPS**.
