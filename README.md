# Tandoori Nights — website

Static site. No framework, no database. Five pages, one stylesheet, real images, structured data, sitemap, robots, llms.txt.
Ordering links to Toast. The catering form posts to Netlify Forms (or swap in Formspree, see below).

## What's in here

    build.py          builds the site from content.py + css + images  ->  dist/
    content.py        EVERY word, price, link and fact on the site. Edit this, not the HTML.
    css/site.css      the one stylesheet (responsive, phone to desktop)
    images/           named, sized JPG + WebP (900px and 1800px) for every photo
    catering-menu.pdf your printed catering menu, served at /catering-menu.pdf
    dist/             the built site. This is what gets uploaded. Never edit it by hand.
    netlify.toml      tells Netlify how to build
    package.json      npm scripts wrapping the commands below

Pages: `/`  `/menu/`  `/lunch-buffet/`  `/catering/` (incl. #trays and #private-events)  `/hours-directions/`  `/thanks/`  `404.html`

## Requirements

- Python 3.8 or newer (Mac: already installed; `python3 --version` to check)
- Node 18+ only if you want the one-line deploy commands (`node --version`)

## 1. Preview on your machine

Quickest: double-click `dist/index.html`. All links are relative, so the whole site works straight from the folder.

Or serve it (closer to how it behaves online):

    cd tandoori-nights-site
    npm run dev          # or: python3 build.py && python3 -m http.server 8080 --directory dist

Open http://localhost:8080. On Windows, use `python` instead of `python3` if `python3` isn't found.

## 2. Fill in the facts

Open `content.py`. Search for `[` — every bracketed item is a fact to confirm (buffet price, room capacity, delivery radius,
year opened, DoorDash and Instagram links, lat/long). Replace and save. Run `npm run build` again.

Prices, hours, FAQ answers, dish descriptions: all in `content.py` too. The tray tables are the lists `ENTREES`, `RICE`, `PIECES`, `TRAYS`.

## 3. Deploy (pick one)

### Netlify (recommended: free, form handling built in)

    npm i -g netlify-cli
    netlify login
    npm run build
    netlify deploy --prod --dir=dist        # first run: "Create & configure a new site"

The catering form works immediately: submissions show up under Site > Forms, and you can add an email notification there.
Or connect the repo in the Netlify dashboard and every push rebuilds automatically (netlify.toml is already set).

### Cloudflare Pages (free, fast)

    npm i -g wrangler
    wrangler login
    npm run build
    wrangler pages deploy dist --project-name tandoori-nights

Cloudflare has no built-in forms. Sign up at formspree.io (free), get your form endpoint, and in `build.py` change the
form tag to `action="https://formspree.io/f/YOUR_ID" method="POST"` and delete the `data-netlify` and `netlify-honeypot` attributes.

### Anything else (cPanel, S3, GitHub Pages)

Upload the contents of `dist/` to the web root. `_headers` and `_redirects` are Netlify/Cloudflare-specific and can be ignored elsewhere.

## 4. Point the domain

In Squarespace: Settings > Domains > tandoorinightsmd.com > DNS settings.
- Netlify: add the site's custom domain in Netlify, then set the DNS records Netlify shows you (an A record and a CNAME for www).
- Cloudflare Pages: same idea under Custom domains.
Keep the domain registered at Squarespace; cancel only the *website* plan once the new site is live. SSL is automatic on both hosts.

`_redirects` already maps the old Squarespace URLs (`/catering-private-events`, `/contact`, `/welcome`) to the new pages so nothing 404s.

## 5. After launch (this is where the ranking comes from)

1. Google Search Console: add the property, submit `https://www.tandoorinightsmd.com/sitemap.xml`.
2. Bing Webmaster Tools: same. Bing feeds ChatGPT search.
3. Google Business Profile: set the website to the new URL, the Order link to Toast, the Menu link to `/menu/`, the Reservations link to OpenTable.
   Mark the Bethesda listing permanently closed if it still exists.
4. Claim the Tripadvisor listing; fix OpenTable's "private dining: not offered".
5. Test rich results: https://search.google.com/test/rich-results on `/`, `/menu/`, `/catering/`.

## Editing later

- Change text or prices: edit `content.py`, run `npm run build`, redeploy.
- Add a photo: drop a JPG in `images/` at 1800px wide as `name.jpg`, plus `name-900.jpg`, `name.webp`, `name-900.webp`
  (any image tool; or ask Claude to size them), then reference `name.jpg` in content.py / build.py.
- New page: copy one of the page blocks at the bottom of `build.py`.
