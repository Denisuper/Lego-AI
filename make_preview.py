"""Rebuilds the readable preview and the part-matches table from a set's JSONL.
Usage: python make_preview.py 03_training_data/8047.jsonl"""
import csv, json, sys
src = sys.argv[1]
base = src[:-len(".jsonl")]
rows = [json.loads(l) for l in open(src, encoding="utf-8")]
md = [f"# {rows[0]['set']} - {len(rows)} labeled steps\n"]
with open(base + "_part_matches.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["example_id", "our_name", "part_number", "catalog_name", "color", "match"])
    for e in rows:
        a = e["answer"]
        for p in a["new_parts"]:
            w.writerow([e["example_id"], p["name"], p["part_number"], p["catalog_name"], p["color"], p["part_match"]])
        flag = " - NEEDS REVIEW" if e["needs_review"] else ""
        y = a["why"]
        md += [f"## {e['example_id']} (page {e['page']}) - {e['confidence']}{flag}\n",
               f"![{e['example_id']}](../{e['input']['picture']})\n",
               "**New parts:** " + "; ".join(f"{p['name']} ({p['part_number']}, {p['color'].lower()}) - {p['position']}" for p in a["new_parts"]) + "\n",
               "**Touches:** " + "; ".join(a["what_each_new_part_touches"]) + "\n",
               "**Who does what:** " + "; ".join(a["who_does_what_to_which"]) + "\n",
               "**After:** " + "; ".join(a["where_everything_is_after"]) + "\n",
               f"**Why:** {y['problem_solved']} {y['why_these_parts']} *Next:* {y['sets_up_for_later']} *Pattern:* {y['design_pattern']}\n"]
        if e["review_note"]:
            md.append(f"**Review:** {e['review_note']}\n")
open(base + "_preview.md", "w", encoding="utf-8").write("\n".join(md))
print(f"{len(rows)} steps -> {base}_preview.md, {base}_part_matches.csv")
