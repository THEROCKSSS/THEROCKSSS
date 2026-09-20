#!/usr/bin/env python3
"""
Self-test for the THEROCKSSS profile repo.

Checks (always):
  - every generated/hand-made asset exists and is valid XML
  - every relative src/href in README.md resolves to a real file
  - README.md keeps the "by Owen" attribution
  - stats.json freshness (warning; fails only with --strict)

With --embeds: every http(s) image URL in README.md is fetched and must be < 400.
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
ASSETS = os.path.join(ROOT, "assets")
UA = "THEROCKSSS-profile-selftest/1.0"

fails, warns = [], []


def note(kind, msg):
    (fails if kind == "FAIL" else warns).append(msg)
    print(f"  {kind}: {msg}")


def check_assets():
    print("assets:")
    if not os.path.isdir(ASSETS):
        return note("FAIL", "assets/ missing")
    for name in sorted(os.listdir(ASSETS)):
        path = os.path.join(ASSETS, name)
        if name.endswith(".svg"):
            try:
                ET.parse(path)
                print(f"  ok: {name} (valid XML, {os.path.getsize(path)}b)")
            except ET.ParseError as e:
                note("FAIL", f"{name} invalid XML: {e}")
        elif name.endswith(".json"):
            try:
                json.load(open(path, encoding="utf-8"))
                print(f"  ok: {name} (valid JSON)")
            except Exception as e:
                note("FAIL", f"{name} invalid JSON: {e}")
    for required in ("banner.svg", "footer.svg", "stats.svg", "stats.json"):
        if not os.path.exists(os.path.join(ASSETS, required)):
            note("FAIL", f"assets/{required} missing")


def check_readme():
    print("readme:")
    if not os.path.isfile(README):
        return note("FAIL", "README.md missing")
    text = open(README, encoding="utf-8").read()
    if "by Owen" not in text:
        note("FAIL", "README.md lost the 'by Owen' attribution")
    else:
        print("  ok: attribution present")
    rel = set(re.findall(r'(?:src|href)="([^"#][^"]*)"', text))
    for ref in sorted(rel):
        if ref.startswith(("http://", "https://", "mailto:")):
            continue
        path = os.path.join(ROOT, ref.split("#")[0].split("?")[0])
        if os.path.exists(path):
            print(f"  ok: {ref}")
        else:
            note("FAIL", f"README references missing file: {ref}")
    if "assets/stats.svg" not in text:
        note("WARN", "README no longer embeds assets/stats.svg")
    return text


def check_stats_fresh():
    print("stats freshness:")
    try:
        data = json.load(open(os.path.join(ASSETS, "stats.json"), encoding="utf-8"))
        gen = data["generated_at"]
        import datetime as dt
        age = dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(gen)
        hours = age.total_seconds() / 3600
        if hours <= 48:
            print(f"  ok: stats.json generated {hours:.1f}h ago")
        else:
            note("WARN", f"stats.json is {hours:.0f}h old (daily Action should refresh it)")
    except Exception as e:
        note("FAIL", f"cannot read stats.json: {e}")


def check_embeds(text):
    print("embeds:")
    urls = sorted(set(re.findall(r'src="(https?://[^"]+)"', text)))
    for url in urls:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                code = r.status
            if code == 200:
                print(f"  ok: {url[:110]}")
            else:
                note("FAIL", f"{code} {url[:110]}")
        except Exception as e:
            note("FAIL", f"unreachable {url[:110]} ({e})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--embeds", action="store_true", help="also check third-party image URLs")
    ap.add_argument("--strict", action="store_true", help="warnings become failures")
    args = ap.parse_args()

    check_assets()
    text = check_readme()
    check_stats_fresh()
    if args.embeds and text:
        check_embeds(text)

    print(f"\nresult: {len(fails)} fail / {len(warns)} warn")
    if fails or (args.strict and warns):
        sys.exit(1)
    print("selftest: PASS")


if __name__ == "__main__":
    main()
