#!/usr/bin/env python3
"""outliers.py - rank posts by how far each beat the account's own median.

Stdlib only. Feed it the posts as JSON (a list, or an object with an "items"/"data"/"media"
list - e.g. saved list_media output) or a CSV with a header row.

    python3 outliers.py posts.json
    python3 outliers.py posts.csv --top 5
    python3 outliers.py posts.json --json > ranked.json

Field names are matched loosely (views / plays / video_views, shares / sends, saved / saves, ...).
Missing metrics are shown as "-" and never guessed.
"""
import argparse
import csv
import json
import statistics
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ALIASES = {
    "id": ["id", "media_id", "shortcode"],
    "type": ["media_product_type", "media_type", "type", "format"],
    "date": ["timestamp", "posted_at", "date", "created_time"],
    "caption": ["caption", "text", "title"],
    "views": ["views", "plays", "video_views", "impressions"],
    "reach": ["reach", "accounts_reached"],
    "likes": ["like_count", "likes", "likes_count"],
    "comments": ["comments_count", "comments", "comment_count"],
    "saves": ["saved", "saves", "save_count"],
    "shares": ["shares", "sends", "share_count"],
    "follows": ["follows", "new_followers"],
}


def flatten(d):
    out = {}
    # Top-level keys win; nested blocks (e.g. "insights": {...}) only fill gaps.
    nested = {}
    for k, v in d.items():
        if isinstance(v, dict):
            nested.update(flatten(v))
        else:
            out[k.lower()] = v
    for k, v in nested.items():
        out.setdefault(k, v)
    return out


def pick(row, field):
    for key in ALIASES[field]:
        v = row.get(key)
        if v not in (None, ""):
            return v
    return None


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except (TypeError, ValueError):
        return None


def load(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8-sig").read()
    s = raw.lstrip()
    if s.startswith("[") or s.startswith("{"):
        data = json.loads(s)
        if isinstance(data, dict):
            for k in ("items", "data", "media", "posts", "results"):
                if isinstance(data.get(k), list):
                    data = data[k]
                    break
        return [flatten(r) for r in data if isinstance(r, dict)]
    return [{k.lower(): v for k, v in r.items()} for r in csv.DictReader(raw.splitlines())]


def ratio(a, b):
    return a / b if a is not None and b else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--json", action="store_true", help="print ranked rows as JSON")
    a = ap.parse_args()

    rows = []
    for r in load(a.file):
        p = {f: pick(r, f) for f in ALIASES}
        for f in ("views", "reach", "likes", "comments", "saves", "shares", "follows"):
            p[f] = num(p[f])
        p["caption"] = (p["caption"] or "").replace("\n", " ").strip()
        rows.append(p)

    a.top = max(1, a.top)
    base_field = "views" if sum(1 for r in rows if r["views"]) >= max(3, len(rows) // 2) else "reach"
    vals = [r[base_field] for r in rows if r[base_field]]
    if len(vals) < 3:
        print(f"Need at least 3 posts with {base_field}; got {len(vals)}. Add insights (include_insights: true).")
        sys.exit(1)
    median = statistics.median(vals)
    skipped = len(rows) - len(vals)
    rows = [r for r in rows if r[base_field]]

    for r in rows:
        r["multiple"] = ratio(r[base_field], median)
        r["send_rate"] = ratio(r["shares"], r["reach"])
        r["save_rate"] = ratio(r["saves"], r["reach"])
        r["comment_rate"] = ratio(r["comments"], r["reach"])

    ranked = sorted(rows, key=lambda r: (r["multiple"] or 0), reverse=True)
    if a.json:
        print(json.dumps(ranked, indent=2, ensure_ascii=False))
        return

    pct = lambda v: f"{v * 100:5.2f}%" if v is not None else "    - "
    mult = lambda v: f"{v:5.1f}x" if v is not None else "    - "
    print(f"OUTLIERS  ·  {len(rows)} posts  ·  baseline: median {base_field} {median:,.0f}")
    if skipped:
        print(f"  ({skipped} post(s) had no {base_field} and were left out. Insights only come back for the first 25 items per page.)")
    print("=" * 96)
    print(f"  {'MULT':>6} {base_field.upper():>9}  {'SENDS/R':>7} {'SAVES/R':>7} {'CMT/R':>7}  {'TYPE':<10} CAPTION")

    def show(r):
        b = r[base_field]
        print(f"  {mult(r['multiple'])} {b if b is None else f'{b:,.0f}':>9}  {pct(r['send_rate'])} {pct(r['save_rate'])} "
              f"{pct(r['comment_rate'])}  {str(r['type'] or '-')[:10]:<10} {r['caption'][:44]}")

    for r in ranked[: a.top]:
        show(r)
    if len(ranked) > a.top * 2:
        print("  " + "·" * 40)
    for r in ranked[max(a.top, len(ranked) - a.top):]:
        show(r)
    print("-" * 96)
    hits = [r for r in rows if (r["multiple"] or 0) >= 3]
    print(f"  {len(hits)} real outlier(s) at 3x+ median. Rank on multiple and sends/reach, not raw views.")


if __name__ == "__main__":
    main()
