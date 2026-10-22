"""Builds a set's training files from its step folders.
Usage: python tools/build_set.py sets/8047
Reads  steps/<folder>/annotation.json + notation.tbl in booklet_map.csv order.
Writes training.jsonl, training.tbl, preview.md, part_matches.csv (all generated, don't hand-edit)."""
import csv, json, sys
d = sys.argv[1].rstrip("/") + "/"
DEPTH = {(r["part_number"], r["point"]): (r["type"], float(r["depth_holes"])) for r in csv.DictReader(open("catalog/connections.csv", encoding="utf-8"))}
FIT = {"LOCKED": "locked (turn together)", "TURNS": "turns freely", "STIFF": "held stiff by friction"}
names = {}

def joins(notation):
    """CONNECT lines of one step -> list of exact joins, with depth from the catalog."""
    out = []
    for line in notation.split("\n"):
        t = line.split("#")[0].split()
        if t[:1] == ["ADD"]: names[t[1]] = t[2]
        if t[:1] != ["CONNECT"]: continue
        (a, _, pa), (b, _, pb) = t[1].partition("."), t[3].partition(".")
        ta, tb = DEPTH.get((names.get(a), pa)), DEPTH.get((names.get(b), pb))
        fit = next((x for x in t[4:] if x in FIT), None)
        out.append({"part": a, "point": pa, "point_type": ta[0] if ta else None,
                    "into": b, "into_point": pb, "into_type": tb[0] if tb else None,
                    "depth_holes": min(ta[1], tb[1]) if ta and tb else None,
                    "fit": FIT.get(fit), "exact": "?" not in pa + pb and bool(ta and tb)})
    return out
rows = list(csv.DictReader(open(d + "booklet_map.csv")))
side = {}  # side build -> its sub-steps' notation, inserted before "ATTACH <build>"
for r in rows:
    if r["build"] != "main":
        side.setdefault(r["build"], []).append(open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read().strip())
tbl, ann = [], []
for r in rows:
    e = json.load(open(f"{d}steps/{r['folder']}/annotation.json", encoding="utf-8"))
    e["answer"]["joins"] = joins(open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read())
    ann.append(e)
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
               "**Exact joins:** " + ("; ".join(f"{j['part']}.{j['point']} into {j['into']}.{j['into_point']}"
                                       + (f" ({j['depth_holes']:g} hole deep, {j['fit']})" if j["exact"] and j["fit"] else " (not fully shown in booklet)")
                                       for j in a["joins"]) or "none") + "\n",
               "**Who does what:** " + "; ".join(a["who_does_what_to_which"]) + "\n",
               "**After:** " + "; ".join(a["where_everything_is_after"]) + "\n",
               f"**Why:** {y['problem_solved']} {y['why_these_parts']} *Next:* {y['sets_up_for_later']} *Pattern:* {y['design_pattern']}\n"]
        if e["review_note"]: md.append(f"**Review:** {e['review_note']}\n")
open(d + "preview.md", "w", encoding="utf-8").write("\n".join(md))
print(f"{len(ann)} steps -> {d}training.jsonl, training.tbl, preview.md, part_matches.csv")
