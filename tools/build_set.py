"""Builds a set's training files from its step folders.
Usage: python tools/build_set.py sets/8047
Reads  steps/<folder>/annotation.json + notation.tbl in booklet_map.csv order.
Also reads systems.json (what each part is for in the finished machine).
Writes training.jsonl, training.tbl, preview.md, part_matches.csv, roles.csv (all generated, don't hand-edit)."""
import csv, json, re, sys
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
# ---- big picture: every part's system, role, and every later step that uses it
systems = json.load(open(d + "systems.json", encoding="utf-8"))
role_of = {pat: (sy, role) for sy in systems["systems"] for pat, role in sy["parts"].items()}
def find_role(name):
    return role_of.get(name) or next((v for k, v in role_of.items() if re.fullmatch(k, name)), (None, None))
step_id = {r["folder"]: json.load(open(f"{d}steps/{r['folder']}/annotation.json", encoding="utf-8"))["example_id"] for r in rows}
added_in, later = {}, {}
for r in rows:
    for line in open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read().split("\n"):
        t = line.split("#")[0].split()
        if not t: continue
        if t[0] == "ADD": added_in.setdefault(t[1], r["folder"]); continue
        if t[0] not in ("DOES", "CONNECT", "MESH", "RATIO"): continue
        for n in {tok.split(".")[0] for tok in t[1:]}:
            if n in added_in and added_in[n] != r["folder"]:
                later.setdefault(n, []).append((step_id[r["folder"]], " ".join(t)))
missing = []
def big_picture(name):
    sy, role = find_role(name)
    if not sy: missing.append(name)
    return {"part": name, "system": sy and sy["name"], "role": role,
            "system_purpose": sy and sy["purpose"], "real_machine": sy and sy["real_machine"],
            "used_later": [{"step": s_, "line": l} for s_, l in later.get(name, [])],
            "feeds": [x["name"] for x in systems["systems"] if sy and x["id"] in sy["feeds"]]}

tbl, ann = [], []
for r in rows:
    e = json.load(open(f"{d}steps/{r['folder']}/annotation.json", encoding="utf-8"))
    e["answer"]["joins"] = joins(open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read())
    e["answer"]["big_picture"] = [big_picture(p["name"]) for p in e["answer"]["new_parts"]]
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
        md.append("**Big picture:**\n" + "\n".join(
            f"- **{b['part']}** ({b['system']}): {b['role']}"
            + (" Later: " + "; ".join(f"{u['step']} `{u['line']}`" for u in b["used_later"]) + "." if b["used_later"] else "")
            for b in a["big_picture"] if not re.fullmatch(r"tread-(?!1$|29$).*", b["part"])) + "\n")
        if e["review_note"]: md.append(f"**Review:** {e['review_note']}\n")
open(d + "preview.md", "w", encoding="utf-8").write("\n".join(md))
with open(d + "roles.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["part", "part_number", "added_in", "system", "role", "used_later_in", "system_purpose"])
    for e in ann:
        for p, b in zip(e["answer"]["new_parts"], e["answer"]["big_picture"]):
            w.writerow([p["name"], p["part_number"], e["example_id"], b["system"], b["role"],
                        "; ".join(f"{u['step']}: {u['line']}" for u in b["used_later"]), b["system_purpose"]])
if missing: print("NO ROLE in systems.json for:", ", ".join(missing))
print(f"{len(ann)} steps -> {d}training.jsonl, training.tbl, preview.md, part_matches.csv")
