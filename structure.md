# Study Project Generation Prompt

**Version 1 · 2026-09-10 · for the AICodeQuest week-long training study**
(`docs/STUDY-PROTOCOL.md` draft 4, `reports/phase-44-basis.md`).

## How to use this document

This is a **prompt** for an AI coding tool. It generates four starter
projects in one repository. Use it like this:

1. Give the tool **Part A (shared brief) plus ONE project section from
   Part B** per run. Generate one project at a time; the root files come
   from the first run.
2. Check each generated project against **A12 (acceptance checklist)**.
3. The study team fills the placeholders below, then pushes to the fresh
   repository.
4. Complete **Part C (dry run)** before any participant sees the repo.

**Placeholders the study team fills in:**

| Placeholder | Meaning |
|---|---|
| `[PASS_MARK]` | e.g. "find at least 2 of the 4 bugs" — set after the pilot |
| `[EXTENSION_INSTALL]` | How to install the AICodeQuest Chrome extension and sign in |
| `[STUDY_DATES]` | Day 0 to day 7 dates |
| `[SUPPORT_CONTACT]` | Who to contact during the study |
| `[REPO_URL]` | URL of the fresh repository |

---

# PART A — Shared brief (give this with every project)

## A1. Context

You are building a **starter codebase** for a week-long software
engineering training study. Teams of four developers will fork this
repository, choose one of four themed projects, and add features to it
**using an AI coding assistant**. Each feature is raised as a pull request.
A browser extension then runs a short game about the code they submitted:
it plants bugs to find, asks them to predict outputs, and asks them to
plant a bug of their own.

Your job is to produce a project that is **polished, fun and runnable on
day one**, with a clearly defined list of features left for the
participants. **Do not implement the participant tasks.** Build everything
around them so that each task is self-contained and well specified.

## A2. Repository layout (mandatory — the game depends on it)

```
<repo>/
  README.md                      ← root README (A10.1)
  CONTRIBUTING.md                ← PR workflow (A10.3)
  .github/PULL_REQUEST_TEMPLATE.md
  .gitignore
  LICENSE                        ← MIT
  moontrip/
  blackhole-explorer/
  rocketmart/
  bhasha-bharat/
```

Inside **every** project, exactly these top-level folders:

```
<project>/
  README.md        ← project README (A10.2)
  logic/           ← pure business logic: ALL graded task code lives here
  api/             ← thin HTTP layer + JSON data access
  web/             ← frontend
  data/            ← JSON files (the only storage — no database)
  tests/           ← tests for BASELINE logic only
```

**Never nest these** (no `server/logic/`, no `backend/api/`). The game
counts changes per top-level folder inside a project, and a feature must
touch `logic/`, `api/` and `web/`. Nesting would merge those into one group
and the game would never start.

## A3. Stack and ports

| Project | logic/ + api/ | web/ | API port | Web port |
|---|---|---|---|---|
| moontrip | Python 3.12, Flask | Vite + React (JavaScript, JSX) | 5101 | 5201 |
| blackhole-explorer | Python 3.12, Flask | Vite + vanilla JavaScript + Three.js | 5102 | 5202 |
| rocketmart | Java 17, Maven, JDK `com.sun.net.httpserver` (Gson allowed in `api/` ONLY) | Vite + React (JavaScript, JSX) | 5103 | 5203 |
| bhasha-bharat | Python 3.12, Flask | Vite + React (JavaScript, JSX) | 5104 | 5204 |

- **No TypeScript, no Vue, no Angular, no CSS frameworks that need a build
  plugin.** Plain CSS with custom properties.
- **Pin exact versions** in `requirements.txt`, `package.json` and
  `pom.xml`.
- The Vite dev server proxies `/api` to the project's API port.
- Commands must work on **Windows and Linux**; READMEs give both where they
  differ.
- Python: `api/` is a package started with `python -m api` from the
  project root, which serves on the API port.
- Java: `pom.xml` at `rocketmart/`. Its `sourceDirectory` is the project
  root, compiling only `logic/**` and `api/**`, so that `logic/` and `api/`
  stay top-level folders. Packages are `logic` and `api`. Started with
  `mvn -q compile exec:java`.

## A4. Architecture rules (apply to every file in `logic/`)

These rules make participant code gradable by the game. Follow them
exactly, and write them into each project README (A10.2) so participants
follow them too.

1. **Functional core, imperative shell.** Logic functions take plain data
   as arguments and return plain data. They never read or write files,
   environment variables, the network, the clock or randomness.
2. **Only `api/` touches `data/*.json`**, through a small `store` module
   (`api/store.py` / `api/Store.java`). A route handler loads the JSON,
   calls a logic function, and returns the result.
3. **Python:** top-level `def` functions only — no classes, no nested
   functions, no lambdas stored in variables. Arguments and return values
   are `dict`, `list`, `str`, `int`, `float`, `bool` or `None`. Standard
   library imports only.
4. **Java:** each logic file is one `public final class` with a private
   constructor and `public static` methods. Small `record` types used by
   those methods are declared **inside that same class**. Imports from
   `java.util` / `java.time` only. No Gson, no I/O.
5. **Self-contained functions.** A function must not read module-level
   variables. Constants go inside the function body or become default
   parameter values (e.g. `def f(mass_kg, G=6.674e-11)`).
6. **Deterministic.** Anything time-dependent receives `today` (ISO date
   string `YYYY-MM-DD`) as a parameter.
7. **Every task function has real logic** — branches, loops, boundaries,
   lookups. No task is a one-line getter.
8. **No logic in `web/`** beyond presentation. Calculations are done by the
   API, never in a React component.

## A5. Task isolation (mandatory)

Every participant task owns **its own three files**, and nothing else needs
editing:

```
<project>/logic/<task_slug>.py        (Java: logic/<TaskName>.java)
<project>/api/<task_slug>_routes.py   (Java: api/<TaskName>Handler.java)
<project>/web/src/tasks/<TaskName>.jsx   (blackhole-explorer: .js)
```

- **The generator pre-creates all three files for every task as stubs**
  (A6), and **pre-registers** them: every task route is already mounted
  and every task UI slot is already on its page. A participant therefore
  never edits a shared file for a task. This avoids merge conflicts inside
  a team.
- **Never put baseline (already-implemented) code in a task file**, and
  never put task code in a baseline file.
- A task may add records to `data/*.json`. Those edits do not count toward
  starting the game.
- Warm-up tasks (W1, W2) are the only tasks that edit shared baseline UI
  files.

## A6. Stub format

**Python logic stub** (`logic/refund.py`):

```python
# ============================================================
# TASK M4 — Cancellation & tiered refund policy
# Files for this task:
#   logic/refund.py            <- this file
#   api/refund_routes.py
#   web/src/tasks/RefundCalculator.jsx
# TODO(M4):
#   [ ] implement refund_amount() in this file
#   [ ] implement the POST /api/refunds/quote route
#   [ ] build the RefundCalculator panel
#   [ ] use an AI assistant; tag its lines honestly in the PR
# ============================================================


def refund_amount(booking, cancel_date):
    """Return the refund for cancelling `booking` on `cancel_date`.

    booking: {"total_inr": int, "launch_date": "YYYY-MM-DD", ...}
    cancel_date: "YYYY-MM-DD"
    Returns {"refund_inr": int, "fee_inr": int, "tier": str}

    Rules: <copied from the task spec>
    Examples: <copied from the task spec>
    """
    raise NotImplementedError("TODO(M4)")
```

**Route stub:** a registered route that returns HTTP 501 with
`{"error": "not_implemented", "task": "M4"}` and a `TODO(M4)` comment
describing the request and response shape.

**Java stub:** the same header as a `/* */` block. Every method throws
`UnsupportedOperationException("TODO(R3)")`; records are already declared.

**UI stub:** the component renders the shared `TaskPlaceholder` card
("🚧 Coming soon — M4 Cancellation & refunds") inside its page slot. Its
header comment lists the task files and a TODO checklist, and describes the
intended UI in two or three sentences.

## A7. TODO header in every file

Every source file starts with a header comment:

- **Task files:** the block shown in A6.
- **Baseline files:** `BASELINE — implemented by the study team. Do not
  modify for tasks M1–M12.`, plus which warm-up tasks (if any) edit this
  file.
- **Root and project READMEs** carry the full task list (A10).

## A8. What the generator IMPLEMENTS (baseline)

For each project:

- **The complete visual shell:** themed layout, navigation, landing page,
  all pages that host task slots, responsive design, dark space-style
  theme (A9).
- **2–3 baseline features, fully working end to end** (listed per
  project) — logic function, route, UI and tests. These are the example
  participants imitate.
- **Seed data** in `data/*.json`: realistic, themed, with the counts listed
  per project.
- **A shared UI kit** in `web/src/ui/`: `Card`, `Button`, `Stat`, `Table`,
  `Field`, `Badge`, `TaskPlaceholder`, and `api.js` with
  `getJson`/`postJson`. Participants' task UIs stay small and consistent.
- **`api/store.py` (or `Store.java`):** `load(name)` and `save(name, data)`
  for `data/<name>.json`.
- **Tests** for the baseline logic (pytest / JUnit 5). None for tasks.

## A9. Visual direction

Each project has its own identity (Part B), but all share these rules:

- Dark background, one accent colour, and one display font plus one body
  font from Google Fonts, with a system fallback stack.
- All artwork is **CSS, SVG or code-generated**: no downloaded images, no
  copyrighted assets.
- Motion is subtle and respects `prefers-reduced-motion`.
- Every page looks finished even where task slots show placeholders.

## A10. Documentation

### A10.1 Root `README.md`

Sections, in this order:

1. **Welcome** — the four projects, one line and an emoji each, in a
   playful tone.
2. **The week** — `[STUDY_DATES]`: day 0 onboarding, days 1–5 build,
   day 6 demo day, day 7 wrap-up.
3. **Get started**
   1. Fork `[REPO_URL]`, and clone your fork.
   2. Pick your team's project and follow its README to run it.
   3. Install the extension: `[EXTENSION_INSTALL]`.
4. **The rules**
   - **Use an AI coding assistant** (Copilot, ChatGPT, Claude, anything)
     to write your task code. That is the point of the study. Note which
     assistant you used in your pull request.
   - **One task = one pull request.** Don't combine tasks, and don't split
     one task across several PRs.
   - **Tag honestly.** When the extension asks which parts an AI wrote,
     answer truthfully. There is no penalty either way.
   - **Keep the game to yourself.** Don't share bugs, answers or
     screenshots of the game with teammates.
   - Follow the coding rules in your project README.
5. **How the game works** — include verbatim:

   > **When does the game start?**
   > When you open a pull request for a **feature-sized** change that
   > touches your project's logic, API and web code together, the extension
   > pauses the *Create pull request* button and starts the game. Every
   > numbered task (M1, B1, R1, L1, …) is designed to start it. Warm-up
   > tasks, data-only edits (`data/*.json`), documentation and small tweaks
   > do not.
   >
   > **What happens?**
   > 1. **Tag your code.** Mark which parts of your change an AI assistant
   >    wrote.
   > 2. **Defend (4 rounds).** We plant a bug in one of *your* functions.
   >    Find it and fix it.
   > 3. **Understand (5 questions).** Predict what one of your functions
   >    returns for a given input.
   > 4. **Attack (4 rounds).** Plant a bug of your own and see whether our
   >    AI can repair it.
   >
   > It takes about 10–15 minutes. To pass, `[PASS_MARK]`. If you don't
   > reach the pass mark, you can play another round with fresh bugs. When
   > you pass, the *Create pull request* button unlocks.
   >
   > **Rewards.** Every bug you catch counts. Badges, streaks and
   > celebrations are waiting — check the Badges page in the extension.

6. **Help** — `[SUPPORT_CONTACT]`, and a troubleshooting table: app
   doesn't start; port in use; the game didn't start (was it a warm-up or
   data-only change?); the extension says I'm signed out.

**Do not state numeric thresholds** for starting the game, in any
document. (Exact numbers invite splitting or padding pull requests.)

### A10.2 Project `README.md`

1. Title, tagline, and a one-paragraph story of the world.
2. **Run it** — prerequisites; API and web commands for Windows and Linux;
   the URLs.
3. **How the code is organised** — `logic/` / `api/` / `web/` / `data/` /
   `tests/`, with a request-flow diagram (ASCII).
4. **Coding rules** — A4 rewritten for participants, with a good and a bad
   example each.
5. **Warm-ups (don't start the game)** — W1, W2.
6. **Tasks** — a table (ID · feature · difficulty ★–★★★ · files), then per
   task: user story, what to build in each of the three files, rules,
   examples, and a "done when…" checklist.
7. **Suggested split** — how a team of four might divide the tasks.
8. **Stretch** — teams that finish may propose their own feature, built as
   a new triple of task files following the same rules.

### A10.3 `CONTRIBUTING.md` and PR template

- **Workflow:** `git checkout -b m4-refunds` → build with your AI assistant
  → run the app and tests → push to your fork → open *Compare & pull
  request* → play the game → create the pull request → a teammate reviews
  and merges.
- **PR template fields:** Task ID; AI assistant(s) used; what you built;
  how you tested it; screenshots (optional).

## A11. Don'ts

- Don't implement any M/B/R/L task, even partially — stubs only.
- Don't put helper logic for tasks in baseline files.
- Don't add a database, ORM, auth system or state library.
- Don't use TypeScript, `.vue` or `.tsx` anywhere.
- Don't use module-level mutable state in `logic/`.
- Don't mention the game's internal thresholds.

## A12. Acceptance checklist (the generator verifies each project)

- [ ] `api` and `web` start with the README commands on a clean machine;
      the landing page renders with no console errors.
- [ ] Baseline features work end to end; baseline tests pass.
- [ ] Every task has exactly its three stub files, pre-registered. The
      route returns 501 and the UI shows `TaskPlaceholder`.
- [ ] No task function body contains an implementation.
- [ ] Every `logic/` file follows A4. No nested functions, no module-level
      variables read by functions, stdlib only.
- [ ] Only `logic/`, `api/`, `web/`, `data/` and `tests/` exist inside the
      project folder — nothing nested deeper at the top level.
- [ ] Every file has its A7 header; the READMEs follow A10.
- [ ] Seed data matches the counts listed for the project.

---

# PART B — Projects

Notation: difficulty ★ easy, ★★ medium, ★★★ hard. In the task tables,
"Logic" is the task's `logic/` file and functions, "API" its route, and
"UI" what its component shows. **Put every rule and example below into
the stub's docstring.**

---

## B1. 🌌 MoonTrip — *"Round trip to the Moon: ₹12,400 only."*

**World.** A cheerful (and wildly subsidised) space-tourism agency selling
trips to the Moon, Mars and the orbital hotels in between.

**Look.** Deep navy, lunar-silver text, one warm "booking orange" accent.
Display font Orbitron (fallback: system sans). A hero with a CSS/SVG Moon
and a slow star parallax.

**Pages.** Home · Destinations · Destination detail · Book · My trips ·
Mission control · Deals.

**Data** (`data/`):

| File | Seed |
|---|---|
| `destinations.json` | 6 destinations: Moon, Lunar Gateway, Mars (added by M2 — seed without windows), Phobos, Orbital Hotel Aurora, ISS Heritage. Fields: `id, name, tagline, base_price_inr, travel_days, season_surcharge_pct` (by month), `launch_windows` (list of `{opens, closes}`) |
| `spacecraft.json` | 4 craft with `seats` layout rows |
| `bookings.json` | 25 bookings across 5 users, with statuses `upcoming`/`completed`/`cancelled` |
| `promos.json` | 6 codes with type (`percent`/`flat`), value, `min_spend_inr`, `expires` |
| `missions.json` | 3 mission timelines (list of `{phase, starts_at_hour}`) |

**Baseline (implemented):**

1. Destination catalogue with sorting —
   `logic/catalogue.py: list_destinations(destinations, sort_by)`.
2. Destination detail page.
3. Spacecraft gallery.

**Warm-ups:**

- **W1** Navbar with active-link highlight, plus a footer.
- **W2** About page: "Our mission".

**Tasks:**

| ID | Feature | ★ | Logic (`logic/…`) | API | UI |
|---|---|---|---|---|---|
| M1 | Round-trip price calculator | ★★ | `pricing.py: trip_price(destination, passengers, cabin, travel_date)` | `POST /api/price` | Calculator on the Book page with a line-by-line breakdown |
| M2 | Mars launch windows | ★★ | `launch_windows.py: next_launch_window(windows, today)`, `is_window_open(window, date)` | `GET /api/destinations/<id>/next-window` | "Next window in N days" badge on destination cards |
| M3 | Booking history | ★ | `booking_history.py: filter_bookings(bookings, user_id, status, from_date)`, `sort_bookings(bookings, key, descending)` | `GET /api/users/<id>/bookings` | Filterable, sortable table on My trips |
| M4 | Cancellation & refunds | ★★ | `refund.py: refund_amount(booking, cancel_date)` | `POST /api/refunds/quote` | Refund quote panel on a booking |
| M5 | Seat allocation | ★★★ | `seating.py: allocate_seats(seat_map, group_size)` | `POST /api/craft/<id>/allocate` | Seat map with the allocated seats highlighted |
| M6 | Mission status tracker | ★★ | `mission_status.py: mission_phase(timeline, hours_since_launch)` | `GET /api/missions/<id>/status?h=` | Progress bar with phase labels on Mission control |
| M7 | Promo codes | ★★★ | `promos.py: apply_promos(price_inr, codes, promos, today)` | `POST /api/promos/apply` | Promo code field in the checkout summary |
| M8 | Itinerary validator | ★★ | `itinerary.py: validate_itinerary(activities, trip_start, trip_end)` | `POST /api/itinerary/validate` | Itinerary builder listing validation errors |
| M9 | Luggage fees | ★ | `luggage.py: luggage_fee(items, cabin)` | `POST /api/luggage/fee` | Luggage estimator |
| M10 | Passenger checks | ★★ | `passengers.py: validate_passengers(passengers, travel_date)` | `POST /api/passengers/validate` | Per-passenger inline errors on the Book page |
| M11 | Moon Miles loyalty | ★★ | `loyalty.py: loyalty_status(bookings, user_id, today)` | `GET /api/users/<id>/loyalty` | Loyalty tier card with progress to the next tier |
| M12 | Mission control stats | ★★ | `trip_stats.py: trip_stats(bookings, destinations)` | `GET /api/stats` | Stat tiles plus revenue-by-destination bars |

**Rules and examples (copy into the docstrings):**

- **M1** — Cabin multipliers: economy 1.0, business 1.8, lunar_suite 3.0.
  Child (age < 12) pays 50%; senior (≥ 65) pays 80%. Seasonal surcharge is
  `season_surcharge_pct[month]`, applied after the discounts. Round trip =
  2 × one-way base. Returns a breakdown dict plus `total_inr`.
  *Example:* Moon, base ₹6,200 one-way, 2 adults, economy, January (0%)
  → `total_inr` 24,800.
- **M2** — A window is open if `opens ≤ date ≤ closes`. The next window is
  the earliest one with `closes ≥ today`; if it is already open, report
  `days_until = 0`. Return `None` if there are no windows.
- **M3** — `status=None` means all statuses; `from_date` is inclusive.
  Sort keys: `launch_date`, `total_inr`, `destination`. Ties are broken by
  booking id.
- **M4** — Days before launch: > 30 → 90% refund; 8–30 → 50%; 1–7 → 10%;
  launch day or later → 0. The fee is the larger of ₹500 and 2% of the
  total, and is never more than the refund.
- **M5** — Prefer one row with `group_size` adjacent free seats (`"."` =
  free, `"X"` = taken), first row first, leftmost first. Otherwise, the
  fewest rows possible. `None` if the group cannot fit.
- **M6** — The phase is the last one whose `starts_at_hour ≤ h`.
  Progress % is measured within the whole timeline. Before launch →
  `"pre-launch"`; after the last phase → `"complete"`.
- **M7** — At most one percent code applies (the best one); flat codes
  stack. Skip expired codes and codes whose `min_spend_inr` is not met,
  returning a reason per rejected code. The total never goes below ₹0.
- **M8** — Errors: overlapping activities; an activity outside the trip
  dates; more than 2 moonwalks (`type: "eva"`) on one day. Return an
  ordered list of messages.
- **M9** — Free allowance: economy 5 kg, business 10 kg, lunar_suite
  20 kg. Excess: first 5 kg at ₹900/kg, then ₹1,500/kg. Items marked
  `"medical": true` are free.
- **M10** — Age 3–80 allowed; age ≥ 70 needs `medical_clearance`; every
  passenger needs a passport expiring > 180 days after `travel_date`;
  names are required. Return errors keyed by passenger index.
- **M11** — Miles = ₹10 spent = 1 mile, on completed bookings in the
  trailing 365 days. Tiers: Crater < 5,000 ≤ Orbit < 20,000 ≤ Apollo.
  Cancelled bookings earn nothing.
- **M12** — Revenue per destination (non-cancelled only), bookings per
  status, average group size, and the most popular destination (ties
  broken alphabetically).

---

## B2. 🕳️ BlackHole Explorer — *"Get close. Not too close."*

**World.** An interactive observatory for exploring real and fictional
black holes: event horizons, bent starlight, slowed clocks and
spaghettification.

**Look.** Pure black background; accretion-disk orange-to-white gradients
as the accent; display font Space Grotesk. Full-screen Three.js canvas
with a glassy side panel.

**Pages** (single-page app with panels): Observatory (3D scene) ·
Catalogue · Object detail · Observation log · Learn.

**Data** (`data/`):

| File | Seed |
|---|---|
| `objects.json` | 12 objects — Sagittarius A*, M87*, Cygnus X-1, Gaia BH1, TON 618, plus 7 others (include 2 neutron stars and 1 white dwarf). Fields: `id, name, kind, mass_solar, radius_km, distance_ly, ra_deg, dec_deg, spin` |
| `observations.json` | 40 entries: `{object_id, date, brightness, notes}` |

**Baseline (implemented):**

1. 3D scene: black sphere, a shader-based accretion disk, a star field,
   orbit controls.
2. Catalogue list plus detail panel — `logic/catalogue.py:
   get_object(objects, object_id)`, `list_objects(objects, kind)`.
3. Observation log viewer (a plain list).

**Warm-ups:**

- **W1** Top bar with a units toggle (km / solar radii).
- **W2** Learn page: "What is a black hole?".

**Tasks** (UI files are `web/src/tasks/<Name>.js`, vanilla JS modules that
mount into a slot):

| ID | Feature | ★ | Logic (`logic/…`) | API | UI |
|---|---|---|---|---|---|
| B1 | Event-horizon size | ★ | `horizon.py: schwarzschild_radius(mass_solar)` | `GET /api/objects/<id>/horizon` | Scales the horizon sphere; shows km and "× Earth radius" |
| B2 | Time dilation | ★★ | `time_dilation.py: dilation_factor(r_km, rs_km)`, `clock_table(rs_km, radii_km)` | `GET /api/objects/<id>/clocks` | Two ticking clocks, near and far |
| B3 | Classify & add object | ★★ | `classify.py: classify_object(mass_solar, radius_km)` | `POST /api/objects/classify` | "Add object" form showing the classification |
| B4 | Escape velocity & orbits | ★★ | `orbits.py: escape_velocity(mass_solar, r_km)`, `orbital_period_days(mass_solar, a_km)` | `GET /api/objects/<id>/orbit?r=` | Orbit calculator; animates a test orbit |
| B5 | Catalogue search | ★★ | `search.py: search_objects(objects, query, min_mass, max_distance_ly, kinds)` | `GET /api/objects/search` | Search box plus filter chips |
| B6 | Spaghettification meter | ★★★ | `tidal.py: tidal_acceleration(mass_solar, r_km, body_length_m)`, `danger_radius_km(mass_solar, tolerance_g)` | `GET /api/objects/<id>/tidal` | A meter that stretches an astronaut icon |
| B7 | Observation stats | ★★ | `observation_stats.py: observation_stats(observations)` | `GET /api/observations/stats` | Stat tiles plus a streak calendar |
| B8 | Lensing strength | ★★ | `lensing.py: einstein_radius_arcsec(mass_solar, d_lens_ly, d_source_ly)` | `GET /api/objects/<id>/lensing` | Slider that drives the lensing shader uniform |
| B9 | Accretion colours | ★ | `disk_color.py: disk_temperature_k(mass_solar, r_over_rs)`, `color_band(temperature_k)` | `GET /api/objects/<id>/disk` | Disk colour rings from the API |
| B10 | Hawking evaporation | ★★ | `hawking.py: hawking_temperature_k(mass_solar)`, `evaporation_time_years(mass_solar)` | `GET /api/objects/<id>/hawking` | "Lifetime" card with scientific notation |
| B11 | Journey planner | ★★ | `journey.py: journey_time(distance_ly, speed_fraction_c)` | `GET /api/objects/<id>/journey?v=` | Earth time vs. ship time |
| B12 | Tonight's sky | ★★★ | `visibility.py: visible_tonight(objects, observer_lat_deg, month)` | `GET /api/sky?lat=&month=` | "Visible tonight" list |

**Rules and examples.** Constants go inside each function or as default
parameters: G = 6.674e-11, c = 2.998e8, M_sun = 1.989e30.

- **B1** — r_s = 2GM/c², returned in km with `earth_radii` (6,371 km).
  *Example:* 1 solar mass → ≈ 2.95 km.
- **B2** — factor = √(1 − r_s/r) for r > r_s; `None` at or inside the
  horizon. `clock_table` returns `[{r_km, factor, seconds_per_hour}]`.
- **B3** — White dwarf if mass ≤ 1.4 and radius > 1,000 km; neutron star
  if 1.1–3 solar masses and radius 8–20 km; otherwise a black hole: <100
  stellar, <100,000 intermediate, else supermassive. `"unknown"` for
  non-positive inputs.
- **B4** — v = √(2GM/r) in km/s. T = 2π√(a³/GM) in days. Raise
  `ValueError` if r is inside the horizon.
- **B5** — The query matches names case-insensitively. Results are ranked:
  name-starts-with before contains, then by distance. Filters combine with
  AND; an empty filter means any.
- **B6** — Δa ≈ 2GM·L/r³, returned in m/s² and in g. `danger_radius_km`
  solves for Δa = tolerance_g · 9.81 with L = 2 m. Report `"safe"`,
  `"uncomfortable"` (> 1 g) or `"spaghetti"` (> 10 g).
- **B7** — Per-object counts, mean brightness (2 decimals), the longest
  run of consecutive observation dates, and the most-observed object
  (ties broken alphabetically).
- **B8** — θ_E = √(4GM/c² · D_ls/(D_l·D_s)) in arcseconds, with
  D_ls = D_s − D_l. Raise `ValueError` if the source is not behind the
  lens.
- **B9** — T ∝ M^(−1/4)·(r/r_s)^(−3/4), scaled so a 10 solar-mass hole at
  r/r_s = 3 gives 10⁷ K. Colour bands: < 4,000 K red, < 6,000 K orange,
  < 10,000 K white, else blue-white (hex codes in the docstring).
- **B10** — T = ħc³/(8πGMk_B); t ≈ 2.1e67 · (M/M_sun)³ years. Constants
  ħ and k_B go in the docstring.
- **B11** — Earth time = distance / v. Ship time = Earth time / γ, where
  γ = 1/√(1 − v²/c²). Reject v ≥ 1 or v ≤ 0.
- **B12** — Visible if the object's declination is within
  (90 − |lat|) of the observer's hemisphere, and its right-ascension
  season matches the month (ra_deg/30 ≈ month ± 2, with wrap-around).
  Sorted by distance.

---

## B3. 🚀 RocketMart — *"Everything you need to leave the planet."*

**World.** An e-commerce store for rockets, spacesuits, satellites and
mission supplies, shipping to Low Earth Orbit and beyond.

**Look.** Clean white-on-charcoal storefront with a "launch red" accent;
display font Rajdhani. Product cards with SVG rocket silhouettes.

**Pages.** Store · Product · Cart · Checkout · Orders · Compare.

**Data** (`data/`):

| File | Seed |
|---|---|
| `products.json` | 30 products across rockets, suits, satellites and supplies. Fields: `sku, name, category, price_paise, mass_kg, volume_m3`, `specs` (for rockets: `payload_leo_kg, thrust_kn, reusable, stages`) |
| `orders.json` | 40 orders `{id, user_id, lines:[{sku, qty}], status, date}` |
| `coupons.json` | 6 coupon rules |
| `orbits.json` | Shipping rates per orbit (LEO, GEO, MOON, MARS) |

**Baseline (implemented):**

1. Store grid with category filter — `logic/Catalogue.java:
   byCategory(List<Product>, String)`.
2. Product page.
3. Client-side cart (add/remove; totals shown as "—" until R1 is done).

**Warm-ups:**

- **W1** Header with a cart item count badge.
- **W2** "About RocketMart" page.

**Tasks** (Java: `logic/<Name>.java`, `api/<Name>Handler.java`,
`web/src/tasks/<Name>.jsx`):

| ID | Feature | ★ | Logic | API | UI |
|---|---|---|---|---|---|
| R1 | Cart totals | ★★ | `CartTotals.total(List<Line> lines, int gstPercent)` | `POST /api/cart/total` | Totals box on the Cart page |
| R2 | Orbital shipping | ★★ | `Shipping.cost(double massKg, String orbit)` | `POST /api/shipping/quote` | Orbit selector with the price |
| R3 | Stock reservation | ★★★ | `Inventory.reserve(Map<String,Integer> stock, List<Line> order)` | `POST /api/orders/reserve` | Checkout shows which items are out of stock |
| R4 | Recommendations | ★★ | `Recommend.topN(List<List<String>> orders, String sku, int n)` | `GET /api/products/<sku>/recommendations` | "Mission crews also bought" row |
| R5 | Order status rules | ★★ | `OrderStatus.next(String current, String event)` | `POST /api/orders/<id>/event` | Status timeline with action buttons |
| R6 | Payload fit check | ★★ | `PayloadFit.check(double maxMassKg, double fairingM3, List<Item> items)` | `POST /api/payload/check` | Fit meter on rocket pages |
| R7 | Rocket comparison | ★ | `Compare.diff(Rocket a, Rocket b)` | `GET /api/compare?a=&b=` | Side-by-side table with winner highlights |
| R8 | EMI plans | ★★★ | `Emi.schedule(long principalPaise, int months, double annualRatePct)` | `POST /api/emi` | EMI table at checkout |
| R9 | Coupons | ★★ | `Coupons.validate(String code, List<Rule> rules, String today, long cartPaise)` | `POST /api/coupons/validate` | Coupon field with the reason if rejected |
| R10 | Price alerts | ★ | `PriceWatch.triggered(List<Watch> watches, Map<String,Long> prices)` | `POST /api/alerts/check` | "Notify me" list showing triggered alerts |
| R11 | Ratings summary | ★★ | `Ratings.summary(List<Integer> stars, double priorMean, int priorWeight)` | `GET /api/products/<sku>/ratings` | Star histogram plus score |
| R12 | Delivery ETA | ★★★ | `DeliveryEta.estimate(String orbit, String orderDate)` | `GET /api/eta?orbit=&date=` | "Arrives by" date at checkout |

Records (`Line`, `Totals`, `Item`, `Rocket`, `Rule`, `Watch`, …) are
declared inside each task's class. Money is always `long` paise.

**Rules and examples:**

- **R1** — Bulk discount per line: qty ≥ 10 → 10%, ≥ 5 → 5%. GST applies
  to the discounted subtotal. Round half up to the paise. Return
  subtotal, discount, GST and total.
- **R2** — Rate per kg: LEO ₹2,000; GEO ₹6,500; MOON ₹40,000; MARS
  ₹1,20,000. Minimum charge ₹50,000; above 10 t, 15% off the excess.
  Unknown orbit → `IllegalArgumentException`.
- **R3** — All or nothing: if any line exceeds stock, reserve nothing and
  list the shortfalls. On success, return the new stock map without
  mutating the input.
- **R4** — Count how often each other SKU appears in an order with `sku`.
  Take the top n by count, ties by SKU. Exclude `sku` itself. Empty if
  there is no co-occurrence.
- **R5** — Transitions: PLACED→ASSEMBLING (`assemble`); ASSEMBLING→
  READY (`qa_pass`); ASSEMBLING→ASSEMBLING (`qa_fail`); READY→LAUNCHED
  (`launch`); LAUNCHED→DELIVERED (`dock`); PLACED or ASSEMBLING→CANCELLED
  (`cancel`). Anything else → `IllegalStateException`.
- **R6** — Fits if total mass ≤ max and total volume ≤ 85% of the fairing
  volume. Return used percentages and the first item that breaks the
  limit, in list order.
- **R7** — For each spec, report which rocket is better: higher payload
  and thrust win; lower price wins; reusable beats not reusable. Report
  ties.
- **R8** — Standard reducing-balance EMI; the rounding remainder goes in
  the last instalment; 0% interest means equal splits. Return
  `{month, emi, interest, principal, balance}` rows.
- **R9** — Reject, in this order: unknown code, expired, below minimum
  cart value, category exclusion. Percent rules are capped at
  `maxDiscountPaise`.
- **R10** — Triggered when the current price ≤ the target. Ignore watches
  for unknown SKUs; results are sorted by the largest drop percentage.
- **R11** — Average (2 decimals), a 1–5 histogram, and a Bayesian score
  `(priorMean·priorWeight + Σstars)/(priorWeight + n)`. Stars outside 1–5
  → `IllegalArgumentException`.
- **R12** — Launches happen only on Tuesdays and Fridays. There are 3
  days of assembly after ordering, then the next launch day, then transit
  (LEO 1, GEO 2, MOON 4, MARS 210 days). Return an ISO date.

---

## B4. 🗣️ Bhasha Bharat — *"Learn India, one language at a time."*

**World.** A friendly language-learning app for India's languages —
Hindi, Tamil, Telugu, Bengali, Marathi, Kannada — with lessons, flashcards
and streaks.

**Look.** Warm night-indigo background with marigold and peacock-teal
accents; display font Baloo 2 (it covers Devanagari); body Noto Sans. SVG
rangoli patterns as decoration.

**Pages.** Home · Languages · Lesson · Flashcards · Quiz · Progress ·
Leaderboard.

**Data** (`data/`):

| File | Seed |
|---|---|
| `languages.json` | 6 languages |
| `lessons.json` | 36 lessons (6 per language), with `prerequisites` |
| `cards.json` | 120 flashcards `{id, language, prompt, answer, script, ease, interval, due}` |
| `words.json` | 60 words of the day |
| `progress.json` | 5 learners, with activity events `{date, minutes, lesson_id, score}` |
| `translit.json` | Devanagari → Latin table |

**Baseline (implemented):**

1. Language picker plus lesson list — `logic/lessons.py:
   list_lessons(lessons, language)`.
2. Lesson reader.
3. Flashcard flip view (no scheduling).

**Warm-ups:**

- **W1** Navbar with a language switcher.
- **W2** About page: "Why Bhasha Bharat".

**Tasks:**

| ID | Feature | ★ | Logic (`logic/…`) | API | UI |
|---|---|---|---|---|---|
| L1 | Spaced repetition | ★★★ | `spaced_repetition.py: next_review(card, grade, today)` | `POST /api/cards/<id>/review` | Again/Hard/Good/Easy buttons on flashcards |
| L2 | Quiz scoring | ★★ | `quiz_scoring.py: score_quiz(answers, key)` | `POST /api/quiz/score` | Results screen with per-question marks |
| L3 | Streaks | ★★ | `streaks.py: update_streak(last_active, today, streak, freezes)` | `POST /api/learners/<id>/streak` | Flame counter with "freeze used" notice |
| L4 | Lesson unlocking | ★★ | `unlocking.py: unlocked_lessons(completed, lessons)` | `GET /api/learners/<id>/unlocked` | Locked/unlocked lesson map |
| L5 | Transliteration | ★★ | `transliteration.py: transliterate(text, table)` | `POST /api/transliterate` | Live transliteration box |
| L6 | "Close enough" answers | ★★ | `answer_check.py: edit_distance(a, b)`, `is_close_answer(given, expected, max_distance)` | `POST /api/answers/check` | A typed answer is marked "almost!" |
| L7 | Progress dashboard | ★★ | `progress.py: progress_summary(events, language, today)` | `GET /api/learners/<id>/progress` | Weekly minutes chart plus totals |
| L8 | Word of the day | ★ | `word_of_day.py: word_of_day(words, day_index, recent_ids)` | `GET /api/word-of-day?day=` | Home page card |
| L9 | Leaderboard | ★★ | `leaderboard.py: rank_learners(scores)` | `GET /api/leaderboard` | Ranked table showing ties |
| L10 | Daily goal | ★ | `daily_goal.py: daily_goal_status(events, goal_minutes, today)` | `GET /api/learners/<id>/goal` | Goal ring |
| L11 | Indian number formatting | ★★ | `numerals.py: format_indian(n)`, `to_script_digits(text, script)` | `GET /api/numerals?n=&script=` | Number explorer (lakh/crore, native digits) |
| L12 | Review queue | ★★★ | `review_queue.py: build_review_queue(cards, today, limit)` | `GET /api/cards/queue` | "Today's reviews" list with a count |

**Rules and examples:**

- **L1** — SM-2. Grade 0–5. If grade < 3: interval 1, repetitions 0. Else
  the interval goes 1 → 6 → round(interval × ease). Ease update
  `ease + (0.1 − (5−g)(0.08 + (5−g)0.02))`, with a floor of 1.3. `due` =
  today + interval. Return a new dict; never mutate the input.
- **L2** — Single choice: 1 or 0. Multi-select: (correct picked − wrong
  picked)/total correct, floored at 0. Text answers: case- and
  space-insensitive. Returns per-question marks, the total and the
  percentage.
- **L3** — Same day: unchanged. The next day: +1. A gap of k extra days
  consumes k freezes if available; otherwise the streak resets to 1.
  Returns `{streak, freezes, freeze_used}`.
- **L4** — A lesson is unlocked if all its prerequisites are completed.
  Lessons with no prerequisites are always unlocked. Completed lessons are
  included. Output is in lesson order.
- **L5** — Greedy longest match over the table (conjuncts before single
  characters); unknown characters pass through; handle the virama and
  inherent-vowel rule described in the docstring.
- **L6** — Levenshtein distance. "Close" means distance ≤ max_distance
  and the expected answer has at least 4 characters. An exact match
  (after trimming and case-folding) counts as close.
- **L7** — Minutes per day for the last 7 days (zeros included), total
  lessons, average score (2 decimals), and the best day. Language filter
  applied.
- **L8** — Rotate by `day_index % len(words)`, skipping `recent_ids`
  (move forward until a word is not recent). If every word is recent,
  ignore recency.
- **L9** — Dense ranking by score, descending (1, 2, 2, 3); ties sorted
  by name. Return `{rank, name, score}`.
- **L10** — Today's minutes versus the goal: percentage (capped at 100),
  remaining minutes, and `met`.
- **L11** — Indian grouping: 12,34,56,789. Digits are mapped to the
  Devanagari, Bengali, Tamil, Telugu or Kannada digit sets. Negative
  numbers and decimals are handled as described in the docstring.
- **L12** — Due cards (due ≤ today), most overdue first, then lowest ease.
  Cap at `limit`. Add "new" cards (no due date) only if fewer than `limit`
  are due.

---

# PART C — After generation (study team, before day 0)

1. **Push to the fresh repo; fork it as a test team.**
2. **Dry run every task.** Implement it WITH an AI assistant on a branch,
   open the compare page, and confirm:
   - the game **starts**;
   - Defense turns target the **task's own functions**;
   - an executable test suite is built (not only comparison grading);
   - comprehension questions are generated.

   Drop or redesign any task that fails.
3. **Verify, don't assume:**
   - Java logic files with a `package logic;` declaration compile inside
     the game's sandbox;
   - Python module-level `import math` in isolated functions;
   - whether warm-up tasks really stay below the trigger.
4. **Implement the trigger exclusions** (`data/*.json`, docs, assets) in
   AICodeQuest's `trigger.ignore_globs`. This was decided 2026-09-10 and
   is not yet implemented.
5. **Consider restricting Defense to `logic/`** (engineering change):
   UI files count toward starting the game, but the gate picks functions
   only from graded logic. Until then, a Defense turn can land on a React
   component or Three.js scene code.
6. **Fill the placeholders**, freeze the repo, and record its commit SHA in
   the study log.
