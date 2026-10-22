"""Checks every labeled step against the set's parts list and the labeling rules.
Usage: python3 check_steps.py 03_training_data/8047.jsonl 04_reference/8047_parts_list.csv"""
import csv, json, re, sys
data, plist = sys.argv[1], sys.argv[2]
stock = {}
for r in csv.DictReader(open(plist)):
    stock[r["part_number"]] = stock.get(r["part_number"], 0) + int(r["qty"])
VERB = re.compile(r"\b(holds?|carr(y|ies)|spins? on|drives?|locks? .* in place|supports?)\b")
used, known, problems = {}, set(), []
for line in open(data):
    e = json.loads(line); s = e["step"]; a = e["answer"]
    box = sum(b["count"] for b in e["input"]["parts_box"])
    if box != len(a["new_parts"]):
        problems.append(f"step {s}: parts box has {box}, answer has {len(a['new_parts'])}")
    for p in a["new_parts"]:
        n = p["part_number"]
        if n not in stock: problems.append(f"step {s}: {n} not on parts list")
        used[n] = used.get(n, 0) + 1
        if used.get(n, 0) > stock.get(n, 0): problems.append(f"step {s}: too many {n}")
        known.add(p["name"])
    for d in a["who_does_what_to_which"]:
        if not VERB.search(d): problems.append(f"step {s}: no allowed verb in '{d}'")
        for nm in re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)*-(?:[A-Z]|\d+)\b", d):
            if nm not in known: problems.append(f"step {s}: '{nm}' used before it exists")
    for k in ("problem_solved", "why_these_parts", "sets_up_for_later", "design_pattern"):
        if not a["why"].get(k): problems.append(f"step {s}: missing why.{k}")
print("\n".join(problems) or "All checks passed.")
