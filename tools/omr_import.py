"""Builds a set's step folders from its official LDraw 3D model (OMR .mpd).
Usage: python tools/omr_import.py <set number> <model.mpd> <ldraw dir> <LDCad shadow dir> [rebrickable parts.csv]
Every part gets its exact position (POS line) and every join is found from the geometry: a pin or axle stop
that sits inside a hole of a part already placed becomes a CONNECT line with catalog point names and LOCKED/TURNS/STIFF.
Gear pairs at the right spacing become MESH + RATIO lines.
Writes sets/<set>/booklet_map.csv and sets/<set>/steps/<build>-NN/{notation.tbl, annotation.json}.
The reasoning fields (why, systems.json, mechanisms.json) are left to write by hand: they say TO WRITE."""
import csv, json, os, re, sys
sys.path.insert(0, "tools")
import build_connections as bc
from check_notation import mode

SET, MPD, LD, SH = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
RB = {r["part_num"]: r["name"] for r in csv.DictReader(open(sys.argv[5], encoding="utf-8"))} if len(sys.argv) > 5 else {}
bc.init(LD, SH)
OUT = f"sets/{SET}/"
CAT = {r["part_number"]: r for r in csv.DictReader(open("catalog/technic_parts.csv", encoding="utf-8"))}

# LDraw colour codes -> names
COLORS = {}
for l in open(LD + "/LDConfig.ldr", encoding="utf-8", errors="ignore"):
    m = re.match(r"0 !COLOUR (\S+)\s+CODE\s+(\d+)", l)
    if m: COLORS[m.group(2)] = m.group(1).replace("_", " ")

# ---- read the model: files -> list of steps -> list of (kind, name, color, matrix, offset)
files, order, cur = {}, [], None
for raw in open(MPD, encoding="utf-8", errors="ignore"):
    t = raw.split()
    if not t: continue
    if t[:2] == ["0", "FILE"]:
        cur = " ".join(t[2:]).lower(); files[cur] = [[]]; order.append(cur); continue
    if cur is None: continue
    if t[:2] in (["0", "STEP"], ["0", "ROTSTEP"]):
        files[cur].append([]); continue
    if t[0] == "1" and len(t) >= 15:
        x, y, z = map(float, t[2:5]); M = list(map(float, t[5:14])); ref = " ".join(t[14:]).lower()
        files[cur][-1].append((ref, t[1], M, [x, y, z]))
for f in files: files[f] = [s for s in files[f] if s]
MAIN = order[0]


def slug(f):
    s = re.sub(r"\.ldr$", "", f.split(" - ", 1)[-1])
    return re.sub(r"[^a-z0-9]+", "", s)[:12] or "sub"


# ---- part names: short type + counter
count = {}
def ldraw_file(num):
    """The 3D file for a part number, trying variant suffixes (33299 -> 33299a)."""
    for t in (num, num + "a", num + "b", num + "c"):
        if bc.find(bc.LDI, t + ".dat"): return t + ".dat"
    return None

def ldraw_title(num):
    p = bc.find(bc.LDI, ldraw_file(num) or "")
    if not p: return RB.get(num, num)
    return open(p, encoding="utf-8", errors="ignore").readline()[2:].strip().lstrip("~=_")

def name_for(num):
    c = CAT.get(num, {})
    n = c.get("name") or ldraw_title(num)
    if not c and re.search(r"Tyre|Tire", n): base = "tyre"
    elif not c and "Wheel" in n and "Steering" not in n: base = "wheel"
    elif not c and "Steering" in n: base = "steeringwheel"
    elif not c and "Bucket" in n: base = "bucket"
    elif c.get("gear_teeth"): base = "gear" + c["gear_teeth"].replace("/", "-")
    elif "Worm" in n: base = "worm"
    elif "Bush" in n: base = "bush"
    elif re.search(r"Axle (\d+(\.\d+)?)", n) and "Pin" not in n and "Connector" not in n:
        base = "axle" + re.search(r"Axle (\d+(\.\d+)?)", n).group(1).replace(".", "")
    elif "Pin" in n and "Connector" not in n: base = "pin"
    elif re.search(r"Beam (\d+) x (\d+)", n): base = "beam" + "x".join(re.search(r"Beam (\d+) x (\d+)", n).groups())
    elif re.search(r"Beam 1 x (\d+)", n): base = "beam" + re.search(r"Beam 1 x (\d+)", n).group(1)
    elif "Connector" in n: base = "conn"
    elif "Panel" in n or "Fairing" in n: base = "panel"
    else: base = re.sub(r"[^a-z]+", "", n.split()[-1].lower())[:8] or "part"
    count[base] = count.get(base, 0) + 1
    return f"{base}-{count[base]}"


def mul(A, B): return [sum(A[r*3+k]*B[k*3+c] for k in range(3)) for r in range(3) for c in range(3)]
def app(A, v): return [sum(A[r*3+k]*v[k] for k in range(3)) for r in range(3)]
def add(a, b): return [x + y for x, y in zip(a, b)]
def sub(a, b): return [x - y for x, y in zip(a, b)]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def norm(a): return dot(a, a) ** .5


POINT_CACHE = {}
def points_of(num):
    if num not in POINT_CACHE:
        f = ldraw_file(num)
        POINT_CACHE[num] = bc.named_points(f) if f else ([], None)
    return POINT_CACHE[num]


class Placed:
    def __init__(self, name, num, color, M, t):
        self.name, self.num, self.color, self.M, self.t = name, num, color, M, t
        pts, self.bbox = points_of(num)
        self.points = [(pn, typ, add(app(M, p), t), [c / (norm(app(M, u)) or 1) for c in app(M, u)], depth, rad)
                       for pn, typ, p, u, depth, rad, slide in pts]


MALE = ("pin stop (round)", "axle stop (cross)", "bar (3.2 mm)")
FEMALE = ("pin hole (round)", "axle hole (cross)", "small hole (3.2 mm bar)", "clip")


def find_joins(new, others):
    """Joins between parts in `new` and parts in `new` + `others`: each hole gets the stop sitting in it."""
    pool = new + others
    out, seen = [], set()
    for a in pool:
        for b in pool:
            if a is b or (a not in new and b not in new): continue  # at least one of the two is new this step
            for pa in a.points:
                if pa[1] not in FEMALE: continue
                best = None
                for pb in b.points:
                    if pb[1] not in MALE or mode(pa[1], pb[1], [a.num, b.num]) is None: continue
                    if abs(dot(pa[3], pb[3])) < 0.9: continue
                    d = sub(pb[2], pa[2]); along = dot(d, pa[3]); perp = norm(sub(d, [along * c for c in pa[3]]))
                    if perp > 3 or abs(along) > pa[4] / 2 + 6: continue
                    score = perp + abs(along)
                    if best is None or score < best[0]: best = (score, pb)
                if best:
                    key = (b.name, best[1][0], a.name, pa[0])
                    if key not in seen:
                        seen.add(key)
                        out.append((b, best[1], a, pa))
    return out


def gear_meshes(new, others):
    out = []
    gears = [p for p in new + others if CAT.get(p.num, {}).get("gear_teeth", "").isdigit()]
    for g in [p for p in new if p in gears]:
        for h in gears:
            if h is g or (h in new and h.name < g.name): continue
            ta, tb = int(CAT[g.num]["gear_teeth"]), int(CAT[h.num]["gear_teeth"])
            ag = next((q[3] for q in g.points if q[1] == "axle hole (cross)"), None)
            ah = next((q[3] for q in h.points if q[1] == "axle hole (cross)"), None)
            if not ag or not ah or abs(dot(ag, ah)) < 0.95: continue
            d = norm(sub(g.t, h.t)); want = (ta + tb) / 16 * 20
            if abs(d - want) <= 2.5 and abs(dot(sub(g.t, h.t), ag)) < 3:
                out.append((h, g, tb, ta))
    return out


def fmt(v): return f"{round(v / 20 * 20) / 20:g}"


JOINED = set()
placed_by_ctx = {}   # context file -> list of Placed (in that file's frame)
steps_out = []       # (folder, build, step no, attaches_at, notation lines, annotation dict)
built = {}           # submodel file -> (folder build name, list of Placed in its own frame)
sub_counter = {}


def build_file(f, build):
    """Emit steps of file f (recursively building submodels first). Returns placed parts in f's frame."""
    ctx = []
    for i, step in enumerate(files[f], 1):
        new, attach_lines, attached = [], [], []
        for ref, color, M, t in step:
            if ref in files:  # side build used here
                if ref not in built:
                    b = slug(ref); sub_counter[b] = sub_counter.get(b, 0) + 1
                    built[ref] = (b, build_file(ref, b))
                b, parts = built[ref]
                attach_lines.append(b)
                attached += [Placed(p.name, p.num, p.color, mul(M, p.M), add(app(M, p.t), t)) for p in parts]
                continue
            num = re.sub(r"\.dat$", "", ref)
            new.append(Placed(name_for(num), num, color, M, t))
        lines = []
        for p in new:
            lines.append(f"ADD {p.name} {p.num} {COLORS.get(p.color, 'color' + p.color).lower().replace(' ', '')}")
            lines.append(f"POS {p.name} {fmt(p.t[0])} {fmt(p.t[1])} {fmt(p.t[2])} " + " ".join(f"{round(c, 3):g}" for c in p.M))
        for g in attach_lines:
            lines.append(f"ATTACH {g}")
        joins = find_joins(new + attached, [p for p in ctx])
        for mpart, mpt, fpart, fpt in joins:
            m = mode(mpt[1], fpt[1], [mpart.num, fpart.num])
            lines.append(f"CONNECT {mpart.name}.{mpt[0]} -> {fpart.name}.{fpt[0]} {m}")
        for h, g, th, tg in gear_meshes(new + attached, ctx):
            lines += [f"MESH {h.name}.teeth {g.name}.teeth", f"RATIO {h.name} {g.name} {th}/{tg}"]
        for j in joins: JOINED.update((j[0].name, j[2].name))
        ctx += new + attached
        steps_out.append((build, i, new, attached, joins, lines))
    return ctx


build_file(MAIN, "main")

# ---- write step folders
os.makedirs(OUT + "steps", exist_ok=True)
attach_at = {}
for build, i, new, attached, joins, lines in steps_out:
    if build == "main":
        for l in lines:
            if l.startswith("ATTACH "): attach_at[l.split()[1]] = i
rows = []
setname = f"LEGO Technic {SET}"
for n, (build, i, new, attached, joins, lines) in enumerate(steps_out, 1):
    folder = f"{build}-{i:02d}"
    d = f"{OUT}steps/{folder}/"
    os.makedirs(d, exist_ok=True)
    head = [f"STEP {i}"] if build == "main" else []
    open(d + "notation.tbl", "w", encoding="utf-8", newline="\n").write("\n".join(head + lines) + "\n")
    eid = f"{SET}-step-{i:02d}" if build == "main" else f"{SET}-{build}-step-{i:02d}"
    touches = [f"{m.name}'s {mp[0]} goes into {f.name}'s {fp[0]} ({mode(mp[1], fp[1], [m.num, f.num]).lower()})" for m, mp, f, fp in joins]
    does = []
    for m, mp, f, fp in joins:
        md = mode(mp[1], fp[1], [m.num, f.num])
        if md == "LOCKED": does.append(f"{m.name} carries {f.name}" if mp[1].startswith("axle") else f"{f.name} holds {m.name}")
        elif md == "TURNS": does.append(f"{m.name} spins on {f.name}" if "pin" in mp[1] else f"{f.name} spins on {m.name}")
        else: does.append(f"{f.name} holds {m.name}")
    ann = {"example_id": eid, "set": setname, "page": None, "step": i,
           "input": {"picture": None, "parts_box": [{"name": p.name, "part_number": p.num, "count": 1} for p in new], "model_so_far": "TO WRITE"},
           "answer": {"new_parts": [{"name": p.name, "part_number": p.num, "catalog_name": CAT.get(p.num, {}).get("name") or ldraw_title(p.num),
                                     "color": COLORS.get(p.color, p.color), "part_match": "confirmed (official 3D model)",
                                     "position": f"at x={fmt(p.t[0])}, y={fmt(p.t[1])}, z={fmt(p.t[2])} holes (exact, from the 3D model)",
                                     "rotation": "TO WRITE"} for p in new],
                      "what_each_new_part_touches": touches or ["attaches the side build"] if attached else touches,
                      "who_does_what_to_which": list(dict.fromkeys(does)),
                      "where_everything_is_after": ["TO WRITE"],
                      "why": {"problem_solved": "TO WRITE", "why_these_parts": "TO WRITE", "sets_up_for_later": "TO WRITE", "design_pattern": "TO WRITE"}},
           "confidence": "high", "needs_review": False, "review_note": "Joins and positions computed from the official LDraw 3D model."}
    json.dump(ann, open(d + "annotation.json", "w", encoding="utf-8", newline="\n"), indent=2)
    rows.append([n, folder, build, i, "", attach_at.get(build, "") if build != "main" else ""])
with open(OUT + "booklet_map.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["order", "folder", "build", "step", "page", "attaches_at_main_step"]); w.writerows(rows)
nj = sum(len(s[4]) for s in steps_out); nparts = sum(len(s[2]) for s in steps_out)
never = [p.name for s_ in steps_out for p in s_[2] if p.name not in JOINED]
print(f"{SET}: {len(steps_out)} steps, {nparts} parts, {nj} joins found")
if never: print("never joined (check by hand):", ", ".join(never))
