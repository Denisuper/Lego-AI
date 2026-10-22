"""Reads the LDraw 3D part files + LDCad snap data and writes, for every catalog part:
  catalog/connections.csv   one row per hole / pin / axle: type, position, direction, depth
  catalog/technic_parts.csv adds size, thickness, counts and a plain-English description
Usage: python tools/build_connections.py <ldraw dir> <LDCadShadowLibrary dir>
  ldraw:  https://library.ldraw.org/library/updates/complete.zip
  shadow: https://github.com/RolandMelkert/LDCadShadowLibrary (download the zip)
Units: LDraw units (LDU). 20 LDU = 1 Technic hole spacing (8 mm). Positions are also given in holes (LDU/20)."""
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
                            app(M, [0, 1, 0]), 1.0 if ys else 1.0, pr.get("slide", "false").lower() == "true"))
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

def kind(g, secs, group=None):
    """Plain name for a connection from LDCad gender + section profile.
    Profile = list of (shape, radius, length): R round, A axle cross, S square, L/_L/L_ = friction ridges or end lock."""
    shapes = [(s, float(r), float(l)) for s, r, l in re.findall(r"([A-Z_]+)\s+([\d.]+)\s+([\d.]+)", secs)]
    letters = {s for s, _, _ in shapes}
    pin_len = sum(l for s, r, l in shapes if s == "R" and 5.5 <= r <= 6.5)
    length = sum(l for _, _, l in shapes)
    radius = max((r for _, r, _ in shapes), default=0)
    if group: return "clip surface", length, radius   # LDCad extras like crane-arm clips on beam bodies
    if g == "F":
        if "A" in letters: k = "axle hole (cross)"
        elif "R" in letters and radius >= 6: k = "pin hole (round)"
        elif "R" in letters: k = "small hole (3.2 mm bar)"
        else: k = "hole"
    elif g == "M":
        if "A" in letters and pin_len: k = "axle + pin combo"
        elif "A" in letters: k = "axle (cross)"
        elif pin_len: k = "pin (round)"
        elif "R" in letters and radius < 5: k = "bar (3.2 mm)"
        elif "S" in letters: k = "square bar"
        else: k = "peg"
    else: k = "other"
    return k, length, radius

def r1(x): return round(x + 0.0, 1)

rows = list(csv.DictReader(open(CAT, encoding="utf-8")))
conn_rows, found = [], 0
for r in rows:
    base = r["part_number"]
    tries = [base, re.sub(r"(pr|pat)\d+.*$", "", base), re.sub(r"[a-z]$", "", re.sub(r"(pr|pat)\d+.*$", "", base))]
    f = next((t + ".dat" for t in tries if find(LDI, t + ".dat")), base + ".dat")
    r["ldraw_file"] = f if find(LDI, f) else ""
    pts, b = resolve(f), bbox(f)
    if b: found += 1
    counts = {}
    seen = set()
    for pid, g, secs, pos, ax, sy, sl in pts:
        k, length, radius = kind(g, secs, (pid or "").startswith("group:"))
        a = [r1(c / (norm(ax) or 1)) for c in ax]
        key = (k, tuple(r1(c) for c in pos), tuple(abs(c) for c in a))
        if key in seen: continue  # same hole reported by two layers
        seen.add(key)
        counts[k] = counts.get(k, 0) + 1
        conn_rows.append([r["part_number"], k, g, r1(pos[0]), r1(pos[1]), r1(pos[2]),
                          r1(pos[0] / 20), r1(pos[1] / 20), r1(pos[2] / 20), *a, r1(length * sy), r1(radius), "yes" if sl else "no", secs])
    if b:
        size = sorted((round((hi - lo) / 20, 2) for lo, hi in zip(*b)), reverse=True)
        r["size_holes_LxWxH"] = " x ".join(str(s) for s in size)
        r["thickness_holes"] = size[-1]
    else:
        r["size_holes_LxWxH"] = r["thickness_holes"] = ""
    order = ["pin hole (round)", "axle hole (cross)", "pin (round)", "axle (cross)", "axle + pin combo", "small hole (3.2 mm bar)", "bar (3.2 mm)", "square bar", "hole", "peg", "clip surface", "other"]
    r["pin_holes"], r["axle_holes"], r["pins"], r["axles"] = (counts.get(k, 0) for k in order[:4])
    r["connections"] = sum(counts.values())
    PLURAL = {"pin hole (round)": "pin holes (round)", "axle hole (cross)": "axle holes (cross)", "pin (round)": "pins (round)",
              "axle (cross)": "axles (cross)", "axle + pin combo": "axle + pin combos", "small hole (3.2 mm bar)": "small holes (3.2 mm bar)",
              "bar (3.2 mm)": "bars (3.2 mm)", "square bar": "square bars", "hole": "holes", "peg": "pegs", "other": "other"}
    plural = lambda n, k: f"{n} {k if n == 1 else PLURAL[k]}"
    parts = [plural(counts[k], k) for k in order if counts.get(k) and k != "clip surface"]
    teeth = re.search(r"([\d/]+) Tooth", r["name"])
    r["gear_teeth"] = teeth.group(1) if teeth else ""
    thick = r["thickness_holes"]
    r["description"] = ("No 3D data in LDraw for this part number." if not b else
                        f"{r['size_holes_LxWxH']} holes in size, {thick} thick. "
                        + (f"Gear with {r['gear_teeth']} teeth. " if teeth else "")
                        + (("Connections: " + ", ".join(parts) + ".") if parts else "No connection data."))

cols = list(rows[0].keys())
with open(CAT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, cols, lineterminator="\n"); w.writeheader(); w.writerows(rows)
with open("catalog/connections.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["part_number", "type", "gender", "x_ldu", "y_ldu", "z_ldu", "x_holes", "y_holes", "z_holes",
                "axis_x", "axis_y", "axis_z", "depth_ldu", "radius_ldu", "can_slide", "ldcad_profile"])
    w.writerows(conn_rows)
print(f"{found}/{len(rows)} parts have 3D data; {len(conn_rows)} connection points")
