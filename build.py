#!/usr/bin/env python3
"""Build the Tandoori Nights static site.  python3 build.py  ->  ./dist
Edit content in content.py; templates live here. No dependencies beyond Python 3.8+."""
import json, os, re, shutil, datetime
from content import *

OUT = 'dist'
STROKE = '<svg class="stroke" viewBox="0 0 260 16" aria-hidden="true"><path d="M4 10c50-7 100-8 150-5 36 2 70 3 102 0" fill="none" stroke="#DB8E2E" stroke-width="6" stroke-linecap="round"/><path d="M12 12c60-4 120-6 200-3" fill="none" stroke="#DB8E2E" stroke-width="2.5" stroke-linecap="round" opacity=".7"/></svg>'

def pic(name, alt, cls='', w=None, h=None, eager=False, sizes='(max-width: 760px) 100vw, 50vw'):
    base = name.rsplit('.', 1)[0]
    lazy = '' if eager else ' loading="lazy" decoding="async"'
    dims = f' width="{w}" height="{h}"' if w and h else ''
    c = f' class="{cls}"' if cls else ''
    return (f'<picture><source type="image/webp" srcset="/images/{base}-900.webp 900w, /images/{base}.webp 1800w" sizes="{sizes}">'
            f'<img src="/images/{base}.jpg" srcset="/images/{base}-900.jpg 900w, /images/{base}.jpg 1800w" sizes="{sizes}" alt="{alt}"{c}{dims}{lazy}></picture>')

def nav(active):
    def l(t, href, key):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{href}"{cur}>{t}</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap nav" id="nav">
<a class="logo" href="/" aria-label="Tandoori Nights home"><img src="/images/logo.png" alt="Tandoori Nights" width="268" height="100"></a>
<div class="nav-links">{l('Home','/','home')}{l('Menu','/menu/','menu')}{l('Lunch Buffet','/lunch-buffet/','buffet')}{l('Catering &amp; Events','/catering/','catering')}{l('Hours &amp; Directions','/hours-directions/','visit')}</div>
<div class="nav-links nav-right"><a class="nav-phone" href="tel:{PHONE_E164}"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg><span>{PHONE}</span></a><a class="btn btn-outline" href="{OPENTABLE}" rel="noopener">Book a table</a><a class="btn btn-primary" href="{TOAST}" rel="noopener">Order online</a></div>
<button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o);this.setAttribute('aria-label',o?'Close menu':'Open menu')"><svg class="ico ico-menu" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg><svg class="ico ico-x" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
</div></header>
'''

FOOTER = f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div class="foot-col"><img src="/images/logo.png" alt="Tandoori Nights" width="268" height="100"><span>Indian restaurant &amp; catering<br>{ADDRESS_1}, {CITY}, {STATE} {ZIP}<br><a href="tel:{PHONE_E164}">{PHONE}</a></span></div>
<div class="foot-col"><span class="lbl">Eat</span><a href="/menu/">Menu</a><a href="/lunch-buffet/">Lunch buffet</a><a href="{TOAST}" rel="noopener">Order online</a><a href="{GIFTCARDS}" rel="noopener">Gift cards</a></div>
<div class="foot-col"><span class="lbl">Catering</span><a href="/catering/">Indian catering</a><a href="/catering/#trays">Tray prices</a><a href="/catering/#private-events">Private events</a><a href="/catering/#quote">Request a quote</a></div>
<div class="foot-col"><span class="lbl">Visit</span><a href="/hours-directions/">Hours &amp; directions</a><a href="{OPENTABLE}" rel="noopener">Reserve on OpenTable</a><a href="{MAPS}" rel="noopener">Get directions</a><a href="tel:{PHONE_E164}">Call {PHONE}</a></div>
</div>
<div class="foot-bottom"><span>© {datetime.date.today().year} Tandoori Nights</span><span>Kentlands · Gaithersburg, Maryland</span></div>
</div></footer>
<nav class="actionbar" aria-label="Quick actions"><a class="primary" href="{TOAST}" rel="noopener">Order</a><a href="tel:{PHONE_E164}">Call</a><a href="{MAPS}" rel="noopener">Directions</a></nav>
'''

def restaurant_ld():
    return {"@context": "https://schema.org", "@type": "Restaurant", "@id": SITE + "/#restaurant", "name": "Tandoori Nights",
            "url": SITE, "image": SITE + "/images/spread-hero.jpg", "logo": SITE + "/images/logo.png", "telephone": PHONE_E164,
            "servesCuisine": ["Indian", "North Indian", "Tandoori"], "priceRange": "$$",
            "address": {"@type": "PostalAddress", "streetAddress": ADDRESS_1, "addressLocality": CITY, "addressRegion": STATE, "postalCode": ZIP, "addressCountry": "US"},
            "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
            "hasMenu": SITE + "/menu/", "acceptsReservations": OPENTABLE, "menu": SITE + "/menu/",
            "openingHoursSpecification": [
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "11:30", "closes": "14:30"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "16:30", "closes": "22:00"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"], "opens": "11:30", "closes": "22:00"}],
            "potentialAction": [{"@type": "OrderAction", "target": TOAST}, {"@type": "ReserveAction", "target": OPENTABLE}],
            "sameAs": [s for s in SAME_AS if s]}

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in items]}

def breadcrumb_ld(crumbs):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (name, url) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": re.sub('&amp;', '&', name), "item": SITE + url})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def faq_html(items, title='Questions we get every day', label='Good to know'):
    rows = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(items))
    return f'<section class="section wrap side faq"><div class="stack"><p class="lbl">{label}</p><h2>{title}</h2></div><div>{rows}</div></section>'

def page(path, title, desc, active, body, ld=(), og_image='spread-hero.jpg', crumbs=None):
    canon = SITE + path
    extra_ld = [breadcrumb_ld(crumbs)] if crumbs else []
    lds = ''.join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in [restaurant_ld(), *extra_ld, *ld])
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Tandoori Nights"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/images/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F6EEDD">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Barlow+Condensed:wght@500;600&display=swap">
<link rel="stylesheet" href="/css/site.css">
<script>if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion:reduce)').matches){{document.documentElement.className+=' js'}}</script>
{lds}
</head>
<body>
{nav(active)}
<main id="main">
{body}
</main>
{FOOTER}
<script>
(function(){{
 var h=document.querySelector('.site-header');
 var s=function(){{if(h)h.classList.toggle('scrolled',(window.scrollY||0)>8)}};s();
 addEventListener('scroll',s,{{passive:true}});
 if(!document.documentElement.classList.contains('js'))return;
 var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{rootMargin:'0px 0px -6% 0px',threshold:.04}});
 document.querySelectorAll('main>section:not(:first-child),main>picture').forEach(function(el){{io.observe(el)}});
}})();
</script>
</body>
</html>
'''
    # make internal links relative so the site also works opened from a folder (file://) and in any sub-directory
    depth = len([p for p in path.strip('/').split('/') if p])
    rel = '../' * depth if depth else './'
    html = re.sub(r'((?:href|src|action|srcset)=")/(?!/)', lambda m: m.group(1) + rel, html)
    html = html.replace(', /images/', ', ' + rel + 'images/')
    html = html.replace(f'href="{rel}"', f'href="{rel}index.html"') if depth else html.replace('href="./"', 'href="./index.html"')
    html = re.sub(r'href="(\.\./|\./)([a-z-]+)/"', lambda m: f'href="{m.group(1)}{m.group(2)}/index.html"', html)
    html = re.sub(r'href="(\.\./|\./)([a-z-]+)/#', lambda m: f'href="{m.group(1)}{m.group(2)}/index.html#', html)
    d = os.path.join(OUT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(html)
    return canon

def hero(crumb, h1, intro, extra=''):
    return f'''<section class="section-tight wrap stack" style="max-width:1100px;margin-left:0">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
<h1>{h1}</h1>{STROKE}
<p style="font-size:clamp(19px,1.6vw,22px)">{intro}</p>{extra}
</section>'''

def tiles(items):
    return '<div class="three">' + ''.join(f'<div class="tile"><span class="lbl">{l}</span><span class="big">{b}</span><p>{t}</p></div>' for l, b, t in items) + '</div>'

urls = []

# ---------------- HOME ----------------
doors = ''.join(f'<a class="door" href="{h}"{" rel=noopener" if h.startswith("http") else ""}><span class="lbl">{l}</span><span class="t">{t}</span><span style="color:var(--body)">{d}</span><span class="lbl">{c} →</span></a>' for l, t, d, c, h in HOME_DOORS)
body = f'''
<section class="hero">
{pic('spread-hero.jpg', HERO_ALT, 'hero-bg', 1800, 1350, eager=True, sizes='100vw')}
<div class="hero-scrim" aria-hidden="true"></div>
<div class="hero-inner">
<p class="lbl hero-eyebrow">Indian restaurant in Kentlands Market Square · Gaithersburg, MD</p>
<h1 class="hero-quote">“{HERO_QUOTE}”</h1>{STROKE}
<p class="lbl hero-src">{HERO_QUOTE_SRC}</p>
<p class="hero-intro">{HOME_INTRO}</p>
<div class="btns"><a class="btn btn-primary" href="{TOAST}" rel="noopener">Start an order</a><a class="btn btn-ghost" href="{OPENTABLE}" rel="noopener">Book a table</a><a class="lbl hero-cat" href="/catering/">Catering →</a></div>
</div>
</section>
<section class="section linen"><div class="wrap doors">{doors}</div></section>
{pic('mural-artwork.jpg', MURAL_ALT, 'band', 2172, 724, sizes='100vw')}
<section class="section dark"><div class="wrap two">
<div class="stack"><p class="lbl">Indian catering in Gaithersburg</p><h2>{HOME_CATERING_H2}</h2><p>{HOME_CATERING_P}</p>
<div class="rows">{''.join(f'<div class="row"><b>{a}</b><span>{b}</span></div>' for a, b in HOME_CATERING_ROWS)}</div>
<div class="btns"><a class="btn btn-orange" href="/catering/">Get a catering quote</a><a class="btn btn-ghost" href="/catering/#trays">See tray prices</a></div></div>
{pic('appetizer-spread.jpg', 'Tandoori Nights appetizers on white square plates: lamb chops, samosa chaat, aloo tikki and chicken curry')}
</div></section>
<section class="section linen"><div class="wrap two two-start">
<div class="stack"><p class="lbl">Dine in · Kentlands Market Square</p><h2>Hours &amp; directions</h2>
<address>{ADDRESS_1}, Kentlands<br>{CITY}, {STATE} {ZIP}</address>
{HOURS_TABLE}
<p>Reservations on <a href="{OPENTABLE}" rel="noopener">OpenTable</a> or at <a href="tel:{PHONE_E164}">{PHONE}</a>. Walk-ins welcome. Dining-room buyouts available for private events and large groups.</p>
<div class="btns"><a class="btn btn-outline" href="{MAPS}" rel="noopener">Get directions</a><a class="btn btn-outline" href="tel:{PHONE_E164}">Call</a></div></div>
<div class="stack">{pic('dining-room-mural.jpg', 'The dining room at Tandoori Nights under the hand-painted mural')}<p style="font-style:italic">The dining room. Reviewers call it “cozy,” “quiet” and “clean and bright.” Free public lot out front.</p></div>
</div></section>
{faq_html(HOME_FAQ)}
'''
urls.append(page('/', 'Tandoori Nights | Indian Restaurant in Kentlands, Gaithersburg MD', HOME_DESC, 'home', body, [faq_ld(HOME_FAQ)]))

# ---------------- MENU ----------------
def slug(t): return re.sub(r'[^a-z]+', '-', re.sub('&amp;', 'and', t.lower())).strip('-')
VEGAN_DISHES = {'chana masala', 'yellow daal', 'baingan bharta', 'vegetable jalfrezi', 'okra do piaza', 'khile phool'}
def diet_for(section, name):
    n = re.sub('&amp;', '&', name).lower()
    if n in VEGAN_DISHES:
        return ['https://schema.org/VeganDiet', 'https://schema.org/VegetarianDiet']
    if 'vegetarian' in section.lower():
        return ['https://schema.org/VegetarianDiet']
    return []
def menu_item_ld(section, n, pr, d):
    item = {"@type": "MenuItem", "name": re.sub('&amp;', '&', n), "description": re.sub('<[^>]+>', '', d),
            "offers": {"@type": "Offer", "price": re.match(r'[\d.]+', pr).group(0), "priceCurrency": "USD"}}
    diets = diet_for(section, n)
    if diets:
        item["suitableForDiet"] = diets
    return item
chips = ''.join(f'<a class="chip" href="#{slug(c[0])}">{c[0]}</a>' for c in MENU)
cats = ''
menu_ld = {"@context": "https://schema.org", "@type": "Menu", "@id": SITE + "/menu/#menu", "name": "Tandoori Nights menu", "hasMenuSection": []}
for i, (name, img, blurb, items) in enumerate(MENU):
    rows = ''.join(f'<div class="dish"><div class="dish-line"><h3>{n}</h3><span class="dots"></span><span class="price">${pr}</span></div><p>{d}</p></div>' for n, pr, d in items)
    photo = pic(img, f'{re.sub("&amp;", "and", name)} at Tandoori Nights') if img else ''
    cats += f'<section id="{slug(name)}" class="section menu-cat{" linen" if i % 2 else ""}"><div class="wrap side"><div class="stack"><h2>{name}</h2>{f"<p>{blurb}</p>" if blurb else ""}{photo}</div><div class="dishes">{rows}</div></div></section>'
    menu_ld["hasMenuSection"].append({"@type": "MenuSection", "name": re.sub('&amp;', '&', name),
        "hasMenuItem": [menu_item_ld(name, n, pr, d) for n, pr, d in items]})
popular = ''.join(f'<a class="chip" href="/menu/{x["slug"]}/">{x["name"].split(" (")[0]}</a>' for x in DISHES)
popular_block = f'<section class="section wrap stack"><p class="lbl">Explore</p><h2>Read more about our most-loved dishes</h2><p>Deep dives on the dishes Gaithersburg orders most — how they’re made, what to pair them with.</p><div class="chips" style="margin-top:8px">{popular}</div></section>'
menu_nav = f'<nav class="menu-nav" aria-label="Menu categories"><div class="menu-nav-inner">{chips}</div></nav>'
menu_nav_js = ('<script>(function(){'
 'var nav=document.querySelector(".menu-nav");if(!nav)return;'
 'var inner=nav.querySelector(".menu-nav-inner"),links={};'
 'nav.querySelectorAll("a.chip").forEach(function(a){links[a.getAttribute("href").slice(1)]=a;});'
 'if(!("IntersectionObserver" in window))return;'
 'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){'
 'var a=links[e.target.id];if(a){for(var k in links)links[k].classList.remove("active");a.classList.add("active");'
 'inner.scrollTo({left:a.offsetLeft-inner.clientWidth/2+a.offsetWidth/2,behavior:"smooth"});}}});},'
 '{rootMargin:"-45% 0px -50% 0px",threshold:0});'
 'document.querySelectorAll(".menu-cat[id]").forEach(function(c){io.observe(c);});'
 '})();</script>')
body = hero('Menu', 'Menu &amp; prices.', MENU_INTRO) + menu_nav + cats + popular_block + faq_html(MENU_FAQ, 'Menu questions') + menu_nav_js
urls.append(page('/menu/', 'Menu & Prices | Tandoori Nights, Gaithersburg MD', MENU_DESC, 'menu', body, [menu_ld, faq_ld(MENU_FAQ)], 'butter-chicken.jpg', crumbs=[('Menu', '/menu/')]))

# ---------------- DISH PAGES (per-dish SEO landing pages) ----------------
DIET_LABEL = {'veg': 'Vegetarian', 'vegan': 'Vegan'}
DIET_SCHEMA = {'veg': ['https://schema.org/VegetarianDiet'], 'vegan': ['https://schema.org/VeganDiet', 'https://schema.org/VegetarianDiet']}
for d in DISHES:
    durl = f"/menu/{d['slug']}/"
    short = d['name'].split(' (')[0]
    dietbadge = f'<span class="chip" style="pointer-events:none;background:var(--linen)">{DIET_LABEL[d["diet"]]}</span>' if d.get('diet') else ''
    paras = ''.join(f'<p>{p}</p>' for p in d['body'])
    pairchips = ''.join(f'<a class="chip" href="{href}">{label}</a>' for label, href in d['pairs'])
    dbody = f'''<section class="section-tight wrap stack" style="max-width:1100px;margin-left:0">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/menu/">Menu</a><span aria-hidden="true">/</span><span>{short}</span></nav>
<h1>{d['name']}</h1>{STROKE}
<p style="font-size:clamp(19px,1.6vw,22px)">{d['lead']}</p>
<div class="btns"><a class="btn btn-primary" href="{TOAST}" rel="noopener">Order online</a><span class="price" style="font-size:20px">${d['price']}</span>{dietbadge}</div>
</section>
<section class="section wrap side two-start"><div class="stack">{pic(d['img'], d['alt'])}</div>
<div class="stack">{paras}<p style="font-style:italic">{d['serve']}</p>
<div class="stack" style="gap:10px"><p class="lbl">Goes well with</p><div class="chips">{pairchips}</div></div>
<div class="btns"><a class="btn btn-primary" href="{TOAST}" rel="noopener">Order {short}</a><a class="btn btn-outline" href="/menu/">See the full menu</a></div></div></section>
''' + faq_html(d['faq'], f"{short} — questions")
    dish_ld = {"@context": "https://schema.org", "@type": "MenuItem", "@id": SITE + durl + "#item", "name": d['name'],
               "description": d['lead'], "url": SITE + durl, "image": SITE + "/images/" + d['img'],
               "isPartOf": {"@id": SITE + "/menu/#menu"},
               "offers": {"@type": "Offer", "price": d['price'], "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": TOAST}}
    if d.get('diet'):
        dish_ld["suitableForDiet"] = DIET_SCHEMA[d['diet']]
    urls.append(page(durl, d['title'], d['desc'], 'menu', dbody, [dish_ld, faq_ld(d['faq'])], d['img'],
                     crumbs=[('Menu', '/menu/'), (d['name'], durl)]))

# ---------------- LUNCH BUFFET ----------------
body = hero('Lunch buffet', 'Indian lunch buffet in Gaithersburg, Monday to Friday.', BUFFET_INTRO) + f'''
<section class="section-tight wrap two">{pic('spread-hero.jpg', 'Tandoori Nights buffet dishes: tandoori chicken, butter chicken, palak paneer, naan, chaat, biryani and desserts')}
<div class="stack"><p class="lbl">What’s on the line</p><h2>{BUFFET_H2}</h2><div class="rows">{''.join(f'<div class="row"><b>{a}</b><span>{b}</span></div>' for a, b in BUFFET_ROWS)}</div>
<div class="btns"><a class="btn btn-primary" href="{OPENTABLE}" rel="noopener">Reserve a table</a><a class="btn btn-outline" href="{INSTAGRAM}" rel="noopener">Today’s lineup on Instagram</a></div></div></section>
{pic('mural-artwork.jpg', MURAL_ALT, 'band', 2172, 724, sizes='100vw')}
<section class="section wrap">{tiles(BUFFET_TILES)}</section>
<section class="section linen"><div class="wrap side"><div class="stack"><p class="lbl">From the reviews</p><h2>What people say about lunch.</h2></div>
<div class="two two-start">{''.join(f'<blockquote><p>“{q}”</p><span class="lbl" style="color:var(--muted)">{s}</span></blockquote>' for q, s in BUFFET_QUOTES)}</div></div></section>
''' + faq_html(BUFFET_FAQ, 'Buffet questions')
urls.append(page('/lunch-buffet/', 'Indian Lunch Buffet in Gaithersburg, Mon–Fri | Tandoori Nights', BUFFET_DESC, 'buffet', body, [faq_ld(BUFFET_FAQ)], crumbs=[('Lunch buffet', '/lunch-buffet/')]))

# ---------------- CATERING & EVENTS ----------------
def tray_table(head, rows):
    return f'<div class="tray-head"><span>{head}</span><span>Small</span><span>Med</span><span>Large</span><span>XL</span></div>' + ''.join(
        f'<div class="tray"><div><span class="n">{r[0]}</span>{f"<i>{r[1]}</i>" if r[1] else ""}</div>' + ''.join(f'<span class="price">{p}</span>' for p in r[2:]) + '</div>' for r in rows)
pieces = f'<div class="piece-head"><span>Appetizers by the piece · min 20</span><span>Each</span></div>' + ''.join(f'<div class="piece"><span>{n}</span><span class="price">{p}</span></div>' for n, p in PIECES)
form = f'''<form id="quote" class="quote" name="catering" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="company">
<input type="hidden" name="form-name" value="catering"><p class="sr"><label>Leave blank: <input name="company"></label></p>
<h2 style="font-size:32px">Get a catering quote</h2><p style="font-size:17px">For weekends, evenings, buffets, dining-room buyouts, and anything over 50 guests. We reply within {REPLY_TIME}.</p>
<div class="pair"><label>Event date<input type="date" name="date" required></label><label>Guests<input type="number" name="guests" min="1" placeholder="50" required></label></div>
<label>Type of event<select name="event"><option>Office lunch</option><option>Corporate event</option><option>Wedding or celebration</option><option>Birthday or party</option><option>Holiday gathering</option></select></label>
<label>Service<select name="service"><option>Tray order (pickup or delivery)</option><option>Full-service buffet at my venue</option><option>Private event / dining-room buyout</option><option>Not sure yet</option></select></label>
<div class="pair"><label>Name<input type="text" name="name" autocomplete="name" required></label><label>Phone<input type="tel" name="phone" autocomplete="tel" required></label></div>
<label>Email<input type="email" name="email" autocomplete="email" required></label>
<label>Anything else<textarea name="notes" placeholder="Venue, dietary needs, dishes you have in mind"></textarea></label>
<button class="btn btn-primary" type="submit">Request my quote</button></form>'''
body = f'''<section class="section-tight wrap two two-start">
<div class="stack"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>Catering &amp; events</span></nav>
<h1>{CATERING_H1}</h1>{STROKE}<p style="font-size:clamp(19px,1.6vw,22px)">{CATERING_INTRO}</p>
{tiles(CATERING_TILES)}
<a class="lbl" href="{EZCATER}" rel="noopener">Weekday lunch drop-off? Order on ezCater, delivery 11:30–2 →</a></div>
{form}</section>
<section class="section wrap stack"><h2>Three ways to cater, from a $40 tray of rice to a wedding for 200.</h2>
<div class="three">{''.join(f'<article class="stack">{pic(img, alt) if img else ""}<h3>{h}</h3><p>{p}</p><span class="lbl">{l}</span></article>' for img, alt, h, p, l in CATERING_FORMATS)}</div></section>
{pic('mural-artwork.jpg', MURAL_ALT, 'band', 2172, 724, sizes='100vw')}
<section id="trays" class="section wrap stack menu-cat"><div class="side" style="align-items:end"><div class="stack"><p class="lbl">Catering menu</p><h2>Tray prices.</h2></div><p>{TRAY_NOTE}</p></div>
<div class="two two-start" style="gap:64px"><div>{tray_table('Entrées', ENTREES)}<div style="height:28px"></div>{tray_table('Rice &amp; biryani', RICE)}</div>
<div>{pieces}<div style="height:28px"></div>{tray_table('Appetizer trays, sides &amp; sweets', TRAYS)}<p style="margin-top:18px;font-size:17px">{BREADS_NOTE}</p></div></div>
<div class="btns"><a class="btn btn-primary" href="/catering/#quote">Request a catering quote</a><a class="btn btn-outline" href="/catering-menu.pdf" download>Download the menu (PDF)</a></div></section>
<section class="section linen"><div class="wrap stack"><h2>Catering by occasion</h2><div class="four" style="border-top:1px solid var(--rule)">{''.join(f'<a class="stack" href="/catering/#quote" style="color:var(--ink);padding-top:24px"><span style="font-size:28px;font-weight:500">{h}</span><p>{p}</p><span class="lbl">{l} →</span></a>' for h, p, l in OCCASIONS)}</div></div></section>
<section class="section wrap side two-start"><div class="stack"><h2>How catering works</h2>{pic('mural-artwork.jpg', 'Lotus detail from the dining room mural', sizes='(max-width:760px) 100vw, 380px')}</div>
<ol style="margin:0;padding:0;list-style:none" class="rows">{''.join(f'<li class="row" style="grid-template-columns:80px 1fr"><span style="font-size:56px;font-weight:500;color:var(--red);line-height:1">{i+1}</span><div class="stack" style="gap:6px"><span style="font-size:28px;font-weight:500">{h}</span><p>{p}</p></div></li>' for i, (h, p) in enumerate(HOW_IT_WORKS))}</ol></section>
<section id="private-events" class="section dark menu-cat"><div class="wrap stack"><p class="lbl">Private events · in the restaurant</p><h2>{EVENTS_H2}</h2><p style="font-size:clamp(19px,1.6vw,21px);max-width:900px">{EVENTS_INTRO}</p></div>
<div class="wrap two two-start" style="margin-top:40px">{pic('private-dining-room.jpg', 'The Tandoori Nights dining room set with white tablecloths and leather chairs')}<div class="stack">{pic('cocktails-bar.jpg', 'Cocktails on the bar at Tandoori Nights')}<p>To book a buyout, fill out the <a href="/catering/#quote">catering form</a> at the top of this page, choose “Private event / dining-room buyout,” and we’ll get back to you.</p></div></div>
<div class="wrap" style="margin-top:40px">{tiles(EVENT_TILES)}</div></section>
''' + faq_html(CATERING_FAQ, 'Catering &amp; event questions')
cat_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + "/catering/#service", "serviceType": "Indian catering", "provider": {"@id": SITE + "/#restaurant"},
          "areaServed": [{"@type": "City", "name": c} for c in SERVICE_AREA], "url": SITE + "/catering/",
          "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Catering trays", "itemListElement": [
              {"@type": "Offer", "itemOffered": {"@type": "Product", "name": f"{r[0]} tray (small, serves 15–20)"}, "price": r[2].strip('$'), "priceCurrency": "USD"} for r in ENTREES + RICE]}}
venue_ld = {"@context": "https://schema.org", "@type": "EventVenue", "name": "Tandoori Nights dining room", "url": SITE + "/catering/#private-events",
            "address": {"@type": "PostalAddress", "streetAddress": ADDRESS_1, "addressLocality": CITY, "addressRegion": STATE, "postalCode": ZIP}}
urls.append(page('/catering/', 'Indian Catering in Gaithersburg, MD | Tray Prices & Private Events | Tandoori Nights', CATERING_DESC, 'catering', body, [cat_ld, venue_ld, faq_ld(CATERING_FAQ)], 'appetizer-spread.jpg', crumbs=[('Catering &amp; events', '/catering/')]))

# ---------------- HOURS & DIRECTIONS ----------------
body = hero('Hours &amp; directions', 'Hours, parking and directions to Tandoori Nights, Kentlands.', VISIT_INTRO) + f'''
<section class="section-tight wrap two two-start">
<div class="stack" style="gap:28px">{HOURS_TABLE.replace('<caption class="lbl">Hours</caption>', '<caption class="lbl">Hours · dine-in and takeout</caption>')}
<div class="stack" style="gap:8px"><p class="lbl">Lunch buffet</p><p>Monday to Friday, 11:30–2:30. <a href="/lunch-buffet/">Details →</a></p></div>
<div class="stack" style="gap:8px"><p class="lbl">Holidays</p><p>{HOLIDAYS}</p></div>
<address>Tandoori Nights<br>{ADDRESS_1}<br>{CITY}, {STATE} {ZIP}<br><a class="lbl" href="tel:{PHONE_E164}" style="font-size:18px">{PHONE}</a></address>
<div class="btns"><a class="btn btn-primary" href="{MAPS}" rel="noopener">Open in Google Maps</a><a class="btn btn-outline" href="{APPLE_MAPS}" rel="noopener">Apple Maps</a><a class="btn btn-outline" href="{OPENTABLE}" rel="noopener">Reserve on OpenTable</a></div></div>
<div class="stack map-sticky"><iframe title="Map to Tandoori Nights, 106 Market St, Gaithersburg" src="{MAP_EMBED}" width="100%" height="460" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></section>
<section class="section linen"><div class="wrap">{tiles(VISIT_TILES)}</div></section>
{pic('mural-artwork.jpg', MURAL_ALT, 'band', 2172, 724, sizes='100vw')}
''' + faq_html(VISIT_FAQ, 'Visiting questions')
urls.append(page('/hours-directions/', 'Hours, Parking & Directions | Tandoori Nights, Kentlands Gaithersburg', VISIT_DESC, 'visit', body, [faq_ld(VISIT_FAQ)], 'dining-room-mural.jpg', crumbs=[('Hours &amp; directions', '/hours-directions/')]))

# ---------------- THANKS / 404 ----------------
page('/thanks/', 'Thanks | Tandoori Nights', 'We got your catering request.', 'catering', hero('Thanks', 'Got it. We’ll be in touch.', f'We reply to catering and private-event requests within {REPLY_TIME}. Need it sooner? Call <a href="tel:{PHONE_E164}">{PHONE}</a>.'))
page('/404/', 'Page not found | Tandoori Nights', 'That page has moved.', 'home', hero('Not found', 'That page isn’t here.', 'Try the <a href="/menu/">menu</a>, <a href="/catering/">catering</a>, or <a href="/hours-directions/">hours &amp; directions</a>.'))
h404 = open(os.path.join(OUT, '404', 'index.html')).read().replace('../', './')
open(os.path.join(OUT, '404.html'), 'w').write(h404); shutil.rmtree(os.path.join(OUT, '404'))

# ---------------- STATIC FILES ----------------
shutil.copytree('images', os.path.join(OUT, 'images'), dirs_exist_ok=True)
shutil.copytree('css', os.path.join(OUT, 'css'), dirs_exist_ok=True)
if os.path.exists('catering-menu.pdf'): shutil.copy('catering-menu.pdf', OUT)
if os.path.isdir('icons'): shutil.copytree('icons', OUT, dirs_exist_ok=True)  # favicon.ico/.svg, apple-touch-icon, icon-192/512, site.webmanifest
today = datetime.date.today().isoformat()
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls) + '</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /thanks/\n\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open(os.path.join(OUT, 'llms.txt'), 'w').write(LLMS_TXT.format(site=SITE))
open(os.path.join(OUT, '_headers'), 'w').write('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n/images/*\n  Cache-Control: public, max-age=31536000, immutable\n/css/*\n  Cache-Control: public, max-age=604800\n')
open(os.path.join(OUT, '_redirects'), 'w').write('/catering-private-events /catering/ 301\n/contact /hours-directions/ 301\n/welcome / 301\n/order https://www.toasttab.com/tandoori-nights-106-market-st/v3 302\n')
print('built', len(urls), 'pages ->', OUT)
