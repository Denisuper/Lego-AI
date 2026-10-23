# Training for mechanisms, not just assembly

## What the step-by-step data taught before (the problem)
Next-line prediction on the build language taught **assembly**: which part tends to come next, which holes fit, how names are used.
It barely taught **mechanisms**:
- The only mechanism signal was an occasional `DOES … DRIVES` or `RATIO` line.
- The "why" lived only in JSON text that the small model never sees.
- A mechanism is spread over many steps (8047's front worm drive spans seat step 7 to main step 34), and nothing tied those steps together.
- With one set, the model could memorise 8047 without learning that "worm on a gear = slow, strong, holds its position".

## The mechanism layer (what's added)
| Piece | File | What it holds |
| --- | --- | --- |
| Mechanism library | `catalog/mechanisms.json` | Every mechanism type (gear pair, idler, bevel 90°, crown, worm drive, slewing ring, shaft with stops, knob input, hinge, 4-bar linkage, push rod, crank-lever, track loop, rigid frame, decoration): what it does, motion in/out, ratio formula, the roles its parts play, the rules that make it work, how it fails, how to spot it. Shared by every set. |
| A set's mechanisms | `sets/<set>/mechanisms.json` | Each mechanism in the model as a **chain of parts in the order motion flows**, each with its role and how it links to the previous part; `confirmed` or `hypothesis`. |
| Motion and state tool | `tools/mechanisms.py` | After every step: which mechanisms the step advances, how complete each is, **what turns when the input turns once** (worked out from LOCKED joins and MESH/RATIO), and for each new part the earlier parts it builds on, followed back two links. Also flags **jams**: an input that would spin a frame part. |

`tools/build_set.py` puts all of this into every training example (`answer.mechanism`) and into the build language:

```
STEP 26
ADD worm-1 4716 lightgray
CONNECT worm-1.axlehole1 -> axle8s-1.axle4 LOCKED
MESH worm-1.teeth crown-1.teeth
RATIO worm-1 crown-1 1/24
MECH drive_front worm_drive worm-1 worm         # this part's role in which mechanism
STATE drive_front 7/8                           # mechanism is 7/8 built
...
STEP 34
MECH drive_front worm_drive knob-2 knob_input
STATE drive_front 8/8 COMPLETE
MOTION knob-2 axle8s-1=1 worm-1=1 crown-1=-1/24 axle7-s=-1/24 gear-5=-1/24 gear-6=1/24 axle7-B=1/24
```
So the model reads, in the same stream it learns to build from, what each part is for in a mechanism, how far along the mechanism is, and what the finished mechanism does when you turn it.

## Training tasks (all generated from the same data)
| # | Task | Input | Target | Teaches |
| --- | --- | --- | --- | --- |
| 1 | Next line | build so far | next line (including MECH / STATE / MOTION) | building, with mechanism roles inline |
| 2 | Predict motion | build so far + `TURN knob-2` | the MOTION line | how motion flows through locks, gears, ratios, direction |
| 3 | Finish a mechanism | build so far + `STATE drive_front 7/8` | the missing part and its joins | what a mechanism still needs |
| 4 | Find the fault | a build with one join changed (LOCKED↔TURNS, cross hole↔round hole, a gear moved out of mesh) | which line is wrong and why (JAM / no drive / doesn't fit) | why each join is the way it is |
| 5 | Explain a part | build + part name | its MECH role + the chain it builds on | tying every part back to earlier steps |
| 6 | Design (later) | `REQUEST` + mechanism type | a build whose MOTION matches the request | using mechanisms on purpose |

Tasks 2 and 4 need no labelling: `tools/mechanisms.py` computes the answer, and the checkers make the faulty copies for task 4 by changing one join at a time.
Task 4 is grounded in real mistakes. The checkers caught these in 8047's own labels: a worm shaft through a cross hole (would jam), a gear shaft locked by a block, a pin in a cross hole, two parts on one pin.

## Rules for labelling a set's mechanisms
1. List every mechanism in the finished model first (read the last pages, try the functions in your head).
2. Write each as a chain in the order motion flows: input → shaft → gear → … → output. Every part gets a role from the library's `roles`.
3. Mark each link `confirmed` only if a picture shows it; otherwise `hypothesis`, and say what to check.
4. Run `python tools/mechanisms.py sets/<set>`: every mechanism with an input must turn something, and no JAM lines. A JAM is either a label error or a misunderstanding of the mechanism; fix it, don't ignore it.

## Model
We fine-tune Qwen (open source, Apache 2.0) instead of training from scratch: it already reads English, so the full-sentence THINK lines are understood, not just copied. training/export.py builds tasks 1 and 2 today; 3-5 are next.

## Limits (be honest)
- One set is far too little to learn general mechanisms. The library + tasks 2-4 help, but more sets are the real fix.
- 8047 still has open mechanism questions (where axle7-B's turning goes; the back shaft that can't turn as labelled). They are marked `hypothesis` / JAM, and the model must not be trained on them as facts: filter `status: hypothesis` out of task 2 targets until confirmed.
