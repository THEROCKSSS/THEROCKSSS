# HANDOFF — GitHub Profile (THEROCKSSS/THEROCKSSS)

**Status:** ✅ DEPLOYED 2026-09-20 · live at https://github.com/THEROCKSSS
**Owner:** Owen (public attribution: "by Owen"). Built by Familiar (Hermes Agent).

## What this is

The special `THEROCKSSS/THEROCKSSS` repo whose README renders on
https://github.com/THEROCKSSS. It presents: the four featured builds, the
harness/agent workflow, self-hosted + third-party stats, and collaboration info.

## Layout

- `README.md` — the profile (production; renders publicly)
- `assets/banner.svg` — hand-built header (palette: bg `#0d1117`, accent `#1f6feb`, ink `#e6edf3`)
- `assets/footer.svg` — hand-built signature strip
- `assets/stats.svg` + `assets/stats.json` — **generated** daily by
  `scripts/generate_stats.py` via `.github/workflows/stats.yml` (never hand-edit)
- `scripts/generate_stats.py` — regenerates stats from public GitHub data (stdlib only)
- `scripts/selftest.py` — asset/README checks; `--embeds` checks third-party URLs
- `.github/workflows/` — `verify.yml` (CI on push) · `stats.yml` (daily 05:23 UTC) · `embed-check.yml` (weekly Mon 06:41 UTC)

## How to update

1. Edit `README.md` / hand-made assets as needed.
2. `python3 scripts/selftest.py` (add `--embeds` when touching embed URLs).
3. Commit + push to `main` (profile renders from the default branch only).

Stats self-refresh daily. Manual refresh:
`gh workflow run stats.yml -R THEROCKSSS/THEROCKSSS`

## Stats card design notes

- Contributions grid cell ids are `contribution-day-component-{WEEKDAY}-{WEEK}` —
  weekday first. Inverting this renders a 7-column strip instead of a 52-week
  heatmap. `generate_stats.py` now guards the index order and refuses to write
  assets when it doesn't match (Sunday at (0,0), 50–54 week columns, 365 cells).
- Cell tooltips carry the counts (`N contributions on <date>`); the `data-count`
  attribute is NOT present in the HTML.
- Current streak is computed from day cells (today excluded when it's a zero
  partial day); GitHub's streak page semantics differ slightly.

## Embed policy / known constraints

- GitHub camo caches README images — stats card may lag up to a few hours.
- Broken-for-everyone services (re-checked 2026-09-20): github-readme-stats
  (503 DEPLOYMENT_PAUSED), profile-trophy (402), readme-activity-graph (402).
  All three verified still broken — not embedded.
- Working embeds in use (all verified 200): ghstats.dev, streak-stats.demolab.com,
  github-profile-summary-cards.vercel.app, shields.io, komarev.com.

## Verification evidence (all real tool output, 2026-09-20)

- Repo created + pushed: `gh repo create THEROCKSSS/THEROCKSSS --public --source=. --push`
  → commit `c43fe31`, then bot commit `8f4cecf` (stats refresh).
- CI: `verify` run `35546163482` → **success** (9s). `stats` run `35546190566` → **success** (10s).
- Stats bot committed its own refresh to `main` — automation proven end-to-end.
- Live profile page fetched: README block present, all sections found
  ("Hey, I'm Owen", banner.svg, stats.svg, footer, 25 README images resolve).
- Live render inspected in browser — banner, badges, cards, pins, activity graph all render.
- Repo topics applied: `agent-ready, ai-agents, github-profile, hermes-agent, profile, profile-readme`.
- Repo metadata: smart-bulb-dashboard About corrected 97 → **186 features**;
  homepages set on hermes-skills-portfolio + smart-bulb-dashboard;
  topics added to 8 repos that had none.
- Canonical memory: `user.identity.public_and_local_names` corrected to "Owen"
  (revision 2, supersedes "Monica Amano"; user chose "by Owen" this session).

## Open items

- **Profile name/bio/website:** token lacks `user` scope — `gh auth refresh -h github.com -s user`
  device flow was started (one-time code issued) and is awaiting browser approval.
  After approval: re-run the PATCH with `.github/profile-patch.json` payload
  (name "Owen", bio "Agent-ready tools, built in human–agent pairs…", blog = portfolio site).
- Profile "location" / social fields left unset (no confirmed values).
- Achievements roadmap: Pull Shark base (2 merged PRs) etc. — earn legitimately via normal PR flow.
- Consider pruning the 34 stale forks (2020–2023 era) from the profile.
- Portfolio README skills table still shows the Phase-1 placeholder — verify whether
  the refresh is intentionally pending before running it.
