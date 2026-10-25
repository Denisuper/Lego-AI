# Lego AI - project guide

## What this project is
An AI made only for LEGO Technic. Real instruction booklets are turned into step-by-step build text. A vision-language model reads booklet pages and parts lists directly, is fine-tuned with LoRA, then improved with GRPO where the reward is not a single number but a structured critique: pass/fail plus plain-language reasons for every failure. The model learns both what is wrong and why.

Owner: Dennis. Plain language, no jargon, straight to the point. Save tokens.

## How everything works (end to end)

1. **Input**: a booklet.pdf page image plus the set's parts_list.csv. The model sees the picture; it does not see cropped annotations or JSON sidecars.
2. **Output**: one build-language block per step (ADD, CONNECT, WHY lines — see "The build language" below). The WHY line is the model's reasoning: one real sentence grounded in the picture and the previous/next steps. There is no separate "think" instruction; reasoning is learned from seeing WHY lines in training examples.
3. **Check, two stages**:
   - **Stage 1 — geometric (cheap)**: tools/check_notation.py validates every join — the point exists in catalog/connections.csv, the two parts fit, the connection word (LOCKED/TURNS/STIFF) is legal for that pair. Instant.
   - **Stage 2 — functional (expensive)**: the same script then traces motion from each input (knob, crank, pump) through the mechanism chain using catalog/mechanisms.json rules and failure modes. Does the crank actually reach the output? Does the worm drive self-lock? Does a four-bar have a free pivot at every corner? Geometry-clean builds that are dead weight — every join legal, nothing moves — get flagged here.
4. **Reward (non-scalar)**: the checker returns a list of critique objects, not one float. Each has a severity (error/warning/info), a code, the exact line it failed on, and a one-sentence explanation a human could act on. GRPO's scalar component is -1 per error and -0.25 per warning; the critique texts are concatenated into the prompt prefix on the next attempt so the model conditions on its own mistakes. This is process supervision: the signal is per-failure and verbal.
5. **Loop**: generate a candidate step block, score it in both stages, feed critiques back, regenerate. Repeat until clean or a step budget is hit. Stage 1 runs on everything; stage 2 only on geometry-clean survivors, because simulation is slow.

## Reward format
check_notation.py with --jsonl emits one object per finding:
```json
{"severity": "error", "code": "WORM_NO_STOP", "line": 12, "message": "line 12 (step 4): worm worm-1 (4716) drives gear-2 but has no LOCKED stop — per worm_drive rules the worm walks along its shaft and loses mesh"}
```
Severity levels: error (illegal join or dead mechanism, must fix), warning (plausible but unverified or suboptimal), info (style nits). Codes include POINT_MISSING, NO_FIT, WRONG_MODE, MESH_NO_TEETH, USED_BEFORE_ADD, WORM_NO_STOP, GEAR_NOT_LOCKED, FRICTION_ON_HINGE, UNREFERENCED_PART. GRPO reward = -1 per error, -0.25 per warning, 0 for clean.

## How to add a set (the only workflow)
1. Make `sets/<set>/` with the original `booklet.pdf` (commit it unedited; add `!sets/<set>/booklet.pdf` to .gitignore) and `parts_list.csv` (Rebrickable).
2. Read the booklet pages directly. Do NOT write steps.md: training.tbl/.jsonl already hold every step. Do NOT crop pictures, do NOT write annotation.json, systems.json, mechanisms.json or booklet_map.csv.
3. Write TWO files directly in the 42175 style — copy `sets/42175/training.tbl` header verbatim, swap set name:
   - `sets/<set>/training.tbl` — plain text: the header comment block, then `STEP N` followed by that step's ADD, CONNECT, optional GROUP/END/ATTACH, and WHY lines.
   - `sets/<set>/training.jsonl` — one JSON object per step: `{"set": "Set <set> - <title>", "step": "N", "messages": [...]}`. System prompt identical to 42175. User message has SET line, PARTS SO FAR (condensed to counts past 60 items), LAST STEPS (previous four steps in full), and the write-step prompt. Assistant message is the ADD/CONNECT/WHY block.
4. Check: every part in the parts list used exactly once by the last step; every point exists in `catalog/connections.csv`; grep -c "TO WRITE" over both training files is 0.
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
- Optional: `MESH a.teeth b.teeth`, `RATIO a b x/y`, `GROUP g ... END` / `ATTACH g` for a side build, `DOES a DRIVES b`, `PATTERN linkage`.
- `WHY` is the reasoning. Training turns it into the model's thinking, so keep it short and real. We do not need a separate "think" instruction: the model learns to reason by seeing WHY lines in the examples.

## Layout
```
sets/<set>/training.tbl + .jsonl  the whole set as training text; every file starts with the instructions the model follows
sets/<set>/booklet.pdf         the original, unedited booklet
sets/<set>/parts_list.csv      official parts list
catalog/                       technic_parts.csv, connections.csv (every point of every part), mechanisms.json (mechanism types, rules, failure modes)
tools/check_notation.py        two-stage checker: geometric legality + functional motion tracing; emits structured critique JSONL
training/                      export.py, train_qwen.py, system_prompt.md
docs/                          set_list.md (sets to do)
```
Finished sets keep only booklet, parts list, training.tbl and training.jsonl. The steps live in training.tbl/.jsonl, so there is no separate steps.md per set (never add one). 42114 in progress: training.tbl + training.jsonl for steps 1-54, continuing from booklet page 37.
NOT STARTED (parts list only; old step folders were deleted unconverted - redo from the booklet with "How to add a set" above): 8043, 8069, 42009, 42030, 8258, 42004, 42006, 42029, 42094, 42129 (parts list also incomplete), 8049.

## Finishing a NOT STARTED set (prompt for agents)
Example sets: **8047**, **42175**, **42061**, **42116**. A finished set looks exactly like them: open sets/42175/training.tbl first and copy its header and STEP format. These sets have no step folders left (unconverted old-format work was deleted rather than carried forward) - read the booklet directly, per "How to add a set" above. Give an agent this prompt, one set at a time:

```
Add set <set>. Copy the layout and wording style of sets/42175/training.tbl. Work only inside sets/<set>/.

MAKE (in this order)
1. Write sets/<set>/training.tbl and sets/<set>/training.jsonl directly from the booklet (do not
   write steps.md, do not run export.py, do not crop pictures or write annotation.json).
   One STEP block per step in booklet order: ADD and CONNECT lines, GROUP/END/ATTACH for side
   builds, plus ONE real WHY sentence per step. jsonl: one object per step with set, step,
   messages[system, user, assistant] per the 42175 schema.
2. grep -c "TO WRITE" over both training files must be 0.

CHECK (all must pass before moving on)
- every part in parts_list.csv is used exactly once by the last step.
- every point in the training files exists in catalog/connections.csv.
- python tools/check_notation.py sets/<set>/training.tbl exits 0 (no error-severity critiques in either stage).

KEEP: booklet.pdf (unedited), parts_list.csv, training.tbl, training.jsonl. Delete model.mpd and
booklet_map.csv once the training files are done - they were only needed for the old per-step pipeline.

THEN: move the set out of NOT STARTED in "Layout" and "Status" of CLAUDE.md. Commit only sets/<set>, plus CLAUDE.md and .gitignore for those two edits.
Never delete before the checks pass. Never leave "TO WRITE" in a training file. Never force-push.
```
NOT STARTED sets have no step folders: use "How to add a set" above instead.
Don't use tools/build_set.py or write systems.json/mechanisms.json for a set's training files.

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

## Training (Qwen2.5-VL-7B)
1. Cat every sets/<set>/training.jsonl into training/data/train.jsonl (+ test.jsonl, one whole set held out).
2. `pip install -r training/requirements.txt`, then `python training/train_qwen.py --model Qwen/Qwen2.5-VL-7B-Instruct` on a GPU with 24+ GB VRAM (or 4-bit quant on ~10 GB).
3. Later: GRPO (TRL) with check_notation.py's two-stage critiques as the reward — scalar mean plus verbal feedback, per "Reward format" above. Stage 1 filters; stage 2 scores survivors.

## Status (Oct 24, 2026)
- 42006 (Excavator, 720 advertised pieces): main model transcribed through all 89 global steps, ending at book 2 page 26, with 695 inventory entries including the sticker sheet. Both training files match and pass the notation checker with 0 errors; 831 joins match the registered read-only OMR reference and 204 are unavailable or uncertain, including modern track clips, hose ends and the small actuator. There are 41 unknown (?) and 25 estimated (~) endpoints. Full motion is not verified. Original PDFs verified against LEGO assets 6037216 and 6037218; compressed copies are 47.0% and 56.2% smaller at 160 dpi JPEG quality 75. All 25 unused inventory parts are reserved for the optional 8293 motor conversion on book 2 pages 31-41. The CSV already matches the PDF bush counts (16 light grey and 3 red); no inventory correction was necessary. The conversion introduces external motor, switch, battery and clutch gear plus removal and reuse of existing assemblies. These are deliberately not invented into the manual build. Whole-inventory completion is pending a separate conversion variant or an agreed main-build inventory scope. Keep model.mpd and booklet_map.csv until that requirement is resolved.
- 42049 (Mine Loader, 476 inventory pieces, 164 steps): complete booklet transcription in training.tbl + training.jsonl; exact inventory match by part and colour; 0 checker errors. Main-build originals verified against LEGO downloads: booklet.pdf is book 1; booklet-part2.pdf is book 2. Reading copies are 40.0% and 30.5% smaller. Existing booklet2.pdf is the alternate cutter build and is not used. A read-only OMR comparison matched 572 joins after registering catalog pin orientations; 42 joins were unavailable or uncertain. There are 9 estimated (~) endpoints and 56 unknown (?) endpoints, including uncataloged wheel, stud and ball-socket interfaces. The checker emits 451 UNREFERENCED_PART warnings; full motion and geometry remain unverified. The OMR substitutes a four-length axle for the booklet's grey three-length linkage axle, so the PDF and inventory take precedence there. Old model.mpd and booklet_map.csv were removed after checks passed; reference copies remain outside the repo. The smooth round axle-bearing checker fix has 6 passing regression tests.
- 42133 (Telehandler, 143 pieces, 59 steps): complete booklet transcription in training.tbl + training.jsonl; exact inventory match by part and colour; 0 checker errors. There are 96 estimated (~) endpoint references and 16 unknown (?) references, including wheel/tyre/stud interfaces absent from the catalog. The checker also emits 142 UNREFERENCED_PART warnings; this is not a fully verified motion model. Original booklet.pdf is preserved; booklet-compressed.pdf is a 220 dpi reading copy (24.2% smaller).
- 42117 (Race Plane, 154 inventory pieces including the sticker sheet, 55 steps): complete booklet transcription in training.tbl + training.jsonl; exact inventory match by part and colour; 0 checker errors. There are 88 estimated (~) endpoints, 86 unknown (?) endpoints, and 4 endpoint references on parts absent from the catalog (18677, 15790, 61800). Stud and tyre interfaces account for many unknowns. The checker emits 144 UNREFERENCED_PART warnings; full motion and geometry remain unverified. Original booklet.pdf is preserved; booklet-compressed.pdf is a 220 dpi reading copy (27.8% smaller).
- 8047 and 42175 (Volvo EC230, 199 steps, all 731 parts) are done: booklet, parts list, training.tbl, training.jsonl.
- 42175 joins: about 276 are `~` estimates and 326 are `?`. Steps 13-31 were re-counted at high zoom; steps 32-199 not yet. Most open joins are holes hidden behind other parts in the booklet pictures, so counting cannot fix them. Best fix: get the official 3D model (`python tools/get_set.py 42175 -`, needs internet access to library.ldraw.org) and import exact joins.
- 42061 and 42116 are done too.
- 42114 in progress: training.tbl + training.jsonl for steps 1-54 (booklet pages 6-43). Remaining steps 55-508 from pages 37-300 still to transcribe.
- sets/differentials/ and sets/gearboxes/ are fan MOCs, not official sets. Done (training.tbl + training.jsonl, 0 errors from check_notation.py): MOC-266362 (12 steps), MOC-226025 (41 steps), MOC-65060 (47 steps), MOC-150019 (32 steps), MOC-51409 (88 steps, 251 parts - largest in the project), MOC-50877 (36 steps). Parts lists only (no training files yet): MOC-171508 (+ parts_list_booklet2.csv for its alternate booklet), MOC-180337, MOC-74158, MOC-187095, MOC-54174, MOC-191057, MOC-6speed-gearbox (unconfirmed - no part numbers in that booklet), Differential-v2, MOC-157410, MOC-158072, MOC-185197, MOC-31209, MOC-31377, MOC-194194. Confidence on the fan MOCs is lower than 8047/42175/42061/42116: many small similar-looking connector parts are a best reading of the render, and several (6speed-gearbox, Differential-v2, etc.) have no printed part numbers in their booklet at all.
- 42101 (Dune Buggy, 117 pieces, 36 steps) is done: booklet, parts list, training.tbl, training.jsonl, 0 errors from check_notation.py.
- 42021 (Snowmobile, 186 pieces, 38 steps) is done: booklet (main A-model only; the B-model alternate booklet was deleted as it doesn't match parts_list.csv's build), parts list, training.tbl, training.jsonl, 0 errors from check_notation.py.
- NOT STARTED: 8043, 8069, 42009, 42030, 8258, 42004, 42006, 42029, 42094, 42129, 8049. Old per-step annotation work for the last 9 was deleted unconverted; redo these from the booklet with "How to add a set" above.

## Saving (agents)
Work only inside `sets/<set>/`. Commit only that folder, no Co-Authored-By lines. Push every ~20 steps: `git add sets/<set> && git commit -m "<set>: steps ..." && git pull --rebase && git push`. Never force-push.
