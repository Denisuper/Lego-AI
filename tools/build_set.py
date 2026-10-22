"""Builds a set's training files from its step folders.
Usage: python tools/build_set.py sets/8047
Reads  steps/<folder>/annotation.json + notation.tbl in booklet_map.csv order.
Writes training.jsonl, training.tbl, preview.md, part_matches.csv (all generated, don't hand-edit)."""
import csv, json, sys
d = sys.argv[1].rstrip("/") + "/"
rows = list(csv.DictReader(open(d + "booklet_map.csv")))
side = {}  # side build -> its sub-steps' notation, inserted before "ATTACH <build>"
for r in rows:
    if r["build"] != "main":
        side.setdefault(r["build"], []).append(open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read().strip())
tbl, ann = [], []
for r in rows:
    ann.append(json.load(open(f"{d}steps/{r['folder']}/annotation.json", encoding="utf-8")))
    if r["build"] != "main": continue
    for line in open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read().strip().split("\n"):
        g = line.split()[1] if line.startswith("ATTACH ") else None
        if g in side:
            tbl += [f"GROUP {g}", *"\n".join(side.pop(g)).split("\n"), "END"]
        tbl.append(line)
    tbl.append("")
assert not side, f"side builds never attached: {list(side)}"
open(d + "training.tbl", "w", encoding="utf-8", newline="\n").write("\n".join(tbl))
with open(d + "training.jsonl", "w", encoding="utf-8", newline="\n") as f:
    for e in ann: f.write(json.dumps(e) + "\n")

md = [f"# {ann[0]['set']} - {len(ann)} labeled steps\n"]
with open(d + "part_matches.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["example_id", "our_name", "part_number", "catalog_name", "color", "match"])
    for e in ann:
        a, y = e["answer"], e["answer"]["why"]
        for p in a["new_parts"]:
            w.writerow([e["example_id"], p["name"], p["part_number"], p["catalog_name"], p["color"], p["part_match"]])
        md += [f"## {e['example_id']} (page {e['page']}) - {e['confidence']}" + (" - NEEDS REVIEW" if e["needs_review"] else "") + "\n",
               f"![{e['example_id']}]({e['input']['picture']})\n",
               "**New parts:** " + "; ".join(f"{p['name']} ({p['part_number']}, {p['color'].lower()}) - {p['position']}" for p in a["new_parts"]) + "\n",
               "**Touches:** " + "; ".join(a["what_each_new_part_touches"]) + "\n",
               "**Who does what:** " + "; ".join(a["who_does_what_to_which"]) + "\n",
               "**After:** " + "; ".join(a["where_everything_is_after"]) + "\n",
               f"**Why:** {y['problem_solved']} {y['why_these_parts']} *Next:* {y['sets_up_for_later']} *Pattern:* {y['design_pattern']}\n"]
        if e["review_note"]: md.append(f"**Review:** {e['review_note']}\n")
open(d + "preview.md", "w", encoding="utf-8").write("\n".join(md))
print(f"{len(ann)} steps -> {d}training.jsonl, training.tbl, preview.md, part_matches.csv")
