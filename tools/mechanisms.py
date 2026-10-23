"""Mechanism layer for a set, step by step. Used by build_set.py.
For every step it works out, from the notation so far + sets/<set>/mechanisms.json:
  advances   which mechanisms this step adds to, and each new part's role in them
  state      how complete each mechanism is (parts present / total, what's still missing)
  motion     what turns when the mechanism's input turns once (ratios from LOCKED joins and MESH/RATIO lines)
  builds_on  for each new part, the earlier parts it joins and what those do, followed back two links
Run alone to print the motion of every mechanism at the end: python tools/mechanisms.py sets/8047"""
import json, re, sys
from fractions import Fraction


class Tracker:
    def __init__(self, set_dir):
        mj = json.load(open(set_dir + "mechanisms.json", encoding="utf-8"))
        self.mechs = mj["mechanisms"]
        self.role = {}  # part -> [(mech, chain entry)]
        for m in self.mechs:
            for c in m["chain"]:
                self.role.setdefault(c["part"], []).append((m, c))
        self.added_in = {}   # part -> step id
        self.locked = {}     # part -> set of parts locked to it (turn together)
        self.mesh = []       # (a, b, Fraction ratio of b per a)
        self.links = {}      # part -> [(other part, line)] all joins seen

    def _feed(self, step_id, notation):
        new, step_joins = [], []
        ratios = {}
        for line in notation.split("\n"):
            t = line.split("#")[0].split()
            if not t: continue
            if t[0] == "ADD":
                self.added_in[t[1]] = step_id; new.append(t[1])
            elif t[0] == "CONNECT":
                a, b = t[1].split(".")[0], t[3].split(".")[0]
                self.links.setdefault(a, []).append((b, " ".join(t)))
                self.links.setdefault(b, []).append((a, " ".join(t)))
                step_joins.append((a, b, " ".join(t)))
                if "LOCKED" in t:
                    self.locked.setdefault(a, set()).add(b); self.locked.setdefault(b, set()).add(a)
            elif t[0] == "RATIO":
                ratios[(t[1], t[2])] = Fraction(t[3])
            elif t[0] == "MESH":
                a, b = t[1].split(".")[0], t[2].split(".")[0]
                if a.startswith("tread") or b.startswith("tread"): continue
                self.links.setdefault(a, []).append((b, " ".join(t))); self.links.setdefault(b, []).append((a, " ".join(t)))
                step_joins.append((a, b, " ".join(t)))
                self.mesh.append([a, b, None])
        for m in self.mesh:
            if m[2] is None and (m[0], m[1]) in ratios: m[2] = ratios[(m[0], m[1])]
        return new, step_joins

    def motion(self, start):
        """Turns of each part per one turn of `start`. Negative = opposite direction."""
        turns, todo = {start: Fraction(1)}, [start]
        while todo:
            p = todo.pop()
            for q in self.locked.get(p, ()):
                if q not in turns: turns[q] = turns[p]; todo.append(q)
            for a, b, r in self.mesh:
                r = r or Fraction(1)
                if a == p and b not in turns: turns[b] = -turns[p] * r; todo.append(b)
                if b == p and a not in turns: turns[a] = -turns[p] / r; todo.append(a)
        return turns

    def step(self, step_id, notation):
        new, joins = self._feed(step_id, notation)
        advances, touched = [], []
        for p in new:
            for m, c in self.role.get(p, []):
                advances.append({"mechanism": m["id"], "name": m["name"], "type": m["type"], "part": p, "role": c["role"],
                                 "link": c.get("link"), "status": c.get("status", "confirmed")})
                if m not in touched: touched.append(m)
        state = []
        for m in touched:
            have = [c["part"] for c in m["chain"] if c["part"] in self.added_in]
            missing = [c["part"] for c in m["chain"] if c["part"] not in self.added_in]
            state.append({"mechanism": m["id"], "parts_present": len(have), "parts_total": len(m["chain"]),
                          "complete": not missing, "still_missing": missing, "does": m["does"]})
        motion = []
        for m in touched:
            inp = m.get("input")
            if inp in self.added_in:
                t = self.motion(inp)
                chain_parts = [c["part"] for c in m["chain"]]
                moving = {p: t[p] for p in chain_parts if p in t and p != inp}
                if moving:
                    motion.append({"mechanism": m["id"], "input": inp,
                                   "per_input_turn": {p: str(v) for p, v in moving.items()},
                                   "says": f"Turn {inp} once: " + ", ".join(
                                       f"{p} turns {abs(v)} {'turn' if abs(v) == 1 else 'turns'}{' the other way' if v < 0 else ''}"
                                       for p, v in moving.items())})
        builds_on = []
        for p in new:
            back = []
            for a, b, line in joins:
                other = b if a == p else a if b == p else None
                if not other or other not in self.added_in or self.added_in[other] == step_id: continue
                roles = [f"{c['role']} in the {m['name'].lower()}" for m, c in self.role.get(other, [])]
                # one more link back: what the earlier part itself hangs on
                prev = [(o, l) for o, l in self.links.get(other, []) if o != p and self.added_in.get(o) and self.added_in[o] != step_id][:2]
                back.append({"joins": other, "added_in": self.added_in[other], "line": line,
                             "that_part_is": roles or None,
                             "which_rests_on": [{"part": o, "added_in": self.added_in[o], "line": l} for o, l in prev]})
            if back:
                builds_on.append({"part": p, "builds_on": back})
        return {"advances": advances, "state": state, "motion": motion, "builds_on": builds_on}

    def jams(self, part_numbers, part_types, pin_holes=None):
        """Drive inputs that would spin a structural part (beam / connector): the drive is locked to the frame."""
        out = []
        for m in self.mechs:
            inp = m.get("input")
            if inp not in self.added_in: continue
            for p in self.motion(inp):
                num = part_numbers.get(p)
                if p != inp and part_types.get(num, "") in ("beam", "beam, thin (half thick)", "connector") and (pin_holes or {}).get(num, 1) > 0:
                    out.append(f"{m['name']}: turning {inp} would also spin {p} ({part_types[part_numbers[p]]}); the drive is locked to the structure")
        return out

    def lines(self, info):
        """Mechanism lines for the build language."""
        out = []
        for a in info["advances"]:
            role = "_".join(re.sub(r"[^a-z0-9 ]+", " ", a["role"].split(":")[0].split(";")[0].lower()).split()[:3])
            out.append(f"MECH {a['mechanism']} {a['type']} {a['part']} {role}" + (" ?" if a["status"] == "hypothesis" else ""))
        for s in info["state"]:
            out.append(f"STATE {s['mechanism']} {s['parts_present']}/{s['parts_total']}" + (" COMPLETE" if s["complete"] else ""))
        for mo in info["motion"]:
            out.append(f"MOTION {mo['input']} " + " ".join(f"{p}={v}" for p, v in mo["per_input_turn"].items()))
        return out


if __name__ == "__main__":
    import csv
    d = sys.argv[1].rstrip("/") + "/"
    tr = Tracker(d)
    for r in csv.DictReader(open(d + "booklet_map.csv")):
        tr.step(r["folder"], open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read())
    nums = {}
    for r in csv.DictReader(open(f"{d}parts_list.csv")): pass
    for line in open(d + "training.tbl", encoding="utf-8"):
        t = line.split()
        if t[:1] == ["ADD"]: nums[t[1]] = t[2]
    cat = list(csv.DictReader(open("catalog/technic_parts.csv", encoding="utf-8")))
    types = {r["part_number"]: r["part_type"] for r in cat}
    holes = {r["part_number"]: int(r["pin_holes"] or 0) for r in cat}
    for j in tr.jams(nums, types, holes): print("JAM:", j)
    for m in tr.mechs:
        if m.get("input") in tr.added_in:
            t = tr.motion(m["input"])
            print(m["name"], {p: str(v) for p, v in t.items() if p != m["input"]})
