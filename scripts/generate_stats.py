#!/usr/bin/env python3
"""
Regenerate assets/stats.svg + assets/stats.json for the THEROCKSSS profile README.

Why: third-party stats services break (readme-stats, trophy, activity-graph were
all down on 2026-09-20). This card is generated from public GitHub data by this
repo's own Action, so it cannot go down with someone else's deployment.

Stdlib only. Optional GITHUB_TOKEN for higher rate limits.
Safety: assets are only replaced when fresh data parses cleanly.
"""

import datetime as dt
import json
import os
import re
import sys
import urllib.request

USER = "THEROCKSSS"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
UA = f"{USER}-profile-stats/1.0 (+https://github.com/{USER})"
TOKEN = (os.environ.get("GITHUB_TOKEN") or "").strip() or None

W = 1200
PAD = 40
BG = "#0d1117"
BORDER = "#21262d"
ACCENT = "#1f6feb"
INK = "#e6edf3"
DIM = "#8b949e"
LEVELS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"


def fetch(url, accept="application/vnd.github+json"):
    headers = {"User-Agent": UA, "Accept": accept}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- data

def get_account():
    u = json.loads(fetch(f"https://api.github.com/users/{USER}"))
    return u["followers"], u["public_repos"]


def get_repos():
    stars = own = forks = 0
    page = 1
    while True:
        repos = json.loads(fetch(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}"))
        if not isinstance(repos, list) or not repos:
            break
        for r in repos:
            if r.get("fork"):
                forks += 1
            else:
                own += 1
                stars += r.get("stargazers_count", 0)
        if len(repos) < 100:
            break
        page += 1
    return stars, own, forks


def parse_days(html):
    days = {}
    for m in re.finditer(r"<td[^>]*ContributionCalendar-day[^>]*>", html):
        tag = m.group(0)
        date = re.search(r'data-date="(\d{4}-\d{2}-\d{2})"', tag)
        cid = re.search(r'id="contribution-day-component-(\d+)-(\d+)"', tag)
        lvl = re.search(r'data-level="(\d+)"', tag)
        if date and cid and lvl:
            days[(int(cid.group(1)), int(cid.group(2)))] = {
                "date": date.group(1), "level": int(lvl.group(1)), "count": None}
    for m in re.finditer(r'for="contribution-day-component-(\d+)-(\d+)"[^>]*>([^<]+)</tool-tip>', html):
        key = (int(m.group(1)), int(m.group(2)))
        if key not in days:
            continue
        txt = m.group(3).strip()
        if txt.startswith("No "):
            n = 0
        else:
            mm = re.match(r"(\d+)\s+contribution", txt)
            n = int(mm.group(1)) if mm else 0
        days[key]["count"] = n
    return days


def get_skills_count():
    try:
        j = json.loads(fetch(
            f"https://raw.githubusercontent.com/{USER}/hermes-skills-portfolio/main/skills-index.json",
            accept="text/plain"))
        sk = j.get("skills") if isinstance(j, dict) else j
        if isinstance(sk, list) and sk:
            return len(sk)
    except Exception:
        pass
    try:
        with open(os.path.join(ASSETS, "stats.json"), encoding="utf-8") as f:
            v = json.load(f)["totals"].get("skills_published")
            if isinstance(v, int) and v > 0:
                return v
    except Exception:
        pass
    return None


# ---------------------------------------------------------------- svg

def svg_card(today, cells, days, weeks):
    gap = 3.0
    cell = (W - 2 * PAD - (weeks - 1) * gap) / weeks
    rows = 7
    grid_top = 84
    row_h = 72
    months_y = grid_top + 2 * row_h + 36
    top = months_y + 12
    bottom = top + rows * cell + (rows - 1) * gap
    H = round(bottom + 26)

    p = []
    A = p.append
    A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'role="img" aria-label="GitHub stats for {USER} — contributions, streaks, and yearly activity">')
    A('<defs><pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse">'
      '<circle cx="2" cy="2" r="1.1" fill="#161b22"/></pattern>'
      f'<style>.mono {{ font-family: {MONO}; }}'
      '.num { font-size: 30px; font-weight: 700; fill: ' + INK + '; letter-spacing: 0.5px; }'
      '.lbl { font-size: 12.5px; fill: ' + DIM + '; letter-spacing: 0.3px; }'
      '.ttl { font-size: 15px; font-weight: 700; fill: #58a6ff; letter-spacing: 2.4px; }'
      '.meta { font-size: 12px; fill: ' + DIM + '; letter-spacing: 0.3px; }'
      '.mon { font-size: 12px; fill: ' + DIM + '; }'
      '</style></defs>')
    A(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    A(f'<rect width="{W}" height="{H}" fill="url(#dots)" opacity="0.55"/>')
    A('<circle cx="1120" cy="100" r="145" fill="none" stroke="#203856" stroke-width="2"/>')
    A('<circle cx="1120" cy="100" r="106" fill="none" stroke="#1f6feb" stroke-dasharray="3 9"/>')
    A(f'<line x1="0" y1="4" x2="{W}" y2="4" stroke="{ACCENT}" stroke-width="3" opacity="0.85"/>')
    A(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" fill="none" stroke="{BORDER}"/>')

    A(f'<text class="mono ttl" x="{PAD}" y="50">BY THE NUMBERS</text>')
    A(f'<text class="mono meta" x="{W - PAD}" y="50" text-anchor="end">auto-updated {today} '
      f'&#183; regenerated by this repo&#8217;s GitHub Action</text>')

    # Eight measured values presented as individual instrument panels.
    cw = (W - 2 * PAD) / 4
    for i, (num, label) in enumerate(cells):
        r, c = divmod(i, 4)
        x = PAD + c * cw
        ny = grid_top + r * row_h + 34
        A(f'<rect x="{x:.0f}" y="{grid_top + r * row_h - 13:.0f}" width="{cw - 9:.0f}" height="70" rx="5" fill="#111d2b" stroke="#2e4561"/>')
        A(f'<path d="M{x + 5:.0f} {grid_top + r * row_h + 4:.0f}v35" stroke="{ACCENT}" stroke-width="2"/>')
        A(f'<text class="mono num" x="{x + 13:.0f}" y="{ny - 2}">{esc(num)}</text>')
        A(f'<text class="mono lbl" x="{x + 13:.0f}" y="{ny + 16}">{esc(label)}</text>')

    A(f'<rect x="{PAD - 12}" y="{top - 15:.0f}" width="{W - 2 * PAD + 24}" height="{bottom - top + 30:.0f}" rx="5" fill="#0e1824" stroke="#2e4561"/>')

    # month labels — row 0 is Sunday; walk week columns and pick the month of each week's Sunday
    last_x = -100.0
    prev_month = None
    for w in range(weeks):
        first = days.get((0, w))
        if not first:
            continue
        month = first["date"][:7]
        if month != prev_month:
            x = PAD + w * (cell + gap)
            if x - last_x > 30:
                name = dt.date.fromisoformat(first["date"]).strftime("%b")
                A(f'<text class="mono mon" x="{x:.1f}" y="{months_y}">{name}</text>')
                last_x = x
            prev_month = month

    # legend (right of month row)
    lx = W - PAD - (5 * 14 + 60)
    legend_y = months_y - 25
    A(f'<text class="mono mon" x="{lx}" y="{legend_y}">less</text>')
    for i in range(5):
        A(f'<rect x="{lx + 34 + i * 14}" y="{legend_y - 10}" width="11" height="11" rx="2.5" '
          f'fill="{LEVELS[i]}"/>')
    A(f'<text class="mono mon" x="{lx + 34 + 5 * 14 + 6}" y="{legend_y}">more</text>')

    # Heatmap cells are actual contribution levels returned by GitHub.
    for (weekday, week), day in days.items():
        x = PAD + week * (cell + gap)
        y = top + weekday * (cell + gap)
        col = LEVELS[max(0, min(4, day["level"]))]
        A(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell:.1f}" height="{cell:.1f}" rx="2.5" fill="{col}">'
          f'<title>{day["count"]} contributions on {day["date"]}</title></rect>')

    A('</svg>')
    return "\n".join(p)


def main():
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    followers, public_repos = get_account()
    stars, own, forks = get_repos()

    html = fetch(f"https://github.com/users/{USER}/contributions", accept="text/html")
    days = parse_days(html)
    if len(days) < 300 or any(d["count"] is None for d in days.values()):
        sys.exit("stats: contributions parse looked wrong — not touching assets")
    # grid-index guard: cells are keyed (weekday, week) — row 0 must be Sunday
    first_cell = days.get((0, 0))
    if not first_cell or dt.date.fromisoformat(first_cell["date"]).strftime("%A") != "Sunday":
        sys.exit("stats: contribution grid index order changed — refusing to write assets")
    if max(k[0] for k in days) != 6 or not (50 <= max(k[1] for k in days) <= 54):
        sys.exit("stats: contribution grid shape unexpected — refusing to write assets")
    order = sorted(days.values(), key=lambda d: d["date"])
    total = sum(d["count"] for d in order)
    active = sum(1 for d in order if d["count"] > 0)

    i = len(order) - 1
    if order[i]["date"] == today and order[i]["count"] == 0:
        i -= 1  # today may be partial; GitHub counts the streak anyway
    cur = 0
    while i >= 0 and order[i]["count"] > 0:
        cur += 1
        i -= 1
    longest = run = 0
    for d in order:
        run = run + 1 if d["count"] > 0 else 0
        longest = max(longest, run)

    skills = get_skills_count()
    skills_s = str(skills) if isinstance(skills, int) else "\u2014"

    cells = [
        (str(total), "contributions \u00b7 last 365 days"),
        (str(active), "active days"),
        (f"{cur}", "current streak (days)"),
        (f"{longest}", "longest streak (days)"),
        (str(stars), "stars received"),
        (str(own), "public repos (own)"),
        (skills_s, "skills published"),
        (str(followers), "followers"),
    ]
    cols = max(k[1] for k in days) + 1
    svg = svg_card(today, cells, days, cols)

    data = {
        "user": USER,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "range": [order[0]["date"], order[-1]["date"]],
        "totals": {
            "contributions": total, "active_days": active, "current_streak": cur,
            "longest_streak": longest, "stars": stars, "own_repos": own, "forks": forks,
            "followers": followers, "public_repos": public_repos,
            "skills_published": skills if isinstance(skills, int) else None,
        },
        "daily": [{"d": d["date"], "c": d["count"], "l": d["level"]} for d in order],
    }

    os.makedirs(ASSETS, exist_ok=True)
    for path, content in ((os.path.join(ASSETS, "stats.svg"), svg),
                          (os.path.join(ASSETS, "stats.json"), json.dumps(data, indent=1) + "\n")):
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        os.replace(tmp, path)
    print(f"stats: wrote assets/stats.svg + stats.json "
          f"(contrib={total} active={active} cur={cur} longest={longest} stars={stars} "
          f"repos={own} skills={skills_s} followers={followers})")


if __name__ == "__main__":
    main()
