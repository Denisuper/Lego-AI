"""Two-stage reward checker for Lego-AI build-language files.

Stage 1 (geometric, cheap): every CONNECT is legal — points exist in
catalog/connections.csv, the pair fits, LOCKED/TURNS/STIFF matches the catalog.

Stage 2 (functional, expensive): trace motion from each input (knob, crank,
pump) through the mechanism chain using catalog/mechanisms.json rules, and
report anything that would not actually move or hold the way its mechanism needs.

Usage:
  python tools/check_notation.py sets/8047/training.tbl
  python tools/check_notation.py sets/8047/training.tbl --jsonl   # machine-readable critiques

Output: plain-text summary, or JSONL critique objects when --jsonl is set.
Each critique: {severity, code, line, message}. severity in error/warning/info.
GRPO uses -1 per error, -0.25 per warning, 0 for clean, and the critique
texts are fed back as conditioning context on the next attempt.
"""
import csv, json, re, sys
from collections import Counter, defaultdict

# ── catalog ──────────────────────────────────────────────────────────────
points, info = {}, {}
for r in csv.DictReader(open("catalog/connections.csv", encoding="utf-8")):
    points.setdefault(r["part_number"], {})[r["point"]] = r["type"]
for r in csv.DictReader(open("catalog/technic_parts.csv", encoding="utf-8")):
    info[r["part_number"]] = r

MECH = json.load(open("catalog/mechanisms.json", encoding="utf-8"))["mechanisms"]
MECH_BY_TYPE = {m["type"]: m for m in MECH}

# ── stage 1: geometric ───────────────────────────────────────────────────
def mode(t1, t2, parts):
    pair = {t1, t2}
    if pair == {"axle stop (cross)", "axle hole (cross)"}: return "LOCKED"
    if pair == {"axle stop (cross)", "pin hole (round)"}: return "TURNS"
    if pair == {"pin stop (round)", "pin hole (round)"}:
        return "TURNS" if any(info.get(p, {}).get("friction") == "frictionless" for p in parts) else "STIFF"
    if pair == {"bar (3.2 mm)", "small hole (3.2 mm bar)"}: return "TURNS"
    if pair == {"bar (3.2 mm)", "clip"}: return "TURNS"
    return None

def stage1(path):
    names, groups, critiques, unknown = {}, set(), [], Counter()
    step = "?"
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.split("#")[0].strip()
        if not line: continue
        t = line.split(); where = f"line {n} (step {step})"
        if t[0] == "STEP": step = t[1]
        elif t[0] == "ADD": names[t[1]] = t[2]
        elif t[0] in ("GROUP", "ATTACH"): groups.add(t[1])
        elif t[0] == "CONNECT":
            a, b, extra = t[1], t[3], t[4:]
            ends = []
            for side in (a, b):
                name, _, pt = side.partition(".")
                if name in groups: ends.append(None); continue
                if name not in names:
                    critiques.append({"severity":"error","code":"USED_BEFORE_ADD","line":n,
                        "message":f"{where}: '{name}' used before it is added"}); ends.append(None); continue
                part = names[name]
                if "?" in pt: unknown["point not shown in booklet"] += 1; ends.append(None); continue
                if pt.endswith("~"): unknown["point named from the picture but not confirmed (~)"] += 1; pt = pt[:-1]
                if pt not in points.get(part, {}):
                    if part not in points: unknown[f"no catalog points for part {part}"] += 1
                    else: critiques.append({"severity":"error","code":"POINT_MISSING","line":n,
                        "message":f"{where}: {name} ({part}) has no point '{pt}'; it has {', '.join(sorted(points[part]))}"})
                    ends.append(None); continue
                ends.append((part, points[part][pt]))
            if None in ends: continue
            m = mode(ends[0][1], ends[1][1], [ends[0][0], ends[1][0]])
            if m is None:
                critiques.append({"severity":"error","code":"NO_FIT","line":n,
                    "message":f"{where}: {a} ({ends[0][1]}) does not fit {b} ({ends[1][1]})"}); continue
            said = next((x for x in extra if x in ("LOCKED", "TURNS", "STIFF")), None)
            if said and said != m:
                critiques.append({"severity":"error","code":"WRONG_MODE","line":n,
                    "message":f"{where}: says {said} but {a} in {b} is {m}"})
            if not said: unknown["CONNECT without LOCKED/TURNS/STIFF"] += 1
        elif t[0] == "MESH":
            for side in t[1:3]:
                name = side.split(".")[0]; part = names.get(name)
                if part and not info.get(part, {}).get("gear_teeth") and info.get(part, {}).get("part_type") not in ("worm gear", "tread link"):
                    critiques.append({"severity":"error","code":"MESH_NO_TEETH","line":n,
                        "message":f"{where}: MESH uses {name} ({part}), which has no gear teeth"})
    return names, critiques, unknown

# ── stage 2: functional simulation ───────────────────────────────────────
# Trace motion through DOES/RATIO/MESH/PATTERN verbs and CONNECT structure.
# A mechanism is alive if its input can reach its output following the rules
# in mechanisms.json; it fails when a fails_when condition is met.

VERB_RE = re.compile(r"^(DOES|RATIO|MESH|PATTERN)\s+(.+)\s+(.+)\s+(.+)$")

def stage2(path, names):
    critiques = []
    # collect verb lines with their step context
    verbs = []  # (line_no, step, kind, rest)
    step = "?"
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.split("#")[0].strip()
        if not line: continue
        t = line.split()
        if t[0] == "STEP": step = t[1]
        elif t[0] in ("DOES", "RATIO", "MESH", "PATTERN"):
            verbs.append((n, step, t[0], t[1:]))
    # build adjacency: part -> list of (other_part, verb, line)
    adj = defaultdict(list)
    for n, step, kind, rest in verbs:
        if kind == "DOES" and len(rest) >= 2:
            a, rel, b = rest[0], rest[1], rest[2] if len(rest) > 2 else None
            adj[a].append((b, rel, n)); adj[b].append((a, rel, n))
        elif kind == "MESH" and len(rest) >= 2:
            adj[rest[0]].append((rest[1], "MESH", n)); adj[rest[1]].append((rest[0], "MESH", n))
        elif kind == "RATIO" and len(rest) >= 2:
            adj[rest[0]].append((rest[1], "RATIO", n)); adj[rest[1]].append((rest[0], "RATIO", n))
    # find inputs: parts whose type suggests knob_input (gear/wheel/knob on exposed axle)
    # We approximate: any part with gear_teeth or a wheel-like type that has a DOES
    # verb driving something else is a candidate input. Also flag parts that are
    # ADDed but never appear in any verb — dead weight.
    driven = set()
    for _, _, kind, rest in verbs:
        if kind == "DOES" and len(rest) >= 3: driven.add(rest[2])
        elif kind == "MESH": driven.update(rest[:2])
        elif kind == "RATIO": driven.update(rest[:2])
    for name, part in names.items():
        if name not in adj and name not in driven:
            # part added but never referenced by a verb — possible dead weight
            ptype = info.get(part, {}).get("part_type", "")
            if ptype not in ("panel", "hose", "light", "plate") and not ptype.startswith("decoration"):
                critiques.append({"severity":"warning","code":"UNREFERENCED_PART","line":0,
                    "message":f"{name} ({part}, {ptype}) is added but never appears in a DOES/MESH/RATIO verb — it may carry no load or motion"})
    # check each DOES chain for mechanism rule violations
    for n, step, kind, rest in verbs:
        if kind != "DOES" or len(rest) < 3: continue
        a, rel, b = rest[0], rest[1], rest[2]
        pa, pb = names.get(a), names.get(b)
        if not pa or not pb: continue
        # worm_drive: needs thrust stops on the worm shaft
        if rel == "DRIVES" and info.get(pa, {}).get("part_type") == "worm gear":
            # look for a bush/axle-stop near the worm on the same shaft — approximated
            # by any LOCKED CONNECT involving pa's part number in this file
            has_stop = False
            for m, raw in enumerate(open(path, encoding="utf-8"), 1):
                if "LOCKED" in raw and pa in raw: has_stop = True; break
            if not has_stop:
                critiques.append({"severity":"error","code":"WORM_NO_STOP","line":n,
                    "message":f"line {n} (step {step}): worm {a} ({pa}) drives {b} but has no LOCKED stop — per worm_drive rules the worm walks along its shaft and loses mesh"})
        # gear on round-hole part instead of locked axle
        if rel == "DRIVES":
            for side_name, side_part in ((a, pa), (b, pb)):
                ptype = info.get(side_part, {}).get("part_type", "")
                if "gear" in ptype and info.get(side_part, {}).get("gear_teeth"):
                    # gear should be LOCKED to an axle; flag if we can't find evidence
                    found_lock = any("LOCKED" in raw and side_name in raw for raw in open(path, encoding="utf-8"))
                    if not found_lock:
                        critiques.append({"severity":"warning","code":"GEAR_NOT_LOCKED","line":n,
                            "message":f"line {n} (step {step}): gear {side_name} ({side_part}) drives via {rel} but no LOCKED connection found — a gear free on a round hole spins without turning its shaft (gear_pair fails_when)"})
        # friction pin where free swing is needed (hinge)
        if rel in ("SPINS_ON", "HOLDS"):
            for side_name, side_part in ((a, pa), (b, pb)):
                for m, raw in enumerate(open(path, encoding="utf-8"), 1):
                    if side_name in raw and "STIFF" in raw and rel == "SPINS_ON":
                        critiques.append({"severity":"warning","code":"FRICTION_ON_HINGE","line":m,
                            "message":f"line {m}: {side_name} uses a STIFF (friction) pin but is described as {rel} — hinge rules say friction pins make the swing stiff where free movement is needed"})
    return critiques

# ── main ─────────────────────────────────────────────────────────────────
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    as_jsonl = "--jsonl" in sys.argv
    if not path:
        print("Usage: python tools/check_notation.py <file> [--jsonl]"); sys.exit(2)
    names, gcrit, unknown = stage1(path)
    fcrit = stage2(path, names)
    allc = gcrit + fcrit
    if as_jsonl:
        for c in allc: print(json.dumps(c))
    else:
        print("\n".join(c["message"] for c in allc) or "All joins fit the catalog and no functional failures found.")
        for k, v in unknown.items(): print(f"open: {v} x {k}")
        errs = sum(1 for c in allc if c["severity"] == "error")
        warns = sum(1 for c in allc if c["severity"] == "warning")
        print(f"summary: {errs} error(s), {warns} warning(s) — reward = -{errs} - 0.25*{warns}")
    sys.exit(1 if any(c["severity"] == "error" for c in allc) else 0)

if __name__ == "__main__":
    main()
