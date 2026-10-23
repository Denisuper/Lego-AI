# Lego AI - project guide

## What this project is
An AI made only for LEGO Technic. Real instruction booklets are turned into step-by-step build text. A Qwen model (Apache 2.0, start with Qwen2.5-1.5B/3B-Instruct) is fine-tuned on it with LoRA, then improved with GRPO using our checkers as the score.

Owner: Dennis. Plain language, no jargon, straight to the point. Save tokens.

## How to add a set (the only workflow)
1. Make `sets/<set>/` with the original `booklet.pdf` (commit it unedited; add `!sets/<set>/booklet.pdf` to .gitignore) and `parts_list.csv` (Rebrickable).
2. Read the booklet pages directly. Do NOT crop pictures, do NOT write annotation.json, systems.json, mechanisms.json or booklet_map.csv.
3. Write ONE file: `sets/<set>/steps.md`, one block per step (see 42175 for an example):
```
## Step 18 (page 18)
ADD pump-beam-1 32278 darkgray
CONNECT pump-pin-1.pin1 -> pump-beam-1.hole4 STIFF
WHY one plain sentence: what this step builds and what it is for.
```
4. Check: every part in the parts list used exactly once by the end; every point exists in `catalog/connections.csv`.
5. Rules for placing a join:
   - Look at the previous step to see what changed, and the next step: a later picture often shows the finished part from another side.
   - An arrow points at the exact hole it enters. Use it.
   - Count the distance between two pins and use the same distance on the part that receives them (pins 2 apart go into holes 2 apart).
   - Pins that come out the other side of a part are often visible in the picture: use them to find the hole.
   - When in doubt, assume the part or pin pair is centered, but only if the picture looks that way.
   - Count holes at high zoom (render the page at 200+ dpi). Pins usually sit in every second hole, not in neighbours. Use `~` when the picture is unclear and `?` when it is not shown. Look at the step before and after.

## The build language
- `ADD name partnum colour` - a part. Names never change once used (beam9-1, gear-3). Only part numbers from the set's parts list.
- `CONNECT a.point -> b.point LOCKED|TURNS|STIFF` - LOCKED = cross in cross (turn together), TURNS = axle in round hole or frictionless pin, STIFF = friction pin in round hole.
- Points are the catalog's names (`catalog/connections.csv`): hole1.. (round), axlehole1.. (cross), pin1.. / axle1.. (one per hole-length), `teeth` for gears.
- Optional: `MESH a.teeth b.teeth`, `RATIO a b x/y`, `GROUP g ... END` / `ATTACH g` for a side build.
- `WHY` is the reasoning. Training turns it into the model's thinking, so keep it short and real. We do not need a separate "think" instruction: the model learns to reason by seeing WHY lines in the examples.

## Layout
```
sets/<set>/steps.md            the whole set in plain steps (what you write)
sets/<set>/training.tbl + .jsonl  the same set as training text; every file starts with the instructions the model follows
sets/<set>/booklet.pdf         the original, unedited booklet
sets/<set>/parts_list.csv      official parts list
catalog/                       technic_parts.csv, connections.csv (every point of every part), mechanisms.json (mechanism types)
tools/check_notation.py        checks every join (point exists, the two fit, word is right)
training/                      export.py, train_qwen.py, system_prompt.md
docs/                          set_list.md (sets to do)
```
Set 8047 and 42175 now keep only booklet, parts list, training.tbl and training.jsonl (42175 also steps.md). 42061 and 42116 have steps.md, training.tbl and training.jsonl too.
NOT STARTED (parts list only; old step folders were deleted unconverted - redo from the booklet with "How to add a set" above): 8043, 8069, 42009, 42030, 8258, 42004, 42006, 42021, 42029, 42049, 42094, 42101, 42129 (parts list also incomplete), 8049.

## Finishing a NOT STARTED set (prompt for agents)
Example sets: **8047**, **42175**, **42061**, **42116**. A finished set looks exactly like them: open sets/42175/steps.md first and copy its wording style. These sets have no step folders left (unconverted old-format work was deleted rather than carried forward) - read the booklet directly, per "How to add a set" above. Give an agent this prompt, one set at a time:

```
Add set <set>. Copy the layout and wording style of sets/42175/steps.md. Work only inside sets/<set>/.

MAKE (in this order)
1. Write sets/<set>/steps.md: one block per step, in booklet order: read the booklet page directly (do not
   crop pictures or write annotation.json), ADD and CONNECT lines for that step, GROUP/END/ATTACH for side
   builds, plus ONE real WHY sentence per step.
2. python training/export.py  ->  writes sets/<set>/training.tbl + training.jsonl from that steps.md, and
   rebuilds training/data/train.jsonl + test.jsonl for every set that has one.

CHECK (all must pass before moving on)
- every part in parts_list.csv is used exactly once by the last step in steps.md.
- every point in steps.md exists in catalog/connections.csv.
- grep -c "TO WRITE" over steps.md and the set's training.tbl/training.jsonl is 0.

KEEP: booklet.pdf (unedited), parts_list.csv, steps.md, training.tbl, training.jsonl. Delete model.mpd and
booklet_map.csv once steps.md is done - they were only needed for the old per-step pipeline.

THEN: move the set out of NOT STARTED in "Layout" and "Status" of CLAUDE.md. Commit only sets/<set>, plus CLAUDE.md and .gitignore for those two edits.
Never delete before the checks pass. Never leave "TO WRITE" in a training file. Never force-push.
```
NOT STARTED sets have no step folders: use "How to add a set" above instead.
Don't use tools/build_set.py or write systems.json/mechanisms.json for a set's training files - training/export.py
builds training.tbl/.jsonl straight from steps.md now, and the THINK/MECH/STATE/MOTION lines those used to produce
were almost entirely restating ADD/CONNECT/WHY in prose. Dropped on purpose; don't bring them back.

## Mechanisms (what the model must understand)
A mechanism is a chain of parts that passes or changes motion. Every part in a build either belongs to one of these or holds the structure together. Full rules and failure modes: `catalog/mechanisms.json`.

| Mechanism | What it does |
| --- | --- |
| gear_pair | Passes turning from one parallel shaft to another. Changes speed and force by the tooth ratio and reverses direction. |
| idler_gear | A gear between two others: carries turning across a gap and keeps the direction the same. Doesn't change the overall ratio. |
| bevel_90 | Turns the drive through 90 degrees. |
| crown_90 | A crown gear (teeth on its face) meshes with a normal gear at 90 degrees, or with a worm or spur gear in line. |
| worm_drive | Big slow-down in one step, and self-locking: the gear can't turn the worm back, so the output holds its position (e.g. a boom stays up). |
| slewing_ring | Lets a whole upper structure rotate on a base. Big turntables have teeth so a gear can drive the rotation. |
| shaft_with_stops | An axle that carries parts and turns, held from sliding by stops at both ends. |
| knob_input | Where a person turns the machine: a gear, wheel or knob on the end of an input shaft. |
| hinge | Lets two parts swing about one axis. |
| linkage_4bar | Four bars joined by four hinges: moving one bar moves the others in a fixed way. Used to tip a stick or bucket as an arm moves. |
| push_rod | A rod with a hinge at each end transfers push and pull between two parts that swing. |
| crank_lever | A short arm on a shaft turns rotation into a back-and-forth swing (or the reverse). |
| track_loop | Tread links wrapped round wheels: spreads weight, lets the machine roll or be driven. |
| rigid_frame | Structure that keeps everything at the right distance. Not a moving mechanism, but every mechanism depends on it. |
| decoration | Looks only: panels, hoses, lights. Carries little or no load, never part of a drive. |
| pneumatic_circuit | A hand pump pushes air through hoses and switches into a cylinder; the cylinder rod pushes or pulls a part. Used where a real machine would use hydraulics. |

How to read a build: find the input (knob, crank, pump), follow the motion through the chain, name the output (what finally moves). A step is correct only if every part still turns or holds the way its mechanism needs (shaft turns in round holes, cross holes lock, gears sit at the right distance).

## Training (Qwen)
1. `python training/export.py` -> training/data/train.jsonl (+ test.jsonl, one whole set held out).
2. `pip install -r training/requirements.txt`, then `python training/train_qwen.py --model Qwen/Qwen2.5-1.5B-Instruct` on a GPU (24 GB).
3. Later: GRPO (TRL) with check_notation.py as the reward.
export.py reads every sets/<set>/steps.md; it writes that set's own training.jsonl/training.tbl too. One whole set is held out for test.

## Status (Oct 23, 2026)
- 8047 and 42175 (Volvo EC230, 199 steps, all 731 parts) are done: booklet, parts list, training.tbl, training.jsonl.
- 42175 joins: about 276 are `~` estimates and 326 are `?`. Steps 13-31 were re-counted at high zoom; steps 32-199 not yet. Most open joins are holes hidden behind other parts in the booklet pictures, so counting cannot fix them. Best fix: get the official 3D model (`python tools/get_set.py 42175 -`, needs internet access to library.ldraw.org) and import exact joins.
- 42061 and 42116 have steps.md, training.tbl and training.jsonl too.
- NOT STARTED: 8043, 8069, 42009, 42030, 8258, 42004, 42006, 42021, 42029, 42049, 42094, 42101, 42129, 8049. Old per-step annotation work for the last 9 was deleted unconverted; redo these from the booklet with "How to add a set" / "Finishing a NOT STARTED set" above.

## Saving (agents)
Work only inside `sets/<set>/`. Commit only that folder , no Co-Authored-By lines. Push every ~20 steps: `git add sets/<set> && git commit -m "<set>: steps ..." && git pull --rebase && git push`. Never force-push.
