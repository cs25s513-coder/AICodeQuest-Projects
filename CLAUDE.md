# Repo orientation

This repository is generated from [`structure.md`](structure.md), a
prompt that specifies starter codebases for a week-long AI-coding training
study (AICodeQuest). Four themed projects (MoonTrip, BlackHole Explorer,
RocketMart, Bhasha Bharat) each ship a working baseline app plus a set of
**stubbed** feature tasks that study participants implement with an AI
assistant. A browser extension grades their pull requests.

**Build progress:** see [`TODO.md`](TODO.md) — updated per phase, don't
assume a project is finished without checking it.

## Rules that apply to every project (from `structure.md` Part A)

- **Layout is fixed and load-bearing.** Every project has exactly
  `logic/ api/ web/ data/ tests/` at its top level — never nested deeper
  (no `server/logic/`). The grading game counts changes per top-level
  folder; nesting breaks it.
- **Functional core, imperative shell.** `logic/` functions take plain
  data in, return plain data out. No file/network/env/clock/RNG access, no
  classes (Python), stdlib-only imports, no module-level mutable state, no
  nested functions or lambdas-in-variables. Only `api/` touches
  `data/*.json`, via a `store` module.
- **Task isolation.** Every numbered task (e.g. M4) owns exactly three
  pre-created stub files — `logic/<slug>.py`, `api/<slug>_routes.py`,
  `web/src/tasks/<Name>.jsx` — already registered (route mounted
  returning 501, UI slot already on its page). Never mix baseline code
  and task code in the same file.
- **Do not implement task logic.** Only baseline features (listed per
  project) are fully built by the generator. Task function bodies stay
  `raise NotImplementedError(...)` / `throw new UnsupportedOperationException(...)`
  until a participant does it.
- **No numeric game thresholds** appear in any document — placeholders
  like `[PASS_MARK]` are filled in later by the study team, not by the
  generator.

Full detail — stack per project, ports, seed data, per-task rules and
examples, doc structure — lives in `structure.md`. Read the relevant Part B
section before touching a given project.
