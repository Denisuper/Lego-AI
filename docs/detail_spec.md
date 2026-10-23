# Detail spec: everything we can record

The goal: a build described so exactly that a program could rebuild it, check it, and explain it, with no picture needed.
This file lists every kind of detail, from one hole up to the whole machine. Each row says where the detail comes from and whether we have it yet.

**Status:** ✅ have it · 🟡 partly · ⬜ planned

**Where it comes from:**
- **catalog**: LDraw 3D parts + LDCad connection data + Rebrickable, filled in by a tool.
- **picture**: read from the booklet.
- **derived**: worked out by a tool from other data.
- **human**: needs a person to judge.

---

## 0. Conventions (apply everywhere)

| Rule | Detail |
| --- | --- |
| Unit | 1 hole = 8 mm = 20 LDraw units (LDU). Plate height = 8 LDU, brick = 24 LDU. All sizes and positions in holes unless marked LDU. |
| Axes | LDraw axes: X right, Y **down**, Z toward the viewer. Model "front" = the side the booklet's first picture faces. |
| Left / right | Seen from the driver's seat, facing forward. |
| Hole numbering | `hole1..N` along the part's longest direction, starting from the end with the lower coordinate in the part's own LDraw file. Bent beams: the same rule applies to the straightened part. Never renumber. |
| Pin / axle stops | One stop per hole-length: `pin1..N`, `axle1..N`, counted the same way. |
| Names | Permanent, `type-ID` (pin-L, gear-3, beam9-X). Side builds use their own suffix (lbeam-s1, worm-2). |
| Rotation | Degrees, right-hand rule around the joint's axis; 0 = as drawn in the booklet. |
| Unknown | `?` in notation, `null` in JSON, and always a review note saying why. Never guess silently. |

---

## 1. Part detail (catalog/technic_parts.csv)

### Identity
| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Part number, name, category | 32524, Technic Beam 1 x 7 Thick, Technic Beams | catalog (Rebrickable) | ✅ |
| Colors it was made in | Black; Red; Yellow… | catalog | ✅ |
| LDraw file | 32524.dat | catalog | ✅ |
| Other numbering systems | BrickLink ID, LEGO element ID per color | catalog (Rebrickable element / external IDs) | ⬜ |
| Old vs new version, mold changes | 4019 old style round holes vs 94925 | catalog + human | ⬜ |
| Years made | 2009-2011 | catalog (Rebrickable sets) | ⬜ |
| Mirror twin | fairing 87080 (side A) ↔ 87086 (side B) | catalog name pattern + geometry | ⬜ |
| Image | render or photo URL | Rebrickable / LDraw render | ⬜ |

### Size and shape
| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Size L x W x H in holes | 6.9 x 1.0 x 0.9 | catalog geometry | ✅ |
| Thickness | 0.5 (thin) or 1 (thick) | catalog geometry | ✅ |
| Holes on a half-hole offset | thin 3x3 L-beams, beams with centre offset | derived from point positions | ⬜ |
| Shape class | straight, L, bent (angle), frame, round, panel | catalog name + geometry | 🟡 (in part_type) |
| Bend angles | 32009 bent 45° twice | geometry between hole axes | ⬜ |
| Symmetry | can be flipped end-for-end without changing anything? | derived from points | ⬜ |
| Weight (g), volume, centre of mass | 7-beam ≈ 1.8 g | catalog (BrickLink weights) / mesh volume | ⬜ |

### Mechanics
| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Part type | pin, frictionless pin, axle with stop, half bush, worm gear, thin beam | catalog name rules | ✅ |
| Friction | friction / frictionless | catalog name rules | ✅ |
| What it's for (plain English) | worm: slow, strong, holds position by itself | rules + human | ✅ (per type) |
| Gear teeth | 16; turntable 24/56 | catalog name | ✅ |
| Gear kind | spur / bevel / double bevel / crown / worm / rack / turntable | catalog name rules | ✅ |
| Gear pitch radius | 16T = 1 hole; 8T = 0.5; 24T = 1.5; 40T = 2.5 | table (teeth / 16) | ⬜ |
| Which gear pairs mesh at whole-hole spacing | 8+24 at 2 holes, 16+16 at 2, 12+20 bevel at 90° | derived from pitch radii | ⬜ |
| Clutch / slip gear, slip torque | 24T clutch gear slips at ~2.5-5 Ncm | catalog name + reference | ⬜ |
| Flexible or rigid | hose 75c12 flexes, axles slightly | catalog + human | ⬜ |
| Load limits / weak points | long axles twist; worm on a thin axle bends | human (design notes) | ⬜ |
| Common partners | 3713 bush goes with axles; 6536 links axle to pin | derived from labeled sets | ⬜ |
| "Never do" rules | don't drive through a frictionless pin; axle in a round hole won't carry torque | human → checker rules | ⬜ |

---

## 2. Connection point detail (catalog/connections.csv)

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Point name | hole3, axlehole1, pin2, axle3 | derived (numbering rule) | ✅ |
| Type | pin hole (round), axle hole (cross), pin stop, axle stop, 3.2 mm bar / hole | catalog | ✅ |
| Position (x, y, z in holes) | 0, 0, -1 | catalog | ✅ |
| Axis direction | 0, -1, 0 | catalog | ✅ |
| Depth | beam hole 1, thin beam 0.5, worm 2 | catalog | ✅ |
| Radius | 6 LDU pin, 8 LDU collar | catalog | ✅ |
| Things can slide through it | yes for beam holes | catalog | ✅ |
| How it turns | cross hole locks; round hole lets axles turn | rules | ✅ |
| Through or blind (open both sides?) | beam hole: through; axle-pin's axle hole: blind | catalog caps= field | ⬜ |
| Which faces you can enter from | both / front only | catalog caps= field | ⬜ |
| Collar / stop position on pins | 2780: collar in the middle, 1 hole each side | catalog profile | 🟡 (in profile, not named) |
| Friction strength of this point | friction pin ridge = stiff; smooth hole | catalog + rules | 🟡 |
| Cross orientation (axle holes fit every 90°) | matters for cranks and lever angles | rule | ⬜ |
| Blocked by the part's own shape | panel holes too close to the edge for a bush | geometry | ⬜ |
| Studs and anti-studs | round 1x1 plate, axle with stud | catalog (stud snap data) | 🟡 (read as pin/hole) |
| Ball joints, clips, bar holders | steering parts, hose clips | catalog (LDCad SNAP_CLP etc.) | ⬜ |
| Gear teeth as a point | `teeth`: pitch circle, plane, number of teeth | derived | 🟡 (name only) |

---

## 3. Join detail (one CONNECT line / one entry in `joins`)

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Which point into which point | `pin-L.pin2 -> beam7-N.hole1` | picture + catalog | 🟡 112/272 exact in 8047 |
| Fit | LOCKED / TURNS / STIFF | derived from point types | ✅ |
| Depth | 1 hole; 0.5 in a half bush | derived (shorter point) | ✅ |
| Partial depth | pushed halfway, finished in a later step (8047 step 18) | picture | ⬜ `DEPTH` exists, not used yet |
| Direction it goes in | from the front face / from below | picture (arrow) | ⬜ `FROM` keyword |
| Angle around the joint | crank at 90°, lever pointing up | picture | 🟡 `ANGLE` exists, rarely used |
| What it stops | locks slide along X; leaves rotation about X free | derived (fit + axis) | ⬜ |
| Push hard / needs a tool | friction pins in thick stacks | human | ⬜ |
| Temporary or final | pins left loose until a later part arrives | picture | ⬜ |
| Arrow evidence | red arrow, dashed arrow, no arrow (read from shape) | picture | 🟡 (in review notes) |
| Confidence per join | high / medium / low, and why | labeler | ⬜ (only per step now) |

---

## 4. Step detail (one annotation.json + notation.tbl)

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Page, step number, side build | page 34, arm step 5 | booklet | ✅ |
| Picture crop | steps/arm-05/picture.png | booklet | ✅ |
| Parts box: parts, counts, colors | 1x 4716, 1x 87083… | picture | ✅ |
| Every new part: name, number, color, match certainty | worm-2, 4716, light bluish gray, confirmed | picture + parts list | ✅ |
| Position and rotation in words | "lengthwise through the arm" | picture | ✅ |
| Position and rotation as numbers (x, y, z + rotation matrix) | needed for LDraw output | derived from exact joins | ⬜ |
| What touches what (words) | | picture | ✅ |
| Exact joins with depth and fit | | picture + catalog | 🟡 |
| Who does what (six verbs) | worm-2 DRIVES crown-1 | picture + reasoning | ✅ |
| Gear ratios | RATIO worm-1 crown-1 1/24 | derived | 🟡 (where written) |
| Where everything is after | | labeler | ✅ |
| Why: problem, why these parts, sets up later, pattern | | labeler | ✅ |
| Sub-steps inside one step (side boxes 1-2-3) | step 54: hub → beam → light | picture | 🟡 (words only) |
| View changes | turn-over symbol, "turn model round" | picture | 🟡 (notes) |
| Model orientation at this step | upside down (steps 1-15) | picture | 🟡 (notes) |
| 1:1 length callouts | "axle 9" drawn to scale | picture | ⬜ (would confirm axle lengths) |
| Order of parts within the step | gear onto axle first, then axle through beam | picture | 🟡 (line order in notation) |
| Hidden parts | parts the picture covers | picture | 🟡 (review notes) |
| Common mistakes | wrong hole by one; axle one too short | human / from the 1:1 callouts | ⬜ |
| What to check after the step | "gear-5 turns freely" | human / derived | ⬜ |
| Difficulty | number of parts, hidden joins, push force | derived | ⬜ |
| Field-level confidence and source | each field: picture / catalog / inferred / human | labeler | ⬜ |

---

## 5. Whole-model detail (after every step and at the end)

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Part list so far vs official list | 252/252 used | derived | ✅ |
| Full 3D position of every part | LDraw .ldr with STEP markers | derived from exact joins | ⬜ (converter, task 4) |
| Connection graph | parts as nodes, joins as edges | derived from notation | ⬜ |
| Sub-assemblies | seat, body, arm, boom, tracks | notation GROUP | ✅ |
| How each part can move | fixed / turns about axis / slides / swings | derived from fits | ⬜ |
| Rigid groups | which parts move as one body | derived (LOCKED + STIFF joins) | ⬜ |
| Collisions and clearance | gear teeth touch the frame? | 3D check | ⬜ |
| Size, weight, centre of gravity, tipping | | derived | ⬜ |
| Stiffness weak spots | long unsupported beams, single-pin joints | derived + human | ⬜ |

---

## 6. Mechanism detail (what the machine does)

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Inputs | knob-1, knob-2 at the back | picture + reasoning | 🟡 |
| Outputs | upper body turns; arm raises; bucket tips | picture + reasoning | 🟡 |
| Drive path, part by part | knob-2 → axle8s-1 → worm-1 → crown-1 → axle7-s → gear-5 → gear-6 → axle7-B | mechanisms.json + tools/mechanisms.py | ✅ front drive; 🟡 output and back shaft open |
| Total ratio and turns per output | 24 knob turns = 1 turn of crown-1 | tools/mechanisms.py (MOTION lines) | ✅ |
| Self-locking | worm drives hold position | mechanism library (worm_drive) | ✅ |
| Jam check: a drive that would spin the frame | back shaft in 8047 | tools/mechanisms.py | ✅ |
| Torque / speed trade-off in words | "slow and strong" | derived | ⬜ |
| Linkages: pivot points, link lengths, range of motion | push rod axle9-43 tips the stick between angles | derived from geometry | ⬜ |
| Limits / end stops | how far the arm can rise | 3D + human | ⬜ |
| Real-world meaning | "this is the swing drive of a real excavator" | human | 🟡 (some why fields) |

---

## 7. Design reasoning detail

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Problem solved, why these parts, sets up later, pattern | per step | labeler | ✅ |
| Role of every part in the finished machine | pin-L: holds beam7-N → closes the frame → carries the turntable | systems.json (human) | ✅ 8047 |
| System map: what each system is on the real machine, purpose, depends on / feeds | swing ring feeds upper frame | systems.json (human) | ✅ 8047 |
| Every later step that uses a part (forward links) | rod-A → steps 2, 5, 12 | derived from notation | ✅ |
| Full chain from a part to the machine's output (part → system → function) | worm-1 → crown-1 → … → boom rises | derived once drive paths are confirmed | 🟡 open questions in 8047 |
| Alternatives and why not | "a 24T gear would fit but the worm self-locks" | human | ⬜ |
| Constraint that forced the choice | space, part count, look, strength | human | ⬜ |
| Pattern library | named tricks with every place they're used | derived from PATTERN lines | ⬜ (catalog/patterns.csv) |
| Look vs function | fairings and hoses are looks only | labeler | 🟡 |

---

## 8. Provenance and quality

| Detail | Example | Source | Status |
| --- | --- | --- | --- |
| Who/what produced each field | picture / catalog / derived / human | pipeline | ⬜ |
| Review status per step | needs_review + note | labeler | ✅ |
| Reviewer and date | | human | ⬜ |
| Tool versions | LDraw library date, LDCad commit, Rebrickable date | tools | 🟡 (dates in CLAUDE.md) |
| Open items count | 160 joins with `?` in 8047 | check_notation.py | ✅ |

---

## 9. Training extras

| Detail | Example | Status |
| --- | --- | --- |
| REQUEST card per set (what the model should do) | `REQUEST excavator TURN knob BOOM knob MAXPARTS 260` | ⬜ |
| Mirrored and renamed copies (augmentation) | swap left/right, new names | ⬜ |
| Wrong examples the checker rejects (negatives) | pin into a cross hole | ⬜ |
| Train / test split by set, never by step | | ⬜ |

---

## What to add first (most value for the least work)
1. **Gear pitch radius + meshing table** (catalog, derived). Lets the checker confirm every MESH sits at a real distance.
2. **Through/blind and entry faces** (catalog caps= field). Small change to build_connections.py.
3. **Fill the 160 open joins in 8047** by counting holes in the pictures.
4. **Per-part 3D position** from exact joins → LDraw .ldr. Unlocks collisions, motion, renders and LPub3D booklets.
5. **Drive paths and total ratios** per input knob, derived from DOES/RATIO lines.
6. **Field-level source + confidence** in annotation.json.
