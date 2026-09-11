# Build TODO — AICodeQuest study repo

Generated from `structure.md`. Tracks progress across sessions so any
session can resume without re-reading the whole spec. Update checkboxes as
work completes — do not wait until a phase is fully done to update this
file.

## Phase 0 — Root files
- [x] `README.md` (A10.1)
- [x] `CONTRIBUTING.md` (A10.3)
- [x] `.github/PULL_REQUEST_TEMPLATE.md`
- [x] `.gitignore`
- [x] `LICENSE` (MIT)
- [x] `CLAUDE.md` (orientation for future sessions)
- [x] `TODO.md` (this file)

## Phase 1 — MoonTrip (Python/Flask + React)
- [ ] Project README (`moontrip/README.md`)
- [x] Seed data: `destinations.json`, `spacecraft.json`, `bookings.json`, `promos.json`, `missions.json`
- [x] `api/store.py`
- [x] Baseline logic: `logic/catalogue.py`, `logic/spacecraft.py`
- [x] Baseline routes: `api/catalogue_routes.py`, `api/spacecraft_routes.py`, `api/deals_routes.py`, `api/app.py`, `api/__main__.py`
- [x] Baseline tests: `tests/test_catalogue.py`, `tests/test_spacecraft.py`
- [x] Shared UI kit: `web/src/ui/*`, `web/src/api.js`
- [x] Page shells: Home, Destinations, DestinationDetail, Book, MyTrips, MissionControl, Deals
- [x] Nav (no active-state) + app shell, Vite config, package.json
- [x] Task stubs — logic + route + UI, all pre-registered, for M1–M12:
  - [x] M1 price calculator
  - [x] M2 launch windows
  - [x] M3 booking history
  - [x] M4 refunds
  - [x] M5 seat allocation
  - [x] M6 mission status
  - [x] M7 promo codes
  - [x] M8 itinerary validator
  - [x] M9 luggage fees
  - [x] M10 passenger checks
  - [x] M11 loyalty
  - [x] M12 mission stats
- [ ] A12 acceptance checklist — **paused 2026-09-11**: pytest (11/11) and
      Flask routes (baseline + 501 stubs) verified working; web build/dev
      server not yet checked. Paused to work on Phase 2; resume before
      calling MoonTrip done.

## Phase 2 — BlackHole Explorer (scoped down, 2026-09-11)

**Deviates from structure.md by explicit user direction.** Not the full
B2 spec (no 12 tasks, no seed data, no warm-ups). Just:
- [x] Minimal backend (`api/`) — a single placeholder route
      (`GET /api/status`), nothing else wired up.
- [x] Frontend home page: an interactive 3D black hole (Three.js) —
      event horizon, glow/photon-ring shader, accretion disk shader
      (radial gradient + turbulence), starfield, gravitational-lensing
      post-process pass, bloom, OrbitControls (drag to orbit, scroll to
      zoom). Verified visually via headless Chrome screenshots — renders
      correctly, drag and zoom both confirmed working, no console errors.

The full B2 task list in `structure.md` (event horizon calc, time
dilation, classification, etc.) is deferred indefinitely unless asked
for again.

## Phase 3 — RocketMart (Java 17/Maven + React)
- [ ] Not started

## Phase 4 — Bhasha Bharat (Python/Flask + React)
- [ ] Not started

## Phase 5 — Part C (study team, before day 0)
- [ ] Push to fresh repo, fork as test team
- [ ] Dry run every task with an AI assistant on a branch
- [ ] Verify Java/Python sandbox compile assumptions
- [ ] Implement `trigger.ignore_globs` exclusions in AICodeQuest
- [ ] Consider restricting Defense to `logic/` only
- [ ] Fill placeholders (`[PASS_MARK]`, `[EXTENSION_INSTALL]`, `[STUDY_DATES]`, `[SUPPORT_CONTACT]`, `[REPO_URL]`), freeze repo, record commit SHA
