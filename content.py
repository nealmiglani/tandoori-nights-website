# ============================================================
# Tandoori Nights — site content. Edit this file, then run build.py.
# Anything in [BRACKETS] is a fact to confirm before launch.
# ============================================================

SITE = 'https://www.tandoorinightsmd.com'          # no trailing slash
PHONE = '301-947-4007'
PHONE_E164 = '+13019474007'
ADDRESS_1 = '106 Market St'
CITY, STATE, ZIP = 'Gaithersburg', 'MD', '20878'
LAT, LNG = 39.1222, -77.2470                        # [CONFIRM from Google Maps pin]
TOAST = 'https://www.toasttab.com/tandoori-nights-106-market-st/v3'
GIFTCARDS = 'https://www.toasttab.com/tandoori-nights-106-market-st/giftcards'
OPENTABLE = 'https://www.opentable.com/r/tandoori-nights-gaithersburg'
EZCATER = 'https://www.ezcater.com/catering/tandoori-nights-gaithersburg'
UBEREATS = 'https://www.ubereats.com/store/tandoori-nights/ztv6RynCQj-yYWHIBS2miw'
DOORDASH = 'https://www.doordash.com/'              # [PASTE your DoorDash store link]
INSTAGRAM = 'https://www.instagram.com/'            # [PASTE your Instagram]
MAPS = 'https://www.google.com/maps/search/?api=1&query=Tandoori+Nights+106+Market+St+Gaithersburg+MD+20878'
APPLE_MAPS = 'https://maps.apple.com/?q=Tandoori+Nights+106+Market+St+Gaithersburg+MD'
MAP_EMBED = 'https://www.google.com/maps?q=Tandoori+Nights,+106+Market+St,+Gaithersburg,+MD+20878&output=embed'
SAME_AS = [OPENTABLE, 'https://www.facebook.com/tandoorinightsgaithersburg/', 'https://www.tripadvisor.com/Restaurant_Review-g41154-d496466-Reviews-Tandoori_Nights-Gaithersburg_Montgomery_County_Maryland.html',
           'https://www.yelp.com/biz/tandoori-nights-gaithersburg', UBEREATS, EZCATER, '']  # add Google Maps place URL, Instagram
SERVICE_AREA = ['Gaithersburg', 'Rockville', 'Bethesda', 'Silver Spring', 'Washington, DC', 'Arlington', 'Alexandria']  # DMV-wide; [CONFIRM exact cities]

# Facts to confirm
REPLY_TIME = '[X] business hours'
ROOM_SEATED = '[XX] guests'
ROOM_SEATED_NUM = 30                                 # [CONFIRM] used in schema only
BUFFET_PRICE = '[$XX]'
DELIVERY_RADIUS = '[XX] miles'
LEAD_TIME_TRAYS = '[XX] hours'
LEAD_TIME_EVENTS = '[XX] weeks'
YEAR_OPENED = '[YEAR]'
HOLIDAYS = 'Open most holidays; Thanksgiving and Christmas hours are posted on Google two weeks ahead. [CONFIRM]'

HOURS_TABLE = '''<table class="hours"><caption class="lbl">Hours</caption>
<tr><th scope="row">Monday – Friday</th><td>11:30am–2:30pm · 4:30–10pm</td></tr>
<tr><th scope="row">Saturday – Sunday</th><td>11:30am–10pm</td></tr></table>'''

# ---------------- HOME ----------------
HOME_DESC = 'Indian restaurant in Kentlands Market Square, Gaithersburg MD. Butter chicken rated 4.7 across 2,000+ orders, tandoori lamb chops, a weekday lunch buffet, and Indian catering across the DMV for any size. Dine in, order online, or cater.'
HERO_ALT = 'A Tandoori Nights spread: butter chicken, palak paneer, tandoori chicken on a sizzling platter, chicken 65, shrimp salad, naan, samosa chaat, biryani, dal makhani, kheer and gulab jamun'
MURAL_ALT = 'The mural on the Tandoori Nights dining room wall: a sleeping woman with green hair, a lotus, and a starry blue sky'
HERO_QUOTE = 'Some of the best Indian food I’ve had this side of the Atlantic.'
HERO_QUOTE_SRC = 'Tripadvisor review · November 2024'
HOME_INTRO = 'For over a decade, Tandoori Nights has cooked North Indian food at 106 Market St in Kentlands: butter chicken rated 4.7 across 2,000+ orders, lamb chops off the clay oven, a weekday lunch buffet, and catering for offices, weddings and parties of any size across the DMV. Every dish is cooked to order with fresh, all-natural ingredients.'
HOME_DOORS = [
    ('Pickup &amp; delivery · 2,000+ orders, 4.7★', 'Order online', 'Butter chicken, tikka masala and palak paneer are what Gaithersburg orders most. Order direct through Toast at menu prices — skip the delivery-app markup.', 'Start an order', TOAST),
    ('Monday to Friday · 11:30–2:30', 'Lunch buffet', f'{BUFFET_PRICE} for [X] curries, tandoori chicken, naan from the oven and dessert. Regulars say it keeps getting better.', 'This week’s buffet', '/lunch-buffet/'),
    ('Catering for any headcount · rated 5.0★', 'Catering', 'A small chicken tikka masala tray (15–20 people) is $100; extra-large (45–50) is $200. Bigger group? Order several XL trays or a full-service buffet. Vegetable trays from $75.', 'Catering menu &amp; prices', '/catering/'),
]
HOME_CATERING_H2 = 'Indian catering for offices and weddings across the DMV.'
HOME_CATERING_P = 'Four tray sizes serving 15 to 50 each — order several for larger groups, or a full-service buffet for any headcount. Real prices on the page, rated 5.0 with 100% on-time delivery.'
HOME_CATERING_ROWS = [
    ('Tray orders', 'Small trays: chicken curry $100, vegetable or dal $75, paneer $85, chicken biryani $100. Naan $2.99 a piece.'),
    ('Full-service buffet', 'We set up, serve and clear. Weddings, receptions, Diwali and office parties. Fill out the catering form and we’ll get back to you.'),
    ('Private room', 'A set menu in our private room for rehearsal dinners, client dinners and birthdays.'),
]
HOME_FAQ = [
    ('How much does Indian catering cost in Gaithersburg?', 'Trays come in four sizes: small serves 15–20, extra-large 45–50, with multiple XL trays or a full-service buffet for larger groups. A small chicken tray is $100, vegetable or dal $75, paneer $85, chicken biryani $100; naan is $2.99 a piece with a 20-piece minimum. A basic lunch for 15–20 (chicken, vegetable, rice, naan) is about $275, roughly $14–18 a head before delivery. Buffets and prix fixe are quoted through our catering form.'),
    ('Do you deliver in Gaithersburg?', 'Yes. The best way is to order direct through Toast for pickup or delivery — menu prices, no delivery-app markup. Butter chicken is our most-ordered dish, rated 4.7 across more than 2,000 orders.'),
    ('Is there a lunch buffet?', f'Monday to Friday, 11:30am to 2:30pm. {BUFFET_PRICE} per person for [X] curries plus tandoori chicken, naan and dessert.'),
    ('Do you have vegetarian, vegan or gluten-free dishes?', 'Sixteen vegetarian mains, including Palak Paneer, Dal Makhani, Chana Masala and Malai Kofta. The kitchen cooks with less oil and all-natural ingredients. Ask your server about vegan and gluten-free options. [CONFIRM which dishes.]'),
    ('Where do I park in Kentlands?', f'Free public lot in Kentlands Market Square, steps from the door at 106 Market St. Reservations on OpenTable or at {PHONE}; walk-ins welcome. Private room for up to {ROOM_SEATED}.'),
]

# ---------------- MENU ----------------
MENU_DESC = 'Full Tandoori Nights menu with prices: butter chicken, chicken tikka masala, lamb chops, palak paneer, biryani, twelve breads and sixteen vegetarian mains. Indian restaurant in Kentlands, Gaithersburg MD.'
MENU_INTRO = 'Every dish we cook at 106 Market St, with prices, as text you can search. North Indian curries, tandoor kebabs, biryani, sixteen vegetarian mains and twelve breads. The kitchen cooks with less oil and all-natural ingredients. Prices are dine-in and pickup; delivery apps add their markup.'
MENU_FAQ = [
    ('Which dishes are vegan?', 'Chana masala, yellow daal, baingan bharta, vegetable jalfrezi, okra do piaza and khile phool can be made without dairy on request. [CONFIRM list with the kitchen.]'),
    ('Which dishes are gluten-free?', 'Most curries, tandoori meats, biryani and rice are made without wheat; breads and pakoras are not. Tell your server about allergies. [CONFIRM.]'),
    ('Can you adjust the spice?', 'Yes. Every curry can be made mild, medium or hot. Vindaloo and Chicken 65 are hot by default.'),
    ('Are the prices the same for delivery?', 'These are the dine-in and pickup prices. Delivery apps list higher prices to cover their fees — ordering direct through Toast gets you the menu prices.'),
]

# ---------------- LUNCH BUFFET ----------------
BUFFET_DESC = f'Weekday Indian lunch buffet in Gaithersburg, Monday to Friday 11:30–2:30 at Tandoori Nights, Kentlands. Tandoori chicken, butter chicken, curries, naan from the oven. {BUFFET_PRICE} per person.'
BUFFET_INTRO = f'From 11:30am to 2:30pm on weekdays, the tandoor and the curry line feed the buffet at 106 Market St. Tripadvisor regulars call it “outstandingly good” and say it “has constantly improved.” {BUFFET_PRICE} per person. [CONFIRM current buffet, price and lineup.]'
BUFFET_H2 = 'Ten to twelve dishes, changed daily.'
BUFFET_ROWS = [
    ('Every day', 'Tandoori chicken, butter chicken, a dal, rice, naan from the oven, salad, raita, chutneys, one dessert.'),
    ('Rotating', 'Chicken tikka masala, chicken curry, palak paneer, chana masala, a lamb or goat curry, pakoras. [CONFIRM]'),
    ('Vegetarian', 'At least four vegetarian mains on the line every day.'),
]
BUFFET_TILES = [
    ('Hours', 'Mon–Fri, 11:30–2:30', 'No buffet on weekends; the full menu runs 11:30am–10pm Saturday and Sunday.'),
    ('Price', f'{BUFFET_PRICE} per person', 'Kids under [X] [$XX]. Drinks separate. [CONFIRM]'),
    ('Groups', 'Office lunches welcome', f'Tables of 8 or more: call {PHONE} the morning of. Free lot out front in Kentlands Market Square.'),
]
BUFFET_QUOTES = [
    ('The lunch buffet has constantly improved and it is an outstandingly good buffet for a satisfying and flavorful lunch.', 'Tripadvisor'),
    ('The selection and taste exceeded my expectations. The staff was friendly.', 'Tripadvisor, “Great Lunch Buffet”'),
]
BUFFET_FAQ = [
    ('What days is the Indian lunch buffet?', 'Monday to Friday, 11:30am to 2:30pm, at 106 Market St in Kentlands. No buffet on weekends.'),
    ('How much is the lunch buffet?', f'{BUFFET_PRICE} per person, [$XX] for children under [X]. [CONFIRM]'),
    ('Is the buffet vegetarian-friendly?', 'Yes. At least four vegetarian mains are on the line every day, plus dal, rice, salad and breads.'),
    ('Can I order from the menu at lunch?', 'Yes. The full menu is available at lunch alongside the buffet.'),
    ('Do you do a holiday buffet?', 'On some holidays the buffet runs as a grand buffet with extended hours; the last Mother’s Day ran 12–3:30pm. Call ahead.'),
]

# ---------------- CATERING & EVENTS ----------------
CATERING_DESC = 'Indian catering across the DMV with tray prices on the page: four tray sizes serving 15 to 50 each, order several for larger groups, $100 minimum, rated 5.0. Plus a private dining room in Kentlands for rehearsal dinners, birthdays and team nights.'
CATERING_H1 = 'Indian catering in Gaithersburg, and a private room when you’d rather come to us.'
CATERING_INTRO = f'Tandoori Nights has catered offices, weddings and holiday parties across the DMV from its Kentlands kitchen since {YEAR_OPENED}. Every tray is cooked to order in the same tandoor and pots as the dining room — rated 5.0 with 100% on-time delivery. Other Indian caterers in Gaithersburg make you call for a price; ours are right here on the page.'
CATERING_TILES = [
    ('Trays', 'Small 15–20 · XL 45–50', 'Four sizes of every entrée, rice, appetizer tray and sweet — order several XL trays for larger groups.'),
    ('By the piece', '20-piece minimum', 'Kebabs, samosas, naan and sweets priced per piece.'),
    ('Delivery', f'From $30 · {DELIVERY_RADIUS}', 'Weekday lunch delivery 11:30–2 through ezCater; evenings and weekends by arrangement.'),
]
CATERING_FORMATS = [
    ('tandoori-chicken-platter.jpg', 'A tandoori chicken platter from a Tandoori Nights full-service catering buffet', 'Full-service buffet', 'Chafing dishes, staff, setup and cleanup. Wedding receptions, Diwali parties, office holiday lunches. Quoted by headcount.', 'Quoted per guest · via the catering form'),
    ('private-dining-room.jpg', 'Private dining room set for a prix fixe dinner at Tandoori Nights', 'Prix fixe in the private room', f'A set menu, plated or family-style, in our private room for up to {ROOM_SEATED}. Rehearsal dinners, client dinners, birthdays.', 'Quoted per guest · via the catering form'),
    ('appetizer-spread.jpg', 'Tandoori Nights appetizers ready for a tray order', 'Tray orders', 'Small, medium, large and extra-large — 15 to 50 people per tray, and order several for bigger groups. Order online for weekday lunch delivery, or call for pickup any day.', 'Trays from $40 · $100 minimum'),
]
TRAY_NOTE = 'Suggested quantities are for a complete menu and are an estimate. A small tray serves 15–20, medium 25–30, large 35–40, extra-large 45–50 — for more than 50, order multiple extra-large trays or ask about a full-service buffet. Appetizers, breads and sweets by the piece, 20-piece minimum.'
ENTREES = [
    ('Vegetable / daal', 'Chana masala, aloo gobi, dal makhani, mixed vegetable.', '$75', '$90', '$115', '$155'),
    ('Paneer', 'Palak paneer, paneer makhani, paneer tikka masala.', '$85', '$100', '$125', '$175'),
    ('Chicken', 'Tikka masala, butter chicken, korma, vindaloo, saag.', '$100', '$120', '$145', '$200'),
    ('Lamb', 'Rogan josh, vindaloo, saag, bhuna.', '$110', '$150', '$185', '$235'),
    ('Goat', 'Goat curry, saag gosht.', '$125', '$165', '$205', '$255'),
    ('Fish', 'Fish Goani, Bombay fish curry.', '$115', '$160', '$190', '$245'),
    ('Prawns', 'Prawn masala, vindaloo, jalfrezi.', '$150', '$170', '$200', '$275'),
]
RICE = [
    ('Jeera rice', '', '$40', '$50', '$65', '$80'),
    ('Vegetable biryani', '', '$70', '$95', '$120', '$145'),
    ('Chicken biryani', '', '$100', '$115', '$130', '$155'),
    ('Lamb / goat biryani', '', '$110', '$140', '$170', '$215'),
    ('Shrimp biryani', '', '$130', '$155', '$185', '$235'),
    ('Veg hakka noodles / fried rice', 'With egg $80–$180.', '$70', '$95', '$125', '$160'),
    ('Chicken hakka noodles / fried rice', '', '$100', '$130', '$160', '$195'),
]
PIECES = [('Aloo tikki', '$1.75'), ('Vegetable samosa', '$2.50'), ('Paneer / chicken pakora', '$2.25 / $2.50'), ('Fish pakora', '$2.75'), ('Tandoori chicken', '$3.75'),
          ('Chicken tikka / malai tikka', '$3.75'), ('Chicken / lamb seekh kabob', '$3.25 / $3.75'), ('Lamb chops', '$5.00'), ('Tandoori prawns / fish tikka', '$4.50 / $5.00'), ('Paneer tikka', '$3.50')]
TRAYS = [
    ('Vegetable pakora', '', '$55', '$65', '$80', '$115'),
    ('Aloo chaat papdi / palak chaat', '', '$55', '$65', '$80', '$115'),
    ('Pani poori', '', '$55', '$65', '$80', '$115'),
    ('Chef salad / spinach &amp; strawberry', '', '$40', '$50–60', '$65–75', '$85'),
    ('Raita (boondi / cucumber)', '', '$40', '$50', '$65', '$75'),
    ('Kheer', '', '$55', '$65', '$80', '$100'),
    ('Gajar (carrot) halwa', '', '$75', '$90', '$120', '$150'),
    ('Moong daal halwa', '', '$85', '$100', '$120', '$140'),
]
BREADS_NOTE = 'Breads by the piece: plain naan or roti $2.99, garlic naan $4.50, onion kulcha $4.50, plain parantha (pudhina/laccha) $4.50, stuffed parantha (aloo/keema) $4.99. Sweets by the piece: gulab jamun $2.00, shahi tukra $2.50, rasmalai $2.50.'
OCCASIONS = [
    ('Office lunch', 'Delivered Monday to Friday 11:30–2. A small chicken tray, a small vegetable tray, jeera rice and 20 naan feeds 15–20 for about $275.', 'Office catering'),
    ('Weddings', 'Full-service buffets for receptions, sangeets and mehndi nights across the DMV.', 'Wedding catering'),
    ('Corporate events', 'Conferences, launches and client dinners. ezCater receipts for expense reports.', 'Corporate catering'),
    ('Holidays &amp; parties', 'Diwali, Eid, graduations and birthdays. Trays for pickup at 106 Market St any day.', 'Party trays'),
]
HOW_IT_WORKS = [
    ('Tell us the date and headcount', 'Under 50 guests on a weekday lunch: order trays on ezCater right now. Anything else: fill out the catering form and we’ll get back to you.'),
    ('Build the menu with us', 'A chicken, a lamb or fish, two vegetarian, rice, naan, one sweet is the usual shape for a mixed crowd. We set spice per tray.'),
    ('Pickup, drop-off or full service', 'Trays arrive labeled, with utensils on request. Buffets arrive with chafing dishes and staff.'),
]
EVENTS_H2 = f'Or bring the party to us: a private room in Kentlands for {ROOM_SEATED}.'
EVENTS_INTRO = 'Rehearsal dinners, birthdays, client dinners and team nights, in our private room at 106 Market St with a set menu built around the tandoor. Reviewers call the main room “cozy” and “quiet”; the private room has its own door and its own pace. Free lot out front.'
EVENT_TILES = [
    ('The room', f'Seats {ROOM_SEATED}', 'Two long tables or a U. Private entrance. [AV / TV] for slides or a toast. [CONFIRM]'),
    ('Prix fixe menus', 'From [$XX] per guest', 'Three courses served family-style: appetizer platter with three chutneys, two or three mains, rice, naan, dessert. Vegetarian and mixed menus.'),
    ('Bar', 'Full bar, open or hosted', 'Cocktails, wine, Indian beer. Set a tab limit or run a drink ticket. [CONFIRM minimums]'),
]
CATERING_FAQ = [
    ('How much does Indian catering cost per person?', 'A small tray serves 15–20. A basic lunch (small chicken tray $100, small vegetable tray $75, small jeera rice $40, 20 naan at $2.99) is about $275, roughly $14–18 a head before delivery. Add a second meat and a dessert and it lands near $22–25. Extra-large trays serve 45–50; a chicken XL is $200. For more than 50 guests, order several XL trays or a full-service buffet — there’s no upper limit. Full-service buffets are quoted by headcount and staffing; fill out the catering form and we’ll get back to you.'),
    ('How much notice do you need?', f'{LEAD_TIME_TRAYS} for tray orders; ezCater orders can be canceled up to 24 hours out (25% fee inside that). {LEAD_TIME_EVENTS} for full-service events.'),
    ('Do you deliver catering?', f'Yes. Delivery is $30 and up depending on distance, weekdays 11:30–2 through ezCater. Evenings, weekends and up to {DELIVERY_RADIUS} by arrangement. Pickup at 106 Market St any day.'),
    ('Can you handle vegetarian, vegan and gluten-free guests?', 'Our menu has sixteen vegetarian mains. Every tray is labeled; vegan and gluten-free dishes are marked on request. [CONFIRM]'),
    ('Can I order catering on ezCater?', 'Yes. We have been on ezCater since 2016 with a 5.0 rating and 100% on-time record. $100 minimum, $20 off weekday orders over $500 through 12/31/2026.'),
    ('How many people fit the private room?', f'Seated {ROOM_SEATED}, standing [XX]. Larger parties can take the main dining room on a buyout; ask.'),
    ('Is there a room fee or minimum?', '[No room fee / $XX] with a food and drink minimum of [$XX] on weekends. [CONFIRM]'),
    ('Can we bring a cake?', 'Yes. [Cake fee $X / no fee.] We’ll plate it with kulfi if you like.'),
]

# ---------------- HOURS & DIRECTIONS ----------------
VISIT_DESC = 'Tandoori Nights hours, parking and directions. 106 Market St in Kentlands Market Square, Gaithersburg MD 20878. Lunch and dinner Monday to Friday, 11:30am–10pm weekends. Free lot out front.'
VISIT_INTRO = 'We’re at 106 Market St in Kentlands Market Square, Gaithersburg, MD 20878, with a free public lot out front. Lunch and dinner Monday to Friday, straight through on weekends.'
VISIT_TILES = [
    ('Parking', 'Free lot in Kentlands Market Square', 'Public lot steps from the door, plus street parking on Market St.'),
    ('From I-270', 'Exit 11, Quince Orchard Rd', 'West on Quince Orchard Rd, left on Kentlands Blvd, right on Market St. About [X] minutes from the exit. [CONFIRM]'),
    ('Nearby', 'Kentlands, Lakelands, North Potomac', 'Fifteen minutes from Rockville and Germantown, twenty from Bethesda and Potomac.'),
]
VISIT_FAQ = [
    ('Do you take reservations?', f'Yes, on OpenTable or at {PHONE}. Walk-ins are welcome; weekend dinner fills up after 7.'),
    ('Is there outdoor seating?', 'Yes, a patio on Market St in warm months. [CONFIRM season and seats.]'),
    ('Is the restaurant wheelchair accessible?', '[CONFIRM] Street-level entrance, accessible restroom.'),
    ('Do you have a bar?', 'A full bar: cocktails, wine, and Indian beers. Happy hour [DAYS, TIMES]. [CONFIRM]'),
    ('Is there a second location?', 'No. The Bethesda location has closed; Gaithersburg is our only restaurant.'),
]

LLMS_TXT = '''# Tandoori Nights
> Indian restaurant and caterer at 106 Market St, Kentlands Market Square, Gaithersburg, MD 20878. Phone 301-947-4007.

- Cuisine: North Indian, tandoori. Sixteen vegetarian mains. Kitchen uses less oil and all-natural ingredients.
- Hours: Mon–Fri 11:30am–2:30pm and 4:30–10pm; Sat–Sun 11:30am–10pm. Weekday lunch buffet 11:30–2:30.
- Most ordered: butter chicken (chicken makhani), chicken tikka masala, palak paneer. Uber Eats rating 4.7 from 2,000+ ratings.
- Catering across the DMV: trays in four sizes (small 15–20 to extra-large 45–50); order multiple XL trays or a full-service buffet for larger groups — no upper limit. Small chicken tray $100, vegetable $75, paneer $85, chicken biryani $100. $100 minimum. Rating 5.0.
- Private dining room available for events.
- Only location; the Bethesda location is closed.

## Pages
- Menu with prices: {site}/menu/
- Lunch buffet: {site}/lunch-buffet/
- Catering trays, prices and private events: {site}/catering/
- Hours, parking, directions: {site}/hours-directions/
- Order online (Toast): https://www.toasttab.com/tandoori-nights-106-market-st/v3
'''
MENU = [
 ('Chaat &amp; appetizers', 'samosa-chaat.jpg', 'Samosa chaat, aloo tikki and pani poori are the starters reviewers name most.', [
  ('Pani Poori','7.99','Six bite-size puffed pooris with spiced potato and flavored waters, served as shots.'),
  ('Aloo Tikki','9.99','Potato patties stuffed with cheese, nuts and raisins.'),
  ('Aloo Chat Papri','8.99','Chickpeas, potatoes and flour crisps with chutneys.'),
  ('Raj Kachori','9.99','Kachori filled with chickpeas and thin vermicelli.'),
  ('Kurkure Hariyali','8.99','Crispy spinach with yogurt and tamarind.'),
  ('Vegetable Samosa','7.99','Seasoned potatoes and green peas in light pastry.'),
  ('Pakoras','8.99–15.99','Vegetable, paneer, chicken, fish or prawn.'),
  ('Chicken 65','12.99','Fiery, tangy diced chicken tempered with mustard seeds.'),
  ('Chili Chicken / Chili Paneer','12.99','Crispy, with peppers and onions in a sweet-sour-spicy sauce.'),
  ('Gobi Manchurian / Veg Manchurian','12.99','Crispy cauliflower or vegetable fritters in manchurian sauce.'),
  ('Masala Calamari','12.99','Fried squid rubbed with spices.'),
  ('Garlic Shrimp','14.99','Delicately spiced shrimp in white wine and honey.'),
  ('Masala Fries','8.99','French fries with our house masala.'),
  ('Assorted Platter','15.99','Vegetable, chicken and lamb appetizers.'),
 ]),
 ('From the tandoor', 'tandoori-chicken-platter.jpg', 'The clay oven seals heat in; marinated meats, seafood and paneer keep their juices.', [
  ('Tandoori Chicken','17.99 half · $29.99 whole','Marinated in yogurt and freshly ground spices.'),
  ('Chicken Tikka','19.99','Boneless cubes of chicken breast, yogurt and spices.'),
  ('Achari Chicken Tikka','19.99','In pickling spices.'),
  ('Malai Kabob','20.99','Chicken in yogurt, cream cheese and ginger.'),
  ('Chicken Seekh Kabob','18.99','Minced chicken, skewered and grilled.'),
  ('Lamb Chops','24.99','Marinated with ginger, herbs and freshly ground spices.'),
  ('Lamb Seekh Kabob','19.99','Minced lamb, skewered and grilled.'),
  ('Boti Kabob','22.99','Marinated lamb cubes.'),
  ('Fish Tikka','23.99','Salmon cubes, marinated and grilled.'),
  ('Prawn Angarey','24.99','Large prawns, marinated and grilled.'),
  ('Tandoori Fish','25.99','Whole fish, marinated and baked.'),
  ('Tandoori Seafood Platter','28.99','Shrimp, salmon and scallops.'),
  ('Paneer Tikka','16.99','Marinated cottage cheese, grilled in the clay oven.'),
  ('Tandoori Vegetables','17.99','Cauliflower, broccoli, paneer, peppers and fruit.'),
  ('Tandoori Special Kabob Platter','23.99','Mixed grilled meats.'),
 ]),
 ('Chicken', 'butter-chicken.jpg', 'Butter chicken is #1 on Uber Eats across 2,000+ orders. Tikka masala is #2.', [
  ('Chicken Makhani (Butter Chicken)','19.99','Tandoori chicken in a creamy tomato sauce.'),
  ('Chicken Tikka Masala','19.99','Grilled chicken in a tomato and onion sauce.'),
  ('Chicken Korma Kashmiri','19.99','Mild, creamy sauce with fruits.'),
  ('Chicken Vindaloo','19.99','Ginger, garlic and potatoes in a fiery sauce.'),
  ('Chicken Saag','19.99','Cooked with chopped creamy spinach.'),
  ('Chicken Jalfrezi','19.99','Curry sauce with sautéed vegetables.'),
  ('Chicken Curry','19.99','Tender chicken in traditional curry sauce.'),
 ]),
 ('Lamb &amp; goat', 'lamb-saag.jpg', 'Rogan josh the traditional way; bone-in goat on slow heat.', [
  ('Lamb Rogan Josh','22.99','Onions, tomatoes and ginger.'),
  ('Lamb Saag','22.99','Lamb with creamy spinach.'),
  ('Lamb Vindaloo','22.99','Tomatoes and potatoes in a fiery sauce.'),
  ('Lamb Korma Kashmiri','22.99','Mild, creamy sauce with fruits.'),
  ('Lamb Pasanda','22.99','Lean lamb in a creamy sauce of fragrant spices.'),
  ('Achari Lamb','22.99','Pickled spices and mustard oil.'),
  ('Lamb Bhuna Punjabi','22.99','Tomatoes, onions and herbs.'),
  ('Lamb Patiala','22.99','Boneless lamb with onions, ginger, garlic and potatoes.'),
  ('Chana Lamb Chop Masala','22.99','Lamb chops with chickpeas.'),
  ('Goat Curry','23.99','Tender bone-in goat, cooked on slow heat.'),
  ('Saag Gosht','23.99','Goat with creamy spinach.'),
  ('Daal Gosht','23.99','Goat with lentils.'),
 ]),
 ('Seafood', None, '“Big pieces of fresh salmon in a delicious spicy sauce,” one review says of the Goan fish.', [
  ('Fish Goani','23.99','Fillets in a fiery sauce with coconut milk.'),
  ('Bombay Fish Curry','21.99','Bombay-style fish in a light tomato curry.'),
  ('Prawn Masala','24.99','Garlic, ginger, onions and tomatoes.'),
  ('Prawn Vindaloo','24.99','Tomatoes and potatoes in a fiery sauce.'),
  ('Shrimp Jalfrezi','24.99','Bell peppers, onions, tomatoes and cilantro.'),
 ]),
 ('Vegetarian · sixteen mains', 'appetizer-spread.jpg', 'Palak paneer is #3 on Uber Eats with a 96% thumbs-up. Paneer makhani, “consistently amazing.”', [
  ('Palak Paneer','18.99','Fresh homemade cheese in creamy spinach.'),
  ('Paneer Makhani','18.99','Paneer in a creamy tomato sauce.'),
  ('Paneer Tikka Masala','18.99','Grilled paneer with peppers in tomato sauce.'),
  ('Mutter Paneer','18.99','Peas and homemade cheese, North Indian style.'),
  ('Paneer Kadhai','18.99','Onions, peppers, tomatoes and cumin.'),
  ('Malai Kofta Curry','18.99','Cheese and potato croquettes in a light creamy sauce.'),
  ('Dum Aloo','18.99','Potatoes stuffed with cottage cheese, simmered with herbs.'),
  ('Shahi Baingan','17.99','Eggplant in a rich cashew white sauce.'),
  ('Khile Phool','17.99','Cauliflower and potatoes with ginger, tomatoes and peas.'),
  ('Okra do Piaza','17.99','Okra with julienned onions and tomatoes.'),
  ('Vegetable Jalfrezi','17.99','Stir-fried garden vegetables.'),
  ('Navaratna Korma','17.99','Vegetables and dry fruits in a creamy sauce.'),
  ('Chana Masala','16.99','Chickpeas slowly simmered with onions and tomatoes.'),
  ('Yellow Daal','16.99','Lentils with tomatoes, ginger, cumin, onions and garlic.'),
  ('Dal Makhani','16.99','Black lentils and kidney beans in a creamy sauce.'),
  ('Baingan Bharta','16.99','Roasted eggplant with tomatoes, onions and peas.'),
 ]),
 ('Rice &amp; biryani', None, 'Saffron basmati with nuts and raisins.', [
  ('Biryani','16.99–24.99','Vegetable 16.99 · chicken 19.99 · lamb 22.99 · shrimp or goat 24.99.'),
  ('Kashmiri Pulao','12.99','Rice with dry fruits, nuts and saffron.'),
  ('Peas Pulao','11.99','Long-grain basmati with green peas and saffron.'),
 ]),
 ('Breads', 'naan-parantha-breads.jpg', 'Garlic naan and jalapeño-cheese naan are the two reviewers single out.', [
  ('Plain Naan','3.49','Freshly baked, topped with butter.'),
  ('Garlic Naan','3.99','Garlic and butter.'),
  ('Jalapeño &amp; Cheese Naan','4.99','Stuffed with jalapeño and cheese.'),
  ('Kashmiri Naan','5.99','Dried fruits and nuts.'),
  ('Olive Naan','3.99','Green olives, red pepper, olive oil.'),
  ('Night’s Naan','5.99','Chicken and herbs.'),
  ('Keema Naan','5.99','Minced lamb and spices.'),
  ('Roti','3.49','Whole wheat, baked in the clay oven.'),
  ('Aloo Parantha','4.99','Whole wheat, stuffed with lightly spiced potatoes.'),
  ('Pudhina Parantha','5.99','Whole wheat with mint.'),
  ('Onion Kulcha','5.99','Fluffy white bread with onions and bell peppers.'),
  ('Assorted Bread Basket','9.99','Plain naan, roti and garlic naan.'),
 ]),
 ('Soups, salads &amp; sides', None, '', [
  ('Mulligatawny Soup','7.99','Lentil-based with vegetables, mild spicing.'),
  ('Tomato Shorba','7.99','Cream of tomato with herbs and spices.'),
  ('Hariyali Chicken Soup','8.99','Spinach and chicken.'),
  ('Vegetable Soup','7.99','Garden vegetables with herbs.'),
  ('Spinach &amp; Strawberry Salad','8.99','With almonds; add chicken 10.99 or shrimp 12.99.'),
  ('Crunchy Shrimp Salad','11.99','Cabbage, lettuce, carrots, sesame dressing.'),
  ('Spicy Cucumber Chicken Salad','9.99','Cucumbers, onions, peppers, tomatoes.'),
  ('Chef’s Salad','7.99','Fresh greens, broccoli and tomatoes.'),
  ('Raita','3.99','Whipped yogurt with cucumbers and tomatoes.'),
  ('Papad','3.99','Lentil crackers.'),
  ('Mango Chutney','3.99','Sweet mango with aromatic spices.'),
  ('Onion Salad / Achar','2.49 / $1.99','Onions and green chilies / Indian pickle mix.'),
 ]),
 ('Desserts', None, 'Gulab jamun is the one people mention.', [
  ('Gulab Jamun','5.99','Milk dumplings in rose syrup with a touch of cardamom.'),
  ('Rasmalai','5.99','Soft cheese patties in milky cardamom and rose-water syrup.'),
  ('Kulfi','5.99','Rich Indian ice cream; malai, pistachio or mango.'),
  ('Kesari Kheer','5.99','Rice pudding with nuts and saffron.'),
  ('Gajar Halwa','6.99','Carrot pudding with milk and nuts.'),
  ('Dessert Platter','13.99','An assortment.'),
 ]),
]

# ---------------- DISH PAGES (SEO landing pages for high-intent dish queries) ----------------
# Each becomes /menu/<slug>/ with MenuItem + FAQ + Breadcrumb schema.
DISHES = [
 {
  'slug': 'butter-chicken', 'name': 'Butter Chicken (Chicken Makhani)', 'price': '19.99',
  'img': 'butter-chicken.jpg', 'alt': 'Butter chicken (chicken makhani) at Tandoori Nights in Kentlands, Gaithersburg',
  'diet': None,
  'title': 'Butter Chicken (Chicken Makhani) in Gaithersburg | Tandoori Nights',
  'desc': 'Butter chicken at Tandoori Nights, 106 Market St, Kentlands, Gaithersburg MD — tandoor-grilled chicken in a creamy tomato-butter sauce, $19.99. Dine in or order online direct.',
  'lead': 'Butter chicken — chicken makhani — is the dish Gaithersburg orders from us most: tandoor-grilled chicken folded into a creamy tomato and butter sauce, rated 4.7 across 2,000+ orders. It is $19.99, served at 106 Market St in Kentlands.',
  'body': [
    'We start with the same chicken that goes on our tandoori platter — marinated in yogurt and freshly ground spices, then cooked in the clay oven until it takes on a little char. That smokiness is what separates a real butter chicken from a sweet, flat one.',
    'The sauce is built from tomatoes, butter, cream and a warm garam-masala base, simmered until it is glossy and mild enough for the whole table. It is rich without being heavy, and it is the reason people who "don’t usually like Indian food" order it twice.',
  ],
  'serve': 'Best with garlic naan to scoop, or over jeera rice. Ask for it mild, medium or hot.',
  'pairs': [('Garlic Naan', '/menu/garlic-naan/'), ('Chicken Tikka Masala', '/menu/chicken-tikka-masala/'), ('Palak Paneer', '/menu/palak-paneer/')],
  'faq': [
    ('Is butter chicken spicy?', 'No. Butter chicken is mild and creamy by default, which is why it is a favorite for kids and first-timers. We can make it medium or hot on request.'),
    ('What is the difference between butter chicken and chicken tikka masala?', 'Both use tandoor-grilled chicken in a tomato sauce. Butter chicken is milder, richer and more buttery; chicken tikka masala has more onion, spice and a bit of tang. Many people try one of each.'),
  ],
 },
 {
  'slug': 'chicken-tikka-masala', 'name': 'Chicken Tikka Masala', 'price': '19.99',
  'img': 'spread-hero.jpg', 'alt': 'Chicken tikka masala and other North Indian dishes in the Tandoori Nights spread',
  'diet': None,
  'title': 'Chicken Tikka Masala in Gaithersburg | Tandoori Nights',
  'desc': 'Chicken tikka masala at Tandoori Nights, Kentlands, Gaithersburg MD — grilled chicken tikka in a spiced tomato and onion sauce, $19.99. Dine in or order online direct.',
  'lead': 'Chicken tikka masala is our second most-ordered curry: boneless chicken tikka grilled in the tandoor, then simmered in a tomato and onion sauce with a gentle kick. It is $19.99 at 106 Market St in Kentlands, Gaithersburg.',
  'body': [
    'The chicken is marinated and grilled first — that is the "tikka" — so every piece carries char before it ever meets the sauce. We fold it into a tomato-onion gravy finished with cream and garam masala.',
    'It sits a step spicier and tangier than butter chicken, with more body from the onions. If you like a curry with a little more going on, this is the one.',
  ],
  'serve': 'Pairs with garlic naan or basmati rice. Choose your spice level: mild, medium or hot.',
  'pairs': [('Butter Chicken', '/menu/butter-chicken/'), ('Garlic Naan', '/menu/garlic-naan/'), ('Chicken Biryani', '/menu/chicken-biryani/')],
  'faq': [
    ('Is chicken tikka masala the same as butter chicken?', 'They are close cousins. Both start with tandoor-grilled chicken in a tomato sauce, but tikka masala is spicier and more savory with onions, while butter chicken is milder, sweeter and creamier.'),
    ('How spicy is chicken tikka masala?', 'Medium by default, and we adjust it mild or hot to taste.'),
  ],
 },
 {
  'slug': 'chicken-biryani', 'name': 'Chicken Biryani', 'price': '19.99',
  'img': 'spread-hero.jpg', 'alt': 'Chicken biryani and other dishes in the Tandoori Nights spread',
  'diet': None,
  'title': 'Chicken Biryani in Gaithersburg | Tandoori Nights',
  'desc': 'Chicken biryani at Tandoori Nights, Kentlands, Gaithersburg MD — saffron basmati layered with spiced chicken, $19.99. Dine in or order online direct.',
  'lead': 'Chicken biryani is long-grain basmati layered and steamed with spiced chicken, saffron, fried onions and whole spices. It is $19.99 at 106 Market St in Kentlands, Gaithersburg — vegetable, lamb, goat and shrimp biryani are on the menu too.',
  'body': [
    'Biryani is cooked the slow way: par-cooked saffron rice layered over marinated chicken, sealed and steamed so the grains take on the spice without turning mushy. You get whole cardamom, clove and bay in every few bites.',
    'It travels well, which is why it is one of our most-ordered catering trays for offices and parties across the DMV.',
  ],
  'serve': 'Served with raita. Add a curry like butter chicken or palak paneer to share.',
  'pairs': [('Butter Chicken', '/menu/butter-chicken/'), ('Palak Paneer', '/menu/palak-paneer/'), ('Garlic Naan', '/menu/garlic-naan/')],
  'faq': [
    ('Is your chicken biryani spicy?', 'It is moderately spiced and aromatic rather than hot. Served with cooling raita on the side.'),
    ('What kinds of biryani do you have?', 'Vegetable, chicken, lamb, goat and shrimp biryani, plus jeera rice and pulao. Biryani is also available in catering trays.'),
  ],
 },
 {
  'slug': 'tandoori-chicken', 'name': 'Tandoori Chicken', 'price': '17.99',
  'img': 'tandoori-chicken-platter.jpg', 'alt': 'Tandoori chicken on a sizzling platter at Tandoori Nights, Kentlands Gaithersburg',
  'diet': None,
  'title': 'Tandoori Chicken in Gaithersburg | Tandoori Nights',
  'desc': 'Tandoori chicken at Tandoori Nights, Kentlands, Gaithersburg MD — yogurt-and-spice marinated chicken roasted in the clay oven. Half $17.99, whole $29.99.',
  'lead': 'Tandoori chicken is the dish we are named for: bone-in chicken marinated overnight in yogurt and freshly ground spices, then roasted in the clay tandoor until the edges char. Half is $17.99, whole is $29.99, at 106 Market St in Kentlands.',
  'body': [
    'The tandoor runs hot enough to seal the outside fast and keep the inside juicy — a texture you cannot get from an oven. The color comes from the spice marinade, not food dye.',
    'It arrives on a sizzling platter with onions and lemon. It is also one of the leaner things on the menu: grilled, not fried, and no heavy sauce.',
  ],
  'serve': 'Squeeze the lemon over the top; pull the meat into naan or eat it straight off the platter.',
  'pairs': [('Garlic Naan', '/menu/garlic-naan/'), ('Butter Chicken', '/menu/butter-chicken/'), ('Lamb Chops', '/menu/lamb-chops/')],
  'faq': [
    ('Is tandoori chicken healthy?', 'It is one of the lighter options: chicken grilled in the clay oven with a yogurt-and-spice marinade, no frying and no heavy cream sauce.'),
    ('Is tandoori chicken very spicy?', 'It is well-spiced but not hot — the flavor is smoky and tangy from the marinade. We can dial the heat up if you like.'),
  ],
 },
 {
  'slug': 'lamb-chops', 'name': 'Tandoori Lamb Chops', 'price': '24.99',
  'img': 'lamb-chops-tandoori.jpg', 'alt': 'Tandoori lamb chops off the clay oven at Tandoori Nights, Kentlands Gaithersburg',
  'diet': None,
  'title': 'Tandoori Lamb Chops in Gaithersburg | Tandoori Nights',
  'desc': 'Tandoori lamb chops at Tandoori Nights, Kentlands, Gaithersburg MD — marinated with ginger, herbs and freshly ground spices, grilled in the clay oven. $24.99.',
  'lead': 'Our tandoori lamb chops are the dish reviewers single out: marinated with ginger, herbs and freshly ground spices, then grilled in the clay oven. They are $24.99 at 106 Market St in Kentlands, Gaithersburg.',
  'body': [
    'Lamb chops live or die on the marinade and the fire. Ours sit in ginger, garlic and ground spices long enough to tenderize, then go straight onto the tandoor so the fat crisps and the center stays pink.',
    'It is the plate we would point a first-time guest to if they wanted to know what the clay oven can really do.',
  ],
  'serve': 'A squeeze of lemon and garlic naan is all they need; add a dal to round out the plate.',
  'pairs': [('Tandoori Chicken', '/menu/tandoori-chicken/'), ('Garlic Naan', '/menu/garlic-naan/'), ('Butter Chicken', '/menu/butter-chicken/')],
  'faq': [
    ('How are the lamb chops cooked?', 'They are marinated with ginger, herbs and freshly ground spices, then grilled in the tandoor clay oven so the outside chars and the inside stays tender.'),
    ('What goes well with tandoori lamb chops?', 'Garlic naan, a dal or a creamy curry like butter chicken, and jeera rice. They also make a standout appetizer to share.'),
  ],
 },
 {
  'slug': 'palak-paneer', 'name': 'Palak Paneer', 'price': '18.99',
  'img': 'spread-hero.jpg', 'alt': 'Palak paneer and other vegetarian dishes in the Tandoori Nights spread',
  'diet': 'veg',
  'title': 'Palak Paneer in Gaithersburg | Vegetarian Indian | Tandoori Nights',
  'desc': 'Palak paneer at Tandoori Nights, Kentlands, Gaithersburg MD — house-made cheese in creamy spinach, $18.99. One of sixteen vegetarian mains. Dine in or order online.',
  'lead': 'Palak paneer is our most popular vegetarian main: cubes of fresh house-made cheese in a creamy, gently spiced spinach gravy. It is $18.99 at 106 Market St in Kentlands, and one of sixteen vegetarian dishes on the menu.',
  'body': [
    'We cook the spinach down with garlic, ginger and green chili, then blend it smooth and finish it with cream so it stays bright rather than muddy. The paneer is soft and fresh, not rubbery.',
    'It is vegetarian, filling and mild, and it is a staple of our catering trays and lunch buffet.',
  ],
  'serve': 'Scoop with garlic naan or spoon over rice. Pairs well with a chicken curry for a mixed table.',
  'pairs': [('Garlic Naan', '/menu/garlic-naan/'), ('Butter Chicken', '/menu/butter-chicken/'), ('Chicken Biryani', '/menu/chicken-biryani/')],
  'faq': [
    ('Is palak paneer vegetarian?', 'Yes. Palak paneer is fully vegetarian — spinach and fresh house-made cheese. We have sixteen vegetarian mains in all.'),
    ('Is palak paneer vegan?', 'No — it contains paneer cheese and cream. For a vegan spinach or chickpea dish, try chana masala, yellow daal or baingan bharta, which can be made without dairy on request.'),
  ],
 },
 {
  'slug': 'garlic-naan', 'name': 'Garlic Naan', 'price': '3.99',
  'img': 'naan-parantha-breads.jpg', 'alt': 'Fresh garlic naan and breads from the tandoor at Tandoori Nights, Kentlands Gaithersburg',
  'diet': 'veg',
  'title': 'Garlic Naan in Gaithersburg | Tandoori Nights',
  'desc': 'Garlic naan at Tandoori Nights, Kentlands, Gaithersburg MD — soft tandoor-baked flatbread brushed with garlic and butter, $3.99. Twelve breads on the menu.',
  'lead': 'Garlic naan is the bread most tables add first: soft dough slapped onto the wall of the tandoor and baked in seconds, then brushed with garlic and butter. It is $3.99 at 106 Market St in Kentlands, one of twelve breads we bake to order.',
  'body': [
    'Naan has to be baked in a real tandoor to get the blistered top and pillowy middle — that is exactly how ours is made, fresh for each order.',
    'Beyond garlic, the oven turns out plain naan, jalapeño-and-cheese naan, Kashmiri naan, keema naan, roti and stuffed paranthas.',
  ],
  'serve': 'Made for scooping butter chicken, palak paneer or any curry. Order a basket for the table.',
  'pairs': [('Butter Chicken', '/menu/butter-chicken/'), ('Palak Paneer', '/menu/palak-paneer/'), ('Chicken Tikka Masala', '/menu/chicken-tikka-masala/')],
  'faq': [
    ('Is naan vegetarian?', 'Yes — our naan and paranthas are vegetarian. (Keema naan is the exception; it is filled with minced lamb.)'),
    ('Is naan gluten-free?', 'No. Naan and paranthas are made with wheat flour. Most of our curries, tandoori meats, biryani and rice are made without wheat — ask your server about gluten-free options.'),
  ],
 },
 {
  'slug': 'pani-poori', 'name': 'Pani Poori', 'price': '7.99',
  'img': 'pani-puri-shots.jpg', 'alt': 'Pani poori shots at Tandoori Nights, Kentlands Gaithersburg',
  'diet': 'veg',
  'title': 'Pani Poori in Gaithersburg | Indian Street Food | Tandoori Nights',
  'desc': 'Pani poori at Tandoori Nights, Kentlands, Gaithersburg MD — crisp puffed pooris with spiced potato and flavored waters, served as shots. $7.99.',
  'lead': 'Pani poori is the street-food starter people come back for: six crisp, hollow pooris filled with spiced potato and flavored waters, served as shots you crack in one bite. It is $7.99 at 106 Market St in Kentlands, Gaithersburg.',
  'body': [
    'The whole point is the pop — a crisp shell, a burst of tangy-spicy tamarind and mint water, and the soft potato underneath, all at once. It has to be eaten right away, which is why it is a dine-in favorite.',
    'It is one of several chaats we make, alongside aloo tikki, aloo chat papri and raj kachori.',
  ],
  'serve': 'Eat immediately, one shot at a time. A great start before a shared table of curries.',
  'pairs': [('Palak Paneer', '/menu/palak-paneer/'), ('Butter Chicken', '/menu/butter-chicken/'), ('Garlic Naan', '/menu/garlic-naan/')],
  'faq': [
    ('What is pani poori?', 'Pani poori (also called golgappa or puchka) is an Indian street-food snack: hollow, crisp pooris filled with spiced potato and chickpeas, then flavored tangy-spicy water. We serve six as shots.'),
    ('Is pani poori vegetarian?', 'Yes, pani poori is vegetarian. It is one of several vegetarian chaats and starters on our menu.'),
  ],
 },
]
