# 🕳️ BlackHole Explorer

**Get close. Not too close.**

This is a small, scoped-down build: an interactive 3D black hole on the
home page (event horizon, accretion disk, lensed starlight, orbit
controls), with a placeholder backend. The full study-project spec in
`structure.md` (Part B2 — 12 graded tasks, seed data, warm-ups) is
deferred; see `TODO.md` at the repo root for status.

## Run it

**Prerequisites:** Python 3.12+, Node.js 18+.

### API (port 5102) — placeholder only

```bash
# from blackhole-explorer/
pip install -r requirements.txt
python -m api
```

### Web (port 5202)

```bash
# from blackhole-explorer/web/
npm install
npm run dev
```

Open http://localhost:5202.

## How it's built

- `web/src/scene.js` — Three.js scene: camera, renderer, OrbitControls,
  starfield, event horizon, accretion disk, and a bloom + gravitational-
  lensing post-processing pass.
- `web/src/shaders.js` — the GLSL for the disk's glow/turbulence and the
  screen-space lensing warp.
- `api/` — a single placeholder Flask route (`GET /api/status`). Nothing
  else is wired up yet.
