<!--
  For AI agents: this profile is machine-readable on purpose.
  → AGENTS.md (this repo) explains how this repo works.
  → hermes-skills-portfolio/skills-index.json is a one-parse index of everything published here.
-->

<div align="center">

<img src="assets/banner.svg" alt="THEROCKSSS — agent-ready tools, built in human–agent pairs" width="100%">

<br>

<a href="https://github.com/THEROCKSSS?tab=followers"><img alt="followers" src="https://img.shields.io/github/followers/THEROCKSSS?style=flat-square&label=followers&color=1f6feb"></a>
<img alt="profile views" src="https://komarev.com/ghpvc/?username=THEROCKSSS&label=profile+views&color=1f6feb&style=flat-square">
<img alt="harness: Hermes Agent" src="https://img.shields.io/badge/harness-Hermes_Agent-1f6feb?style=flat-square">
<img alt="pairing: Claude Code and Codex" src="https://img.shields.io/badge/pairing-Claude_Code_%C2%B7_Codex-1f6feb?style=flat-square">
<img alt="agents welcome" src="https://img.shields.io/badge/agents-welcome-3fb950?style=flat-square">

</div>

## Hey, I'm Owen.

I build **agent-ready tools** — software that a person *and* their AI agents can pick up, run, and extend without a six-week onboarding. Local-first where it counts; documented like a new team takes over tomorrow, because that's usually the plan.

The whole shop runs as a **human–agent pairing loop**, and it's all in the open — specs, tickets, implementation, review, with agents in most seats and a human on the merge button.

## Featured builds

### [hermes-skills-portfolio](https://github.com/THEROCKSSS/hermes-skills-portfolio)
<img alt="stars" src="https://img.shields.io/github/stars/THEROCKSSS/hermes-skills-portfolio?style=flat-square&color=1f6feb"> <img alt="license" src="https://img.shields.io/github/license/THEROCKSSS/hermes-skills-portfolio?style=flat-square&color=8b949e"> <img alt="last commit" src="https://img.shields.io/github/last-commit/THEROCKSSS/hermes-skills-portfolio?style=flat-square&color=3fb950">

A curated set of **50+ installable skills for [Hermes Agent](https://hermes-agent.nousresearch.com)**. One pattern throughout: *agent + skill = a working capability* — deploy on Tailscale, self-host Forgejo, build a non-generic frontend, publish a skill. Every skill is ranked, reviewed, and merged through a submission workflow; `skills-index.json` gives agents a single-parse index.

```bash
hermes skills install https://raw.githubusercontent.com/THEROCKSSS/hermes-skills-portfolio/main/skills/tailscale-deploy/SKILL.md
```

### [vpn-egress](https://github.com/THEROCKSSS/vpn-egress)
<img alt="stars" src="https://img.shields.io/github/stars/THEROCKSSS/vpn-egress?style=flat-square&color=1f6feb"> <img alt="license" src="https://img.shields.io/github/license/THEROCKSSS/vpn-egress?style=flat-square&color=8b949e"> <img alt="last commit" src="https://img.shields.io/github/last-commit/THEROCKSSS/vpn-egress?style=flat-square&color=3fb950">

The only question that matters about a public service is whether it **actually loads from outside your network** — so this Docker stack answers it. One Mullvad WireGuard tunnel feeds three containers: a GUI browser for humans, a headless one for agents, and `check-url` results in structured JSON either can trust. Built because hairpin NAT and cloud probes both lie — both produce false negatives that look authoritative.

### [anvil](https://github.com/THEROCKSSS/anvil)
<img alt="stars" src="https://img.shields.io/github/stars/THEROCKSSS/anvil?style=flat-square&color=1f6feb"> <img alt="license" src="https://img.shields.io/github/license/THEROCKSSS/anvil?style=flat-square&color=8b949e"> <img alt="last commit" src="https://img.shields.io/github/last-commit/THEROCKSSS/anvil?style=flat-square&color=3fb950"> <img alt="platforms: iOS and Android" src="https://img.shields.io/badge/iOS_%C2%B7_Android-one_Expo_codebase-1f6feb?style=flat-square">

A **mobile client for self-hosted Forgejo** — Android and iOS from one Expo codebase. Explore instances, repos, files, milestones, and issues from a phone over a tailnet, with tokens in the device keychain and screenshots from real devices in the README. Independent, unofficial, MIT.

### [smart-bulb-dashboard](https://github.com/THEROCKSSS/smart-bulb-dashboard)
<img alt="stars" src="https://img.shields.io/github/stars/THEROCKSSS/smart-bulb-dashboard?style=flat-square&color=1f6feb"> <img alt="license: noncommercial" src="https://img.shields.io/badge/license-noncommercial-6e7681?style=flat-square"> <img alt="last commit" src="https://img.shields.io/github/last-commit/THEROCKSSS/smart-bulb-dashboard?style=flat-square&color=3fb950">

A **local, cloud-independent dashboard** for Tuya Wi-Fi bulbs: **186 features**, a FastAPI backend, and a vanilla-JS dark UI that talks to the bulb directly over your LAN — no cloud round-trip for day-to-day control. 14 audio-reactive lighting modes at sub-15ms latency, Prometheus metrics, a PIN-gated remote path, and a [hand-built 9-page docs site](https://therocksss.github.io/smart-bulb-dashboard/). Noncommercial license.

<img src="https://raw.githubusercontent.com/THEROCKSSS/smart-bulb-dashboard/master/docs/screenshots/control.png" alt="Smart Bulb Dashboard control panel" width="640">

---

**Elsewhere in the workshop:** [discord-stream-overlay](https://github.com/THEROCKSSS/discord-stream-overlay) — OBS overlays from a Vencord plugin · [crate](https://github.com/THEROCKSSS/crate) — community playlists, one PR per song · [battlebit-stats](https://github.com/THEROCKSSS/battlebit-stats) — self-hosted game stats · [sorted-iptv](https://github.com/THEROCKSSS/sorted-iptv) — free-to-air streams, sorted · [self-hosted-project-hub](https://github.com/THEROCKSSS/self-hosted-project-hub) — a cloneable live-data project index

## How the work gets made

Every repo here is built in a **human–agent pairing loop** — and ships the scaffolding so any agent (yours included) can pick up where mine left off.

- **Harnesses** — [Hermes Agent](https://hermes-agent.nousresearch.com) runs my fleet; **Claude Code** and **Codex** work beside it as peers. Specs, tickets, and review comments — not vibes.
- **Coordination** — self-hosted **Forgejo**: feature branches, PRs, review queues. Agents open PRs; a human merges.
- **Memory** — a self-hosted **Supabase** store keeps durable context consistent across agents and sessions, so nothing gets learned twice.
- **Handoff by default** — repos ship `AGENTS.md`, project-local agent skills, and a `HANDOFF.md`, so work survives interruptions, outages, and model swaps.

## By the numbers

<img src="assets/stats.svg" alt="Stats — regenerated daily by this repo's own GitHub Action" width="100%">

<p>
<img src="https://ghstats.dev/api/card?username=THEROCKSSS&theme=tokyonight&hide_border=true" alt="Live activity card" height="165">
<img src="https://streak-stats.demolab.com?user=THEROCKSSS&theme=tokyonight&hide_border=true" alt="Streak card" height="165">
</p>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=THEROCKSSS&theme=tokyonight" alt="Contribution summary" width="100%">

<sub>The first card is generated daily by this repo's own Action — it can't go down with a third-party service. The rest are live embeds (ghstats.dev, streak-stats, summary-cards).</sub>

## Work with me — and with my agents

- **Open to collaborate.** Issues and PRs welcome on every repo — a rough PR beats a perfect plan.
- **Agents welcome.** The projects ship agent instructions on purpose: point yours at any `AGENTS.md`, or one-parse [skills-index.json](https://raw.githubusercontent.com/THEROCKSSS/hermes-skills-portfolio/main/skills-index.json).
- **Usage is the fuel.** The skills portfolio improves every time someone installs one and reports what broke — that's the loop. Try one against your own agent.

<div align="center">
<img src="assets/footer.svg" alt="by Owen — built with Hermes Agent, Claude Code and Codex" width="100%">
</div>
