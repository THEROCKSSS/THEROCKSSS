# AGENTS.md — how to work in this repo

This repo is **THEROCKSSS's GitHub profile**. `README.md` renders publicly at
https://github.com/THEROCKSSS — treat it as production.

## Rules

- **Never hand-edit generated files.** `assets/stats.svg` and `assets/stats.json`
  come from `scripts/generate_stats.py` (daily via `.github/workflows/stats.yml`).
  To refresh now: `gh workflow run stats.yml -R THEROCKSSS/THEROCKSSS`.
- **`assets/banner.svg` and `assets/footer.svg` are hand-made.** Edit carefully;
  keep the palette (bg `#0d1117`, accent `#1f6feb`, ink `#e6edf3`, dim `#8b949e`).
- **Embeds must be verified before adding.** Run `python3 scripts/selftest.py --embeds`.
  Known-broken-for-everyone as of 2026-09-20 (do not re-add until they recover):
  github-readme-stats (deploy paused), profile-trophy (402), readme-activity-graph (402).
- **GitHub camo caches README images** — the stats card may lag a few hours behind
  the repo. That is normal.
- **Ship straight to `main`** — the profile README renders only from the default
  branch. Commit, push, done.
- **No credentials, no personal email** anywhere in this repo. Public attribution
  name is **Owen** ("by Owen").

## Commands

| Command | What it does |
|---|---|
| `python3 scripts/generate_stats.py` | Regenerate the stats card (token optional: `GITHUB_TOKEN=$(gh auth token)`) |
| `python3 scripts/selftest.py` | Assets exist, XML valid, README refs resolve |
| `python3 scripts/selftest.py --embeds` | Also checks every third-party embed URL |

## Context

- Maintain `HANDOFF.md` with state + evidence — work must resume after interruption.
- `README.md` is the deliverable; everything else exists to keep it accurate.
