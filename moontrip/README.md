# 🌌 MoonTrip

**Round trip to the Moon: ₹12,400 only.**

MoonTrip is a cheerful (and wildly subsidised) space-tourism agency. We
sell seats to the Moon, Mars, and everything in between — a lunar
gateway station, a couple of moons of Mars, an orbital hotel with
sixteen sunrises a day, and a heritage tour of the old ISS. This repo is
the starter for MoonTrip's booking site: a working catalogue and fleet
gallery today, and a dozen features for you to build this week.

## Run it

**Prerequisites:** Python 3.12, Node.js 20+.

### API (port 5101)

```bash
# from moontrip/
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python -m api
```

### Web (port 5201)

```bash
# from moontrip/web/
npm install
npm run dev
```

Open http://localhost:5201. The dev server proxies `/api` requests to
the Flask API on port 5101, so both need to be running.

### Tests

```bash
# from moontrip/, with the virtualenv active
pytest
```

## How the code is organised

```
moontrip/
  logic/    pure functions — pricing, refunds, seating, etc.
  api/      Flask routes + api/store.py (the only code that touches data/)
  web/      Vite + React frontend
  data/     JSON "database"
  tests/    pytest tests for the baseline logic
```

Request flow for a typical feature:

```
Browser (web/)
   │  fetch("/api/...")
   ▼
Flask route (api/<task>_routes.py)
   │  store.load("...")
   ▼
data/*.json
   │
   ▼
logic function (logic/<task>.py)   <- pure, no I/O
   │  return value
   ▼
Flask route -> jsonify(...) -> Browser
```

## Coding rules

These aren't style preferences — a browser extension grades your pull
requests by inspecting `logic/` functions directly, and it can only do
that if every file follows these rules.

1. **`logic/` functions are pure.** They take plain data in (dicts,
   lists, strings, numbers, booleans) and return plain data out. No
   reading files, no `datetime.now()`, no `random`, no network calls.
   Anything date-dependent is a parameter.

   ```python
   # good
   def is_expired(expires, today):
       return today > expires

   # bad — reads the clock itself, not testable, not gradable
   from datetime import date
   def is_expired(expires):
       return date.today().isoformat() > expires
   ```

2. **Only `api/` touches `data/*.json`,** through `api/store.py`
   (`store.load(name)` / `store.save(name, data)`). A route loads data,
   calls a logic function, returns the result.

   ```python
   # good — route in api/, logic in logic/
   @app.route("/api/refunds/quote", methods=["POST"])
   def refund_quote_route():
       booking = store.load("bookings")[0]
       return jsonify(refund_amount(booking, request.json["cancel_date"]))

   # bad — logic/ file reading a file directly
   def refund_amount(booking_id, cancel_date):
       bookings = json.load(open("data/bookings.json"))  # NO
       ...
   ```

3. **Top-level functions only.** No classes, no nested `def`, no
   `lambda` assigned to a variable. Standard library imports only in
   `logic/`.

4. **Self-contained.** A function can't read a module-level variable.
   Constants live inside the function body or as default parameter
   values: `def f(mass_kg, G=6.674e-11): ...`.

5. **Every task function has real logic** — branches, loops, boundary
   checks, lookups. If your implementation is a one-liner, re-read the
   rules; you're probably missing a case.

6. **No logic in `web/`.** Components display what the API returns; they
   don't compute prices, refunds, or anything else.

## Warm-ups (don't start the game)

These touch shared baseline files directly — that's fine, they're small
enough not to trigger the game.

- **W1 — Navbar polish.** Add active-link highlighting to
  `web/src/components/Nav.jsx` (the current route's link should look
  visually distinct) and add a simple footer to the app shell in
  `web/src/App.jsx`.
- **W2 — About page.** Add a new "Our mission" page (`web/src/pages/About.jsx`)
  telling MoonTrip's story, and link to it from the navbar.

## Tasks

| ID | Feature | Difficulty | Files |
|---|---|---|---|
| M1 | Round-trip price calculator | ★★ | `logic/pricing.py`, `api/pricing_routes.py`, `web/src/tasks/PriceCalculator.jsx` |
| M2 | Mars launch windows | ★★ | `logic/launch_windows.py`, `api/launch_windows_routes.py`, `web/src/tasks/LaunchWindowBadge.jsx` |
| M3 | Booking history | ★ | `logic/booking_history.py`, `api/booking_history_routes.py`, `web/src/tasks/BookingHistory.jsx` |
| M4 | Cancellation & refunds | ★★ | `logic/refund.py`, `api/refund_routes.py`, `web/src/tasks/RefundCalculator.jsx` |
| M5 | Seat allocation | ★★★ | `logic/seating.py`, `api/seating_routes.py`, `web/src/tasks/SeatMap.jsx` |
| M6 | Mission status tracker | ★★ | `logic/mission_status.py`, `api/mission_status_routes.py`, `web/src/tasks/MissionStatus.jsx` |
| M7 | Promo codes | ★★★ | `logic/promos.py`, `api/promos_routes.py`, `web/src/tasks/PromoCode.jsx` |
| M8 | Itinerary validator | ★★ | `logic/itinerary.py`, `api/itinerary_routes.py`, `web/src/tasks/ItineraryValidator.jsx` |
| M9 | Luggage fees | ★ | `logic/luggage.py`, `api/luggage_routes.py`, `web/src/tasks/LuggageEstimator.jsx` |
| M10 | Passenger checks | ★★ | `logic/passengers.py`, `api/passengers_routes.py`, `web/src/tasks/PassengerChecks.jsx` |
| M11 | Moon Miles loyalty | ★★ | `logic/loyalty.py`, `api/loyalty_routes.py`, `web/src/tasks/LoyaltyCard.jsx` |
| M12 | Mission control stats | ★★ | `logic/trip_stats.py`, `api/trip_stats_routes.py`, `web/src/tasks/MissionStats.jsx` |

Each task's three files already exist as stubs — the route is mounted
(it just returns HTTP 501) and the UI slot is already on its page (it
just shows a "coming soon" card). Full rules and worked examples are in
each stub's docstring; the summaries below are quick reference.

### M1 — Round-trip price calculator (★★)

*As a traveller, I want to see the full round-trip price for my party
before I book.*

- **Logic** (`logic/pricing.py`): `trip_price(destination, passengers, cabin, travel_date)`.
  Cabin multipliers: economy 1.0, business 1.8, lunar_suite 3.0. Age
  discounts: child (<12) 50%, senior (≥65) 80%. Round trip = 2× one-way
  fare. Seasonal surcharge from `season_surcharge_pct[month]` applies
  after age discounts.
- **API**: `POST /api/price`.
- **UI**: a calculator on the Book page with a line-by-line breakdown.
- **Example**: Moon, base ₹6,200 one-way, 2 adults, economy, a month
  with 0% surcharge → `total_inr` 24,800.
- **Done when:** the form calculates a correct breakdown for at least
  one child, one senior, and one surcharge month, and the route returns
  the same numbers as the logic function.

### M2 — Mars launch windows (★★)

*As a traveller, I want to know when the next launch window opens.*

- **Logic** (`logic/launch_windows.py`): `next_launch_window(windows, today)`,
  `is_window_open(window, date)`. A window is open if
  `opens ≤ date ≤ closes`. The next window is the earliest one with
  `closes ≥ today`; if already open, `days_until` is 0. `None` if there
  are no windows.
- **API**: `GET /api/destinations/<id>/next-window`.
- **UI**: "Next window in N days" badge on destination cards.
- **Done when:** Mars (seeded with no windows) shows a sensible empty
  state, and a destination with an open window shows "open now".

### M3 — Booking history (★)

*As a traveller, I want to filter and sort my past and upcoming trips.*

- **Logic** (`logic/booking_history.py`): `filter_bookings(bookings, user_id, status, from_date)`,
  `sort_bookings(bookings, key, descending)`. `status=None` means any
  status; `from_date` is inclusive. Sort keys: `launch_date`,
  `total_inr`, `destination`. Ties broken by booking id.
- **API**: `GET /api/users/<id>/bookings`.
- **UI**: filterable, sortable table on My trips.
- **Done when:** filtering by status and sorting by each key produce
  correct order, with ties broken by id.

### M4 — Cancellation & refunds (★★)

*As a traveller, I want to know what I'll get back before I cancel.*

- **Logic** (`logic/refund.py`): `refund_amount(booking, cancel_date)`.
  Tiers by days before launch: >30 → 90%, 8–30 → 50%, 1–7 → 10%, launch
  day+ → 0%. Fee = max(₹500, 2% of total), capped at the refund.
- **API**: `POST /api/refunds/quote`.
- **UI**: refund quote panel on a booking.
- **Done when:** all four tiers produce the documented percentages, and
  the fee never pushes the refund negative.

### M5 — Seat allocation (★★★)

*As a traveller, I want my group seated together where possible.*

- **Logic** (`logic/seating.py`): `allocate_seats(seat_map, group_size)`.
  Prefer one row with `group_size` adjacent free seats (first row first,
  leftmost first); otherwise use the fewest rows possible. `None` if the
  group can't fit anywhere.
- **API**: `POST /api/craft/<id>/allocate`.
- **UI**: seat map with the allocated seats highlighted.
- **Done when:** a group that fits in one row gets adjacent seats, and a
  group that doesn't still gets seated across the fewest rows possible.

### M6 — Mission status tracker (★★)

*As a fan, I want to watch a mission's progress in real time.*

- **Logic** (`logic/mission_status.py`): `mission_phase(timeline, hours_since_launch)`.
  The phase is the last timeline entry whose `starts_at_hour ≤ h`.
  Before launch → `"pre-launch"`. After the last phase → `"complete"`.
- **API**: `GET /api/missions/<id>/status?h=`.
- **UI**: progress bar with phase labels on Mission control.
- **Done when:** hours before 0, during each phase, and past the final
  phase all show the correct label and a progress percentage that never
  leaves 0–100.

### M7 — Promo codes (★★★)

*As a traveller, I want to stack a coupon into my checkout total.*

- **Logic** (`logic/promos.py`): `apply_promos(price_inr, codes, promos, today)`.
  At most one percent code applies (the best one); flat codes stack.
  Skip expired codes and codes below `min_spend_inr`, with a reason
  each. Total never goes below ₹0.
- **API**: `POST /api/promos/apply`.
- **UI**: promo code field in the checkout summary on the Book page.
- **Done when:** an expired code, an under-minimum code, and a valid
  code all produce the right accept/reject result, and two percent codes
  entered together only apply the better one.

### M8 — Itinerary validator (★★)

*As a traveller, I want warnings before I overbook my trip.*

- **Logic** (`logic/itinerary.py`): `validate_itinerary(activities, trip_start, trip_end)`.
  Flags: activities outside the trip dates, overlapping activities on
  the same day, and more than 2 moonwalks (`type: "eva"`) on one day.
- **API**: `POST /api/itinerary/validate`.
- **UI**: itinerary builder listing validation errors.
- **Done when:** each of the three error types is triggered by at least
  one test case, and a valid itinerary returns no errors.

### M9 — Luggage fees (★)

*As a traveller, I want to know my luggage fee before I pack.*

- **Logic** (`logic/luggage.py`): `luggage_fee(items, cabin)`. Free
  allowance: economy 5kg, business 10kg, lunar_suite 20kg. Excess: first
  5kg at ₹900/kg, then ₹1,500/kg. Medical items are always free.
- **API**: `POST /api/luggage/fee`.
- **UI**: luggage estimator.
- **Done when:** an under-allowance bag, an over-allowance bag crossing
  both excess tiers, and a medical item all price correctly.

### M10 — Passenger checks (★★)

*As a traveller, I want to know if a passenger can't fly before
checkout.*

- **Logic** (`logic/passengers.py`): `validate_passengers(passengers, travel_date)`.
  Age 3–80 only; age ≥70 needs `medical_clearance`; every passenger
  needs a passport valid >180 days past `travel_date`; names required.
- **API**: `POST /api/passengers/validate`.
- **UI**: per-passenger inline errors on the Book page.
- **Done when:** each rule produces its own error message, keyed to the
  right passenger index.

### M11 — Moon Miles loyalty (★★)

*As a frequent flyer, I want to see my tier and progress.*

- **Logic** (`logic/loyalty.py`): `loyalty_status(bookings, user_id, today)`.
  ₹10 spent = 1 mile, only on "completed" bookings in the trailing 365
  days. Tiers: Crater <5,000, Orbit <20,000, Apollo ≥20,000. Cancelled
  bookings earn nothing.
- **API**: `GET /api/users/<id>/loyalty`.
- **UI**: loyalty tier card with progress to the next tier.
- **Done when:** a user with only cancelled bookings shows 0 miles, and
  tier boundaries land on the correct side.

### M12 — Mission control stats (★★)

*As the ops team, I want a dashboard of how the business is doing.*

- **Logic** (`logic/trip_stats.py`): `trip_stats(bookings, destinations)`.
  Revenue per destination (excluding cancelled bookings), bookings per
  status, average group size, and the most popular destination (ties
  broken alphabetically).
- **API**: `GET /api/stats`.
- **UI**: stat tiles plus revenue-by-destination bars.
- **Done when:** cancelled bookings are excluded from revenue but
  counted in `bookings_by_status`, and a tie in popularity resolves
  alphabetically.

## Suggested split

A team of four could divide the twelve tasks roughly by page:

- **Person A** — M1, M9, M10 (Book page: pricing, luggage, passengers)
- **Person B** — M5, M7, M8 (Book page: seating, promos, itinerary)
- **Person C** — M3, M4, M11 (My trips)
- **Person D** — M2, M6, M12 (Destinations + Mission control)

## Stretch

Finished early? Propose your own MoonTrip feature and build it as a new
task triple (`logic/<slug>.py`, `api/<slug>_routes.py`,
`web/src/tasks/<Name>.jsx`), following the same coding rules and task
isolation as M1–M12.
