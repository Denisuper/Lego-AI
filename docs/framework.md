# Lego AI: Labeling Framework

The rules for turning one booklet step into one labeled training example. Live version: https://claude.ai/artifact/9agc7uxAr16TjJK2EYirj4

## How it works (6 steps per page)
1. **Split the booklet into steps.** Each page becomes a picture; find each step box, step number and parts box.
2. **Read the parts box.** Cut out each part picture and count. Match to a part number. The set's parts list is the answer key: every part must be on it, and counts must add up by the last page.
3. **Spot what's new.** Compare with the previous step's picture.
4. **Place the new parts.** Try each spot a part could fit; keep the one that matches the picture. When unclear, a person picks from the top 2-3 options, and each pick is saved.
5. **Record what touches what.** Which hole, pin or axle end joins which.
6. **Label what each part does.** Six verbs only. Gear ratio = driver teeth / driven teeth.

At the end, rebuild the whole model and compare with the last page and the parts list.

## What we save for every part
| Field | What it holds |
| --- | --- |
| Name | Permanent label, like gear-14 |
| Part number | Which LEGO part (e.g. 4019), checked against the parts list |
| Catalog name + match | Official name; confirmed or likely |
| Color | The part's color |
| Step | The step that added it |
| Position | Where it sits (words now, 3D numbers later) |
| Rotation | Which way it faces, and whether it can spin |
| Touches | Parts it connects to, and through which hole or end |
| Does what | Records like "gear-D drives gear-B" |
| Confidence | low / medium / high, plus review flag and note |
| Where it is later | Position after every later step |

## Following each part
Every part keeps its name to the last page. Each new step updates: where it is (mini builds move as a group), what it touches (neighbor list grows), what it does (an axle "carries" once a gear goes on it; a gear "drives" once another meshes). Rotation arrows mark spinning parts. Hidden parts keep their last known position.

## One training example
Input: step picture + parts box + model so far.
Answer, always in this order:
1. new_parts (name, part number, color, position, rotation)
2. what_each_new_part_touches
3. who_does_what_to_which (six verbs)
4. where_everything_is_after ("no change" if nothing moved)
Plus confidence, needs_review, review_note.

## The six verbs
| Verb | Means | Example |
| --- | --- | --- |
| holds | keeps another part in place | connector-H holds pin-L |
| carries | a shaft with something fixed to it | axle-red-G carries connector-H |
| spins on | turns around another part | turntable-O spins on the frame |
| drives | turns another part by contact | gear-D drives gear-B |
| locks in place | stops a part sliding or turning | pin-L and pin-M lock beam7-N in place |
| supports | carries weight without moving | beam7-N supports the front of the frame |

## Worked example: set 8047, step 7
beam7-N (32524) lies flat across the front, long side left to right. Its end holes go over pin-L and pin-M. pin-L and pin-M lock beam7-N in place; beam7-N supports the front of the frame. Nothing else moved.

## Tools
| Piece | Option |
| --- | --- |
| Page converter | PyMuPDF |
| Box finder | Small image-detection model trained on a few hundred hand-marked pages |
| Part matcher | Image-matching model (e.g. DINOv2) + catalog part pictures, narrowed by the parts list |
| Parts lists | Rebrickable / Brickset |
| Part library | LDraw |
| 3D drawer | LDView or Blender |
| Review screen | Simple web page |

## Checks a program runs on every answer
- Every part number is on the set's parts list.
- Counts never exceed the set's total, and add up by the last page.
- Only the six verbs appear.
- Every name mentioned was introduced in this or an earlier step.
- Every part in the parts box appears in the answer, with the right count.
