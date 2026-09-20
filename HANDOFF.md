# HANDOFF — GitHub Profile (THEROCKSSS/THEROCKSSS)

**Status:** created 2026-09-20 · deployed (verification evidence below)
**Owner:** Owen (public attribution: "by Owen"). Built by Familiar (Hermes Agent).

## What this is

The special `THEROCKSSS/THEROCKSSS` repo whose README renders on
https://github.com/THEROCKSSS. It presents: the four featured builds, the
harness/agent workflow, self-hosted + third-party stats, and collaboration info.

## Layout

- `README.md` — the profile (production; renders publicly)
- `assets/banner.svg` — hand-built header (palette: bg `#0d1117`, accent `#1f6feb`, ink `#e6edf3`)
- `assets/stats.svg` + `assets/stats.json` — **generated** daily by
  `scripts/generate_stats.py` via `.github/workflows/stats.yml` (never hand-edit)
- `scripts/generate_stats.py` — regenerates stats from public GitHub data (stdlib only)
- `scripts/selftest.py` — asset/README checks; `--embeds` checks third-party URLs
- `.github/workflows/verify.yml` — CI on push · `stats.yml` — daily refresh (cron `23 5 * * *`)

## How to update

1. Edit `README.md` / hand-made assets as needed.
2. `python3 scripts/selftest.py` (add `--embeds` when touching embed URLs).
3. Commit + push to `main` (profile renders from the default branch only).

Stats self-refresh daily. Manual refresh:
`gh workflow run stats.yml -R THEROCKSSS/THEROCKSSS`

## Embed policy / known constraints

- GitHub camo caches README images — stats card may lag up to a few hours.
- Broken-for-everyone services (checked 2026-09-20): github-readme-stats
  (DEPLOYMENT_PAUSED), profile-trophy (402), readme-activity-graph (402).
- Working third-party embeds in use: ghstats.dev, streak-stats.demolab.com,
  github-profile-summary-cards.vercel.app, shields.io, komarev.com.

## Verification evidence

- Profile repo created + README pushed: _filled in after deploy_
- Stats workflow run: _filled in after deploy_
- Live profile renders README: _filled in after deploy_
- Profile settings (name/bio/website) applied via API: _filled in after deploy_

## Follow-ups

- Profile "location" / social fields left unset (no confirmed values).
- Achievements roadmap: Pull Shark base (2 merged PRs) etc. — earn legitimately via normal PR flow.
- Consider pruning the 34 stale forks (2020–2023 era) from the profile.
- Portfolio README skills table still shows the Phase-1 placeholder — verify whether
  the refresh is intentionally pending before running it.
