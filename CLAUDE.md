# Lego AI - project guide for Claude Code

## What this project is
Build a brand-new AI made only for LEGO Technic. Real instruction booklets are translated into a build language (exact part-to-hole moves + what each part does + why). A small AI is trained from scratch on that language, then learns to design its own working builds. Booklets for its designs are drawn by LDraw + LPub3D, not by the AI.

Owner: Dennis. Wants plain language, no jargon, straight to the point.

## Files
- 00_README.md - what's in the folder
- 01_INSTRUCTIONS.md - rules for labeling a booklet step (JSON format, six verbs, the "why" fields)
- 02_FRAMEWORK.md - labeling pipeline and checks
- 02_PLAN.md - goal, status, 6-week plan, build language summary, training methods
- 03_training_data/8047.jsonl - labeled steps (JSON), one per line
- 03_training_data/8047.tbl - the same steps in the build language
- 04_reference/8047_parts_list.csv - official parts list (answer key)
- 05_booklets/ - booklet PDFs and one picture per step (steps/8047-step-NN.png; side builds 8047-<build>-step-NN.png)
- 03_training_data/8047_preview.md and 8047_part_matches.csv are GENERATED: run `python make_preview.py 03_training_data/8047.jsonl`, don't hand-edit
- 05_booklets/8047_steps.csv - map of the booklet: main steps and side builds (seat, body, arm, boom), pages, where each side build attaches
- 05_booklets/pages/ - every booklet page as a picture
- check_steps.py - checks a JSONL file against the parts list and rules
- Live docs: Plan https://claude.ai/artifact/3UqS1JRTkBuiq9jE5KFjfm, Build Language https://claude.ai/artifact/TXzA7joTEvVGAZ2y94mvUw, Framework https://claude.ai/artifact/9agc7uxAr16TjJK2EYirj4

## Build language (short)
STEP n | ADD name partnum color | CONNECT a.point -> b.point | ANGLE name deg | MESH a.teeth b.teeth | GROUP g ... END / ATTACH g | DOES a VERB b (HOLDS, CARRIES, SPINS_ON, DRIVES, LOCKS, SUPPORTS) | RATIO a b x/y | PATTERN name | REQUEST ...
- `?` = join not shown in the picture (checker fills it in). `#` = note for people, stripped before training.
- Points: beams hole1..N (bent beams from short-arm end); pins end1/end2; long pin with stop ring pin/axlehole; axle pins pin/axle; axles end1/end2/mid; connectors axlehole/pinhole/holeN; gears axlehole/teeth; turntable base.holeN/top.holeN/top.teeth_out/base.teeth_in.
- Names are permanent (pin-L, gear-3, beam9-X). Only part numbers from the set's parts list.

## How to label a new step
1. Crop the step picture from the booklet PDF (PyMuPDF) into 05_booklets/steps/.
2. Look at the picture and the next pages to confirm what later steps use it for.
3. Write the JSON entry (see 01_INSTRUCTIONS.md) AND the build-language lines.
4. Run `python3 check_steps.py 03_training_data/<file>.jsonl 04_reference/<set>_parts_list.csv`; fix anything listed.
5. Flag anything the picture doesn't show (needs_review + review_note, `?` in the language).

## Status (Oct 22, 2026)
Set 8047 fully labeled: main steps 1-56 + side builds seat (11), body (5), arm (12), boom (4) = 88 examples. All 252 pieces used exactly once; all checks pass. 25 high / 63 medium confidence; 47 flagged needs_review (mostly exact hole numbers, marked `?` in the .tbl). Gear drive path (which knob drives what) is not confirmed.

## Next tasks, in order
1. Review the needs_review steps of 8047 (start with the gear train, steps 19-34 and the arm build), JSON + build language.
2. Write a parser/checker for the build language (names exist before use, parts on the list, counts, verbs).
3. Check every part in 8047's list exists in the LDraw parts library.
4. Build the converter: build language -> LDraw .ldr file with STEP markers (for LDCad viewing and LPub3D booklets).
5. Build the connection-points table from LDraw part shapes (LDCad snap data as a starting point).
