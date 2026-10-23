# Lego AI - project guide

## What this project is
An AI made only for LEGO Technic. Real instruction booklets are turned into step-by-step build text. A Qwen model (Apache 2.0, start with Qwen2.5-1.5B/3B-Instruct) is fine-tuned on it with LoRA, then improved with GRPO using our checkers as the score.

Owner: Dennis. Plain language, no jargon, straight to the point. Save tokens.

## How to add a set (the only workflow)
1. Make `sets/<set>/` with `booklet.pdf` (git-ignored) and `parts_list.csv` (Rebrickable).
2. Read the booklet pages directly. Do NOT crop pictures, do NOT write annotation.json, systems.json, mechanisms.json or booklet_map.csv.
3. Write ONE file: `sets/<set>/steps.md`, one block per step (see 42175 for an example):
```
## Step 18 (page 18)
ADD pump-beam-1 32278 darkgray
CONNECT pump-pin-1.pin1 -> pump-beam-1.hole4 STIFF
WHY one plain sentence: what this step builds and what it is for.
```
4. Check: every part in the parts list used exactly once by the end; every point exists in `catalog/connections.csv`.
5. Count holes at high zoom (render the page at 200+ dpi). Pins usually sit in every second hole, not in neighbours. Use `~` when the picture is unclear and `?` when it is not shown. Look at the step before and after.

## The build language
- `ADD name partnum colour` - a part. Names never change once used (beam9-1, gear-3). Only part numbers from the set's parts list.
- `CONNECT a.point -> b.point LOCKED|TURNS|STIFF` - LOCKED = cross in cross (turn together), TURNS = axle in round hole or frictionless pin, STIFF = friction pin in round hole.
- Points are the catalog's names (`catalog/connections.csv`): hole1.. (round), axlehole1.. (cross), pin1.. / axle1.. (one per hole-length), `teeth` for gears.
- Optional: `MESH a.teeth b.teeth`, `RATIO a b x/y`, `GROUP g ... END` / `ATTACH g` for a side build.
- `WHY` is the reasoning. Training turns it into the model's thinking, so keep it short and real. We do not need a separate "think" instruction: the model learns to reason by seeing WHY lines in the examples.

## Layout
```
sets/<set>/steps.md            the whole set, all steps (new sets: only this + booklet + parts list)
sets/<set>/booklet.pdf         git-ignored
sets/<set>/parts_list.csv      official parts list
catalog/                       technic_parts.csv, connections.csv (every point of every part), mechanisms.json (mechanism types)
tools/check_notation.py        checks every join (point exists, the two fit, word is right)
training/                      export.py, train_qwen.py, system_prompt.md
docs/                          set_list.md (sets to do)
```
Older sets (8047, 42004, ...) still have step folders from the old workflow (other agents are working on them). Do not do that for new sets.

## Training (Qwen)
1. `python training/export.py` -> training/data/train.jsonl (+ test.jsonl, one whole set held out).
2. `pip install -r training/requirements.txt`, then `python training/train_qwen.py --model Qwen/Qwen2.5-1.5B-Instruct` on a GPU (24 GB).
3. Later: GRPO (TRL) with check_notation.py as the reward.
(export.py still reads the old step folders; it needs a small change to read steps.md.)

## Status (Oct 23, 2026)
- 8047 fully labeled (old format). 42175 (Volvo EC230, 199 steps, all 731 parts) is now only `sets/42175/steps.md` + parts list.
- 42175 joins: about 276 are `~` estimates and 328 are `?`. Steps 13 and 18 were re-counted at high zoom; steps 19-199 not yet.
- Other sets (42004 ... 42116) come from 3D models and are labeled by other agents.

## Saving (agents)
Work only inside `sets/<set>/`. Commit only that folder (never booklet PDFs), no Co-Authored-By lines. Push every ~20 steps: `git add sets/<set> && git commit -m "<set>: steps ..." && git pull --rebase && git push`. Never force-push.
