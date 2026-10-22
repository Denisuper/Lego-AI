"""Reads the LDraw 3D part files + LDCad snap data and writes, for every catalog part:
  catalog/connections.csv   one row per hole / pin / axle: type, position, direction, depth
  catalog/technic_parts.csv adds size, thickness, counts and a plain-English description
Usage: python tools/build_connections.py <ldraw dir> <LDCadShadowLibrary dir>
  ldraw:  https://library.ldraw.org/library/updates/complete.zip
  shadow: https://github.com/RolandMelkert/LDCadShadowLibrary (download the zip)
Units: holes (1 hole = 20 LDraw units = 8 mm). Every hole, pin stop and axle stop gets a point name (hole1.., axlehole1.., pin1.., axle1..)
numbered along the part's longest direction; instructions name these points."""
import csv, os, re, sys
from functools import lru_cache

LD, SH = sys.argv[1], sys.argv[2]
CAT = "catalog/technic_parts.csv"

def index(*dirs):
    idx = {}
    for root in dirs:
        for dp, _, fs in os.walk(root):
            for f in fs:
                if f.lower().endswith(".dat"):
                    rel = os.path.relpath(os.path.join(dp, f), root).replace("\\", "/").lower()
                    for key in (rel, rel.split("/", 1)[-1]):  # "parts/s/x.dat" -> also "s/x.dat"
                        idx.setdefault(key, os.path.join(dp, f))
    return idx
LDI, SHI = index(LD + "/parts", LD + "/p"), index(SH + "/parts", SH + "/p")
find = lambda idx, name: idx.get(name.replace("\\", "/").lower())

def mul(A, B):  # 3x3 row-major
    return [sum(A[r*3+k]*B[k*3+c] for k in range(3)) for r in range(3) for c in range(3)]
def app(A, v): return [sum(A[r*3+k]*v[k] for k in range(3)) for r in range(3)]
I3 = [1, 0, 0, 0, 1, 0, 0, 0, 1]

def props(line):
    return {k.lower(): v.strip() for k, v in re.findall(r"\[(\w+)=([^\]]*)\]", line)}

def snaps_of(name):
    """LDCad snap lines for one file: list of (kind, props)."""
    p = find(SHI, name)
    if not p: return []
    out = []
    for l in open(p, encoding="utf-8", errors="ignore"):
        m = re.match(r"\s*0 !LDCAD (SNAP_\w+)(.*)", l)
        if m: out.append((m.group(1), props(m.group(2))))
    return out

def grid_offsets(g):
    """LDCad grid: [C] nx [C] nz sx sz  or  [C] nx [C] ny [C] nz sx sy sz  (C = centered) -> list of (x, y, z) offsets."""
    if not g: return [(0, 0, 0)]
    t, cen, nums = g.split(), [], []
    for tok in t:
        if tok.upper() == "C": cen.append(len(nums)); continue
        nums.append(float(tok))
    n = len(nums) // 2
    counts, steps = [int(x) for x in nums[:n]], nums[n:]
    axes = [0, 2] if n == 2 else [0, 1, 2]
    ranges = []
    for i, (c, st) in enumerate(zip(counts, steps)):
        o = -(c - 1) * st / 2 if i in cen else 0
        ranges.append([o + k * st for k in range(c)])
    out = [[0, 0, 0]]
    for ax, rng in zip(axes, ranges):
        out = [v[:ax] + [d] + v[ax + 1:] for v in out for d in rng]
    return [tuple(v) for v in out]

@lru_cache(None)
def resolve(name, depth=0):
    """Connection points of a file in its own coordinates: tuple of (id, gender, secs, pos, axis, scale_y, slide)."""
    p = find(LDI, name)
    if depth > 30: return ()
    pts = []
    if p:  # inherited from sub-files
        for l in open(p, encoding="utf-8", errors="ignore"):
            t = l.split()
            if len(t) >= 15 and t[0] == "1":
                x, y, z, *M = map(float, t[2:14]); sub = " ".join(t[14:])
                for pid, g, secs, pos, ax, sy, sl in resolve(sub, depth + 1):
                    pts.append((pid, g, secs, [a + b for a, b in zip(app(M, pos), (x, y, z))], app(M, ax), sy * norm(app(M, [0, 1, 0])), sl))
    for kind, pr in snaps_of(name):
        if kind == "SNAP_CLEAR":
            drop = pr.get("id")
            pts = [q for q in pts if drop and (q[0] or "").lower() != drop.lower()]
        elif kind == "SNAP_INCL":
            pos = list(map(float, pr.get("pos", "0 0 0").split())); M = list(map(float, pr.get("ori", " ".join(map(str, I3))).split()))
            for go in grid_offsets(pr.get("grid")):
                for pid, g, secs, q, ax, sy, sl in resolve(pr["ref"], depth + 1):
                    pts.append((pid, g, secs, [a + b + c for a, b, c in zip(app(M, q), pos, go)], app(M, ax), sy, sl))
        elif kind == "SNAP_CYL":
            pos = list(map(float, pr.get("pos", "0 0 0").split())); M = list(map(float, pr.get("ori", " ".join(map(str, I3))).split()))
            ys = 1.0 if pr.get("scale", "").lower() != "yonly" else None  # None: depth follows the parent's Y scale
            for go in grid_offsets(pr.get("grid")):
                pts.append((pr.get("id") or ("group:" + pr["group"] if pr.get("group") else None), pr.get("gender", "?").upper(), pr.get("secs", ""), [a + b for a, b in zip(pos, go)],
                            app(M, [0, 1, 0]), 1.0, (pr.get("slide", "false").lower() == "true", pr.get("center", "false").lower() == "true")))
    return tuple(pts)

def norm(v): return sum(a*a for a in v) ** .5

@lru_cache(None)
def bbox(name, depth=0):
    """Min/max corner of the part's geometry, own coordinates."""
    p = find(LDI, name)
    if not p or depth > 30: return None
    lo, hi = [1e9]*3, [-1e9]*3
    def add(v):
        for i in range(3): lo[i] = min(lo[i], v[i]); hi[i] = max(hi[i], v[i])
    for l in open(p, encoding="utf-8", errors="ignore"):
        t = l.split()
        if not t: continue
        if t[0] in ("3", "4") and len(t) >= 2 + 3*int(t[0]):
            v = list(map(float, t[2:2 + 3*int(t[0])]))
            for i in range(0, len(v), 3): add(v[i:i+3])
        elif t[0] == "1" and len(t) >= 15:
            b = bbox(" ".join(t[14:]), depth + 1)
            if b:
                x, y, z, *M = map(float, t[2:14])
                for cx in (b[0][0], b[1][0]):
                    for cy in (b[0][1], b[1][1]):
                        for cz in (b[0][2], b[1][2]):
                            add([a + o for a, o in zip(app(M, [cx, cy, cz]), (x, y, z))])
    return (lo, hi) if lo[0] < 1e9 else None

def sections(secs):
    """LDCad profile -> [(shape, radius, length)]. R round, A axle cross, S square, L_/_L = lock lip at a pin end."""
    return [(s, float(r), float(l)) for s, r, l in re.findall(r"([A-Z_]+)\s+([\d.]+)\s+([\d.]+)", secs)]

def seg_class(s, r):
    if s == "A": return "axle"
    if s in ("L_", "_L", "L") or (s == "R" and 5.5 <= r <= 6.5): return "pin"
    if s == "R" and r < 5: return "bar"
    if s == "S": return "square"
    return "collar"  # wide ring (R 8) between pin halves, or anything else that doesn't go in a hole

# type, plain name, point prefix
FEMALE = {"axle": ("axle hole (cross)", "axlehole"), "pin": ("pin hole (round)", "hole"), "collar": ("pin hole (round)", "hole"),
          "bar": ("small hole (3.2 mm bar)", "barhole"), "square": ("square hole", "sqhole")}
MALE = {"axle": ("axle stop (cross)", "axle"), "pin": ("pin stop (round)", "pin"), "bar": ("bar (3.2 mm)", "bar"), "square": ("square bar", "sqbar")}

def points(g, secs, pos, ax, sy, slide, center):
    """Split one LDCad cylinder into named stops, one per hole-length (20 LDU).
    Female: one point (a hole), depth = its length. Male: walk the profile; every pin/axle run of n holes gives n stops."""
    sec = sections(secs)
    total = sum(l for *_, l in sec) * sy
    u = [c / (norm(ax) or 1) for c in ax]
    if g == "F":
        cls = next((seg_class(s, r) for s, r, _ in sec if seg_class(s, r) in ("axle",)), None) or \
              ("pin" if any(r >= 6 for _, r, _ in sec) else seg_class(*sec[0][:2]) if sec else "pin")
        mid = [p - c * total / 2 for p, c in zip(pos, u)] if not center else pos  # one-sided cylinders run along -axis
        return [(FEMALE[cls][0], FEMALE[cls][1], mid, u, total, max((r for _, r, _ in sec), default=0))]
    if not center: u = [-c for c in u]  # one-sided cylinders run along -axis
    start = [p - c * total / 2 for p, c in zip(pos, u)] if center else list(pos)
    out, runs, at = [], [], 0.0
    for s, r, l in sec:  # merge neighbouring sections of the same class into runs
        c = seg_class(s, r)
        if runs and runs[-1][0] == c: runs[-1][2] += l * sy
        else: runs.append([c, at, l * sy])
        at += l * sy
    for c, a0, length in runs:
        if c not in MALE: continue
        n = max(1, round(length / 20))
        for i in range(n):
            d = a0 + length * (i + .5) / n
            at_ = [round((p + cc * d) / 10) * 10 for p, cc in zip(start, u)]  # stops sit on the half-hole grid
            out.append((MALE[c][0], MALE[c][1], at_, u, length / n, 6 if c in ("pin", "axle") else 0))
    return out

def r1(x): return round(x + 0.0, 1)

# What each kind of part is for, from its catalog name. First match wins.
ROLES = [
    (r"Pin.*without Friction|Pin.*No Friction|Axle Pin without", "pin, frictionless", "frictionless",
     "Joins two parts and lets them turn freely. Use for hinges and moving joints."),
    (r"Axle Pin.*with Friction|Axle Pin 3L", "axle pin, friction", "friction",
     "Pin on one end, axle on the other. The pin end grips a round hole stiffly; the axle end locks into a cross hole or carries a gear."),
    (r"Pin Long.*Stop Bush", "long pin with stop bush, friction", "friction",
     "Pin end grips round holes stiffly; the bush end has a cross hole that takes an axle. Turns an axle end into a pin."),
    (r"Pin.*with Friction|Pin.*Friction Ridges|Pin 3/4|Pin Double", "pin, friction", "friction",
     "Joins two parts so they stay put. Friction ridges hold the joint stiff; parts can still be turned by hand."),
    (r"Axle.*with Stop", "axle with stop", "n/a",
     "Turns and carries gears. The stop end can't pass through a hole, so it holds the axle in place from one side."),
    (r"Axle.*Notched", "axle, notched", "n/a",
     "Short axle that locks two cross holes together. The notch lets it sit flush."),
    (r"^Technic Axle \d", "axle", "n/a",
     "Turns freely in round holes; locks to anything with a cross hole (gears, connectors), so they turn together."),
    (r"Bush 1/2|Half Bush", "half bush", "n/a",
     "Thin stop on an axle: keeps the axle and the parts on it from sliding, takes half a hole of space."),
    (r"Bush", "bush", "n/a",
     "Stop on an axle: keeps the axle and the parts on it from sliding, but lets the axle turn."),
    (r"Worm", "worm gear", "n/a",
     "Turns a gear one tooth per turn: very slow, very strong, and the gear can't turn it back, so it holds position by itself."),
    (r"Turntable", "turntable", "n/a",
     "Two halves that turn against each other on a big ring. Used to rotate a whole upper structure; its teeth let a gear drive it."),
    (r"Gear.*Crown", "crown gear", "n/a",
     "Teeth on the face: meshes with a normal gear at a right angle, or as a normal gear."),
    (r"Gear.*Double Bevel", "double bevel gear", "n/a",
     "Meshes at a right angle with another bevel gear, or side by side like a normal gear."),
    (r"Gear.*Bevel", "bevel gear", "n/a",
     "Meshes with another bevel gear at a right angle to turn the drive 90 degrees."),
    (r"Gear Rack", "gear rack", "n/a", "Straight row of teeth: a gear turning against it moves it in a straight line."),
    (r"Gear|Gearwheel", "gear", "n/a",
     "Passes turning to another gear. Speed and force change by the ratio of their teeth."),
    (r"Beam.*Thin|Liftarm.*Thin", "beam, thin (half thick)", "n/a",
     "Structural. Half the thickness of a normal beam, for tight spaces and spacers."),
    (r"Beam|Liftarm", "beam", "n/a",
     "Structural: the main building part. Round holes take pins (stiff joint) or axles (free turning); cross holes lock axles."),
    (r"Axle Connector|Axle and Pin Connector|Pin Connector|Connector", "connector", "n/a",
     "Joins axles and pins at an angle or end to end. Cross holes lock to axles; round holes take pins or let axles turn."),
    (r"Panel|Fairing", "panel", "n/a", "Cover for looks; carries little load."),
    (r"Link Tread|Tread", "tread link", "n/a", "Clips to other links into a track loop that runs on gears or sprockets."),
    (r"Link", "link", "n/a", "Rod with holes at the ends for linkages: transfers push and pull between two pivots."),
    (r"Shock Absorber", "shock absorber", "n/a", "Spring that lets a part move and pushes it back. Used for suspension."),
    (r"Steering|CV Joint|Towball|Ball", "steering / ball joint", "n/a", "Lets parts turn or swivel for steering and suspension."),
    (r"Hose", "hose", "n/a", "Flexible rod. Mostly for looks; can also brace or push lightly."),
    (r"Bucket|Claw|Grabber", "tool", "n/a", "Working end of a machine: digs, grabs or scoops."),
    (r"Brick|Slope", "technic brick", "n/a", "Classic brick with pin holes through it; stacks with studs and takes pins."),
    (r"Plate", "plate", "n/a", "Thin brick, usually for looks (e.g. lights)."),
]

rows = list(csv.DictReader(open(CAT, encoding="utf-8")))
conn_rows, found = [], 0
ORDER = ["pin hole (round)", "axle hole (cross)", "pin stop (round)", "axle stop (cross)", "small hole (3.2 mm bar)", "bar (3.2 mm)", "square hole", "square bar"]
PLURAL = {"pin hole (round)": "pin holes (round)", "axle hole (cross)": "axle holes (cross)", "pin stop (round)": "pin stops (round)",
          "axle stop (cross)": "axle stops (cross)", "small hole (3.2 mm bar)": "small holes (3.2 mm bar)", "bar (3.2 mm)": "bars (3.2 mm)",
          "square hole": "square holes", "square bar": "square bars"}
for r in rows:
    base = r["part_number"]
    tries = [base, re.sub(r"(pr|pat)\d+.*$", "", base), re.sub(r"[a-z]$", "", re.sub(r"(pr|pat)\d+.*$", "", base))]
    f = next((t + ".dat" for t in tries if find(LDI, t + ".dat")), base + ".dat")
    r["ldraw_file"] = f if find(LDI, f) else ""
    b = bbox(f)
    if b: found += 1
    # collect points; the same spot reported by two layers keeps the longest one
    best = {}
    for pid, g, secs, pos, ax, sy, (slide, center) in resolve(f):
        if (pid or "").startswith("group:"): continue  # LDCad extras (crane-arm clips on beam bodies)
        for typ, prefix, p, u, depth, rad in points(g, secs, pos, ax, sy, slide, center):
            key = (typ, tuple(round(c) for c in p), tuple(abs(round(c, 1)) for c in u))
            if key not in best or depth > best[key][4]:
                best[key] = (typ, prefix, p, u, depth, rad, slide)
    pts = list(best.values())
    # number points along the part's longest direction so names are stable: hole1..holeN, axle1..axleN
    main = max(range(3), key=lambda i: b[1][i] - b[0][i]) if b else 2
    pts.sort(key=lambda q: (q[1], round(q[2][main], 1), round(q[2][(main + 1) % 3], 1), round(q[2][(main + 2) % 3], 1)))
    counts, idx = {}, {}
    for typ, prefix, p, u, depth, rad, slide in pts:
        idx[prefix] = idx.get(prefix, 0) + 1
        counts[typ] = counts.get(typ, 0) + 1
        turns = {"pin hole (round)": "axles turn freely; friction pins hold stiff, frictionless pins turn freely",
                 "axle hole (cross)": "locks an axle: they turn together", "pin stop (round)": "turns in a round hole (stiff if friction)",
                 "axle stop (cross)": "turns freely in a round hole; locked in a cross hole"}.get(typ, "")
        conn_rows.append([r["part_number"], f"{prefix}{idx[prefix]}", typ, r1(p[0] / 20), r1(p[1] / 20), r1(p[2] / 20),
                          *[r1(c) for c in u], r1(depth / 20), r1(depth), r1(rad), "yes" if slide else "no", turns])
    if b:
        size = sorted((round((hi - lo) / 20, 2) for lo, hi in zip(*b)), reverse=True)
        r["size_holes_LxWxH"] = " x ".join(str(s) for s in size)
        r["thickness_holes"] = size[-1]
    else:
        r["size_holes_LxWxH"] = r["thickness_holes"] = ""
    r["pin_holes"], r["axle_holes"], r["pin_stops"], r["axle_stops"] = (counts.get(k, 0) for k in ORDER[:4])
    for k in ("pins", "axles", "connections"): r.pop(k, None)
    teeth = re.search(r"([\d/]+) Tooth", r["name"])
    r["gear_teeth"] = teeth.group(1) if teeth else ""
    role = next(((t, fr, fn) for pat, t, fr, fn in ROLES if re.search(pat, r["name"], re.I)), ("other", "n/a", ""))
    r["part_type"], r["friction"], r["function"] = role
    listed = [f"{counts[k]} {k if counts[k] == 1 else PLURAL[k]}" for k in ORDER if counts.get(k)]
    r["description"] = ("No 3D data in LDraw for this part number. " + role[2] if not b else
                        f"{r['size_holes_LxWxH']} holes in size, {r['thickness_holes']} thick. "
                        + (f"Gear with {r['gear_teeth']} teeth. " if teeth else "")
                        + (("Connections: " + ", ".join(listed) + ". ") if listed else "")
                        + role[2]).strip()

cols = [c for c in rows[0].keys() if c != "description"] + ["description"]
with open(CAT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, cols, lineterminator="\n"); w.writeheader(); w.writerows(rows)
with open("catalog/connections.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["part_number", "point", "type", "x_holes", "y_holes", "z_holes", "axis_x", "axis_y", "axis_z",
                "depth_holes", "depth_ldu", "radius_ldu", "can_slide", "how_it_turns"])
    w.writerows(conn_rows)
print(f"{found}/{len(rows)} parts have 3D data; {len(conn_rows)} named points")
