"""Checks a set's build-language file against the parts catalog.
Usage: python tools/check_notation.py sets/8047/training.tbl
For every CONNECT a.point -> b.point [LOCKED|TURNS|STIFF] [DEPTH n]:
  - both parts were ADDed earlier (or are a GROUP)
  - each point exists on that part in catalog/connections.csv ('?' = not shown in the booklet, allowed but counted)
  - the two points fit: pin stop -> round hole, axle stop -> round or cross hole, bar -> small hole
  - LOCKED / TURNS / STIFF matches what the catalog says the pair does
Also: MESH only between parts with gear teeth."""
import csv, re, sys
from collections import Counter

points, info = {}, {}
for r in csv.DictReader(open("catalog/connections.csv", encoding="utf-8")):
    points.setdefault(r["part_number"], {})[r["point"]] = r["type"]
for r in csv.DictReader(open("catalog/technic_parts.csv", encoding="utf-8")):
    info[r["part_number"]] = r

def mode(t1, t2, parts):
    """Expected joint behaviour for two point types, or None if they don't fit."""
    pair = {t1, t2}
    if pair == {"axle stop (cross)", "axle hole (cross)"}: return "LOCKED"
    if pair == {"axle stop (cross)", "pin hole (round)"}: return "TURNS"
    if pair == {"pin stop (round)", "pin hole (round)"}:
        return "TURNS" if any(info.get(p, {}).get("friction") == "frictionless" for p in parts) else "STIFF"
    if pair == {"bar (3.2 mm)", "small hole (3.2 mm bar)"}: return "TURNS"
    return None

def check(path):
    names, groups, problems, unknown = {}, set(), [], Counter()
    step = "?"
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.split("#")[0].strip()
        if not line: continue
        t = line.split()
        where = f"line {n} (step {step})"
        if t[0] == "STEP": step = t[1]
        elif t[0] == "ADD": names[t[1]] = t[2]
        elif t[0] in ("GROUP", "ATTACH"): groups.add(t[1])
        elif t[0] == "CONNECT":
            a, b, extra = t[1], t[3], t[4:]
            ends = []
            for side in (a, b):
                name, _, pt = side.partition(".")
                if name in groups: ends.append(None); continue
                if name not in names: problems.append(f"{where}: '{name}' used before it is added"); ends.append(None); continue
                part = names[name]
                if "?" in pt: unknown["point not shown in booklet"] += 1; ends.append(None); continue
                if pt not in points.get(part, {}):
                    if part not in points: unknown[f"no catalog points for part {part}"] += 1
                    else: problems.append(f"{where}: {name} ({part}) has no point '{pt}'; it has {', '.join(sorted(points[part]))}")
                    ends.append(None); continue
                ends.append((part, points[part][pt]))
            if None in ends: continue
            m = mode(ends[0][1], ends[1][1], [ends[0][0], ends[1][0]])
            if m is None:
                problems.append(f"{where}: {a} ({ends[0][1]}) does not fit {b} ({ends[1][1]})")
                continue
            said = next((x for x in extra if x in ("LOCKED", "TURNS", "STIFF")), None)
            if said and said != m: problems.append(f"{where}: says {said} but {a} in {b} is {m}")
            if not said: unknown["CONNECT without LOCKED/TURNS/STIFF"] += 1
        elif t[0] == "MESH":
            for side in t[1:3]:
                name = side.split(".")[0]
                part = names.get(name)
                if part and not info.get(part, {}).get("gear_teeth") and info.get(part, {}).get("part_type") not in ("worm gear", "tread link"):
                    problems.append(f"{where}: MESH uses {name} ({part}), which has no gear teeth")
    return problems, unknown

if __name__ == "__main__":
    problems, unknown = check(sys.argv[1])
    print("\n".join(problems) or "All joins fit the catalog.")
    for k, v in unknown.items(): print(f"open: {v} x {k}")
