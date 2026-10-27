#!/usr/bin/env python3
"""outliers.py - rank posts by how far each beat its own account's median.

Stdlib only. Use python3 on macOS/Linux and python on Windows. Feed it posts as JSON (a list, or
an object with an "items"/"data"/"media" list, e.g. saved list_media output) or a CSV with a header.

    python3 outliers.py posts.json                       # your own account
    python3 outliers.py posts.csv --top 5
    python3 outliers.py posts.csv --group-by formula     # which hook formula wins (needs a formula column)
    python3 outliers.py niche.csv --group-by formula     # many accounts: each reel vs its own account
    python3 outliers.py posts.json --json > ranked.json

Baseline, per row, in this order:
  1. a "median" column (that account's median views, e.g. eyeballed from its last 12 reels)
  2. otherwise, when there's an "account" column, the median of that account's rows (3+ rows needed)
  3. otherwise, the median of the whole file (one account)

Field names are matched loosely (views / plays, shares / sends, saved / saves, ...).
Missing metrics show as "-" and are never guessed.
"""
import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DOT = chr(0x00B7)
ALIASES = {
    "id": ["id", "media_id", "shortcode"],
    "account": ["account", "username", "handle", "owner"],
    "type": ["media_product_type", "media_type", "type", "format"],
    "date": ["timestamp", "posted_at", "date", "created_time"],
    "caption": ["caption", "text", "title"],
    "hook": ["hook", "first_line"],
    "formula": ["formula", "hook_formula"],
    "length": ["length", "seconds", "duration"],
    "median": ["median", "account_median"],
    "views": ["views", "plays", "video_views", "impressions"],
    "reach": ["reach", "accounts_reached"],
    "likes": ["like_count", "likes", "likes_count"],
    "comments": ["comments_count", "comments", "comment_count"],
    "saves": ["saved", "saves", "save_count"],
    "shares": ["shares", "sends", "share_count"],
    "follows": ["follows", "new_followers"],
}
NUMERIC = ("views", "reach", "likes", "comments", "saves", "shares", "follows", "median", "length")


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
    for key in ALIASES.get(field, [field]):
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
    return [{k.lower().strip(): v for k, v in r.items()} for r in csv.DictReader(raw.splitlines())]


def ratio(a, b):
    return a / b if a is not None and b else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--group-by", default="", help="summarise by a column, e.g. formula, type, account, pillar")
    ap.add_argument("--json", action="store_true", help="print ranked rows as JSON")
    a = ap.parse_args()

    raw_rows = load(a.file)
    rows = []
    for r in raw_rows:
        p = {f: pick(r, f) for f in ALIASES}
        if a.group_by and a.group_by not in ALIASES:
            p[a.group_by] = r.get(a.group_by.lower())
        for f in NUMERIC:
            p[f] = num(p[f])
        p["caption"] = (p["caption"] or p["hook"] or "").replace("\n", " ").strip()
        rows.append(p)

    a.top = max(1, a.top)
    base_field = "views" if sum(1 for r in rows if r["views"]) >= max(3, len(rows) // 2) else "reach"
    usable = [r for r in rows if r[base_field]]
    skipped = len(rows) - len(usable)
    rows = usable

    # baseline per row: given median > per-account median > whole-file median
    by_account = defaultdict(list)
    for r in rows:
        by_account[r["account"] or ""].append(r[base_field])
    accounts = [k for k in by_account if k]
    whole = statistics.median([r[base_field] for r in rows]) if len(rows) >= 3 else None
    thin = set()
    for r in rows:
        if r["median"]:
            r["baseline"] = r["median"]
        elif r["account"] and len(by_account[r["account"]]) >= 3:
            r["baseline"] = statistics.median(by_account[r["account"]])
        elif r["account"] and len(accounts) > 1:
            r["baseline"] = None
            thin.add(r["account"])
        else:
            r["baseline"] = whole
    if not any(r["baseline"] for r in rows):
        print(f"Need at least 3 posts with {base_field} (or a median column); got {len(rows)}. "
              "For your own account, add insights (include_insights: true).")
        sys.exit(1)

    for r in rows:
        r["multiple"] = ratio(r[base_field], r["baseline"])
        r["send_rate"] = ratio(r["shares"], r["reach"])
        r["save_rate"] = ratio(r["saves"], r["reach"])
        r["comment_rate"] = ratio(r["comments"], r["reach"])
        r["follow_rate"] = ratio(r["follows"], r["reach"])

    ranked = sorted([r for r in rows if r["multiple"] is not None], key=lambda r: r["multiple"], reverse=True)
    if a.json:
        print(json.dumps(ranked, indent=2, ensure_ascii=False))
        return

    pct = lambda v: f"{v * 100:5.2f}%" if v is not None else "    - "
    mult = lambda v: f"{v:5.1f}x" if v is not None else "    - "
    multi = len(accounts) > 1
    basis = "each account's own median" if multi else f"median {base_field} {whole:,.0f}" if whole else "given medians"
    print(f"OUTLIERS  {DOT}  {len(ranked)} posts" + (f" from {len(accounts)} accounts" if multi else "") + f"  {DOT}  baseline: {basis}")
    if skipped:
        print(f"  ({skipped} post(s) had no {base_field} and were left out. Insights only come back for the first 25 items per page.)")
    if thin:
        print(f"  ({len(thin)} account(s) had fewer than 3 posts and no median column, so they were left out: {', '.join(sorted(thin))})")
    print("=" * 100)
    who = "ACCOUNT" if multi else "TYPE"
    print(f"  {'MULT':>6} {base_field.upper():>9}  {'SENDS/R':>7} {'SAVES/R':>7} {'CMT/R':>7}  {who:<14} CAPTION / HOOK")

    def show(r):
        b = r[base_field]
        tag = (r["account"] if multi else r["type"]) or "-"
        print(f"  {mult(r['multiple'])} {b:>9,.0f}  {pct(r['send_rate'])} {pct(r['save_rate'])} "
              f"{pct(r['comment_rate'])}  {str(tag)[:14]:<14} {r['caption'][:44]}")

    for r in ranked[: a.top]:
        show(r)
    if len(ranked) > a.top * 2:
        print("  " + DOT * 40)
    for r in ranked[max(a.top, len(ranked) - a.top):]:
        show(r)
    print("-" * 100)
    hits = [r for r in ranked if r["multiple"] >= 3]
    print(f"  {len(hits)} real outlier(s) at 3x+ baseline. Rank on multiple and sends/reach, not raw views.")

    if a.group_by:
        key = a.group_by
        groups = defaultdict(list)
        for r in ranked:
            groups[str(r.get(key) or "unlabelled")].append(r)
        print()
        print(f"BY {key.upper()}  {DOT}  median multiple, highest first")
        print("=" * 72)
        order = sorted(groups.items(), key=lambda kv: statistics.median([x["multiple"] for x in kv[1]]), reverse=True)
        for name, items in order:
            m = statistics.median([x["multiple"] for x in items])
            sends = [x["send_rate"] for x in items if x["send_rate"] is not None]
            s = f"{statistics.median(sends) * 100:5.2f}%" if sends else "    - "
            hit = sum(1 for x in items if x["multiple"] >= 3)
            flag = "   (n<3: anecdote, not a pattern)" if len(items) < 3 else ""
            print(f"  {m:5.1f}x  n={len(items):<3} 3x+={hit:<3} sends/reach {s}  {name[:30]}{flag}")
        n = len(ranked)
        verdict = "a pattern you can act on" if n >= 30 else "an early signal, keep collecting" if n >= 10 else "too few posts to conclude anything"
        print("-" * 72)
        print(f"  {n} posts: {verdict}.")


if __name__ == "__main__":
    main()
