#!/usr/bin/env python3
"""Refresh the public profile's recent-repository section from GitHub metadata."""
import html
import os
import re
import urllib.request
import json
from pathlib import Path

USER = "THEROCKSSS"
CUTOFF = "2026-09-20T23:59:59Z"
ROOT = Path(__file__).resolve().parent.parent
START = "<!-- RECENT-REPOS:BEGIN -->"
END = "<!-- RECENT-REPOS:END -->"


def github_repos():
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "THEROCKSSS-profile-repos"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    all_repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}&sort=created&direction=desc"
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=45) as response:
            repos = json.load(response)
        if not isinstance(repos, list):
            raise ValueError("Unexpected GitHub repositories response")
        all_repos.extend(repos)
        if len(repos) < 100:
            break
        page += 1
    return all_repos


def safe_text(value):
    value = html.escape(str(value or ""), quote=False)
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", value).replace("\n", " ").replace("\r", " ")


def render(repos):
    recent = [r for r in repos if r.get("created_at", "") > CUTOFF and not r.get("private")]
    recent.sort(key=lambda r: r["created_at"], reverse=True)
    lines = [START, "", "| Repository | Type | What it is |", "|---|---|---|"]
    for repo in recent:
        name = repo["name"]
        url = repo["html_url"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", name) or not url.startswith(f"https://github.com/{USER}/"):
            raise ValueError(f"Unexpected repository metadata: {name}")
        kind = "Fork" if repo.get("fork") else "Original"
        desc = safe_text(repo.get("description") or "No description provided")
        lines.append(f"| [{safe_text(name)}]({url}) | {kind} | {desc} |")
    lines += ["", f"*{len(recent)} public repositories created since 2026-09-20. Metadata from GitHub; refreshed daily. Forks are labeled above.*", "", END]
    return "\n".join(lines)


def main():
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        raise SystemExit("README recent-repo markers missing or duplicated")
    start = text.index(START)
    end = text.index(END) + len(END)
    updated = text[:start] + render(github_repos()) + text[end:]
    if updated != text:
        path.write_text(updated, encoding="utf-8")
    print("Recent repository section refreshed")


if __name__ == "__main__":
    main()
