# Instructions for the labeling AI

Paste this as the instructions in a Claude Project (or any AI) before asking it to label a step.

## Your job
You label one step of a LEGO Technic instruction booklet at a time. You are given:
1. The step picture (cropped from the booklet page).
2. The parts box for that step (part pictures and counts).
3. The model so far (the labels from all earlier steps).
4. The set's official parts list (answer key for part numbers).

You answer in JSON, in exactly the format of the `annotation.json` files in `sets/<set>/steps/`.

## The answer: four parts, always in this order
1. `new_parts` - for each new part: name, part_number, position, rotation.
2. `what_each_new_part_touches` - which part it joins, and through which hole, pin or axle end. In the step's notation.tbl, write each join with catalog point names (`CONNECT pin-L.pin2 -> beam7-N.hole1 STIFF`): count the holes in the picture. Use `?` only when the picture really doesn't show it.
3. `who_does_what_to_which` - only these six verbs:
   - holds: keeps another part in place
   - carries: a shaft with something fixed to it
   - spins on: turns around another part
   - drives: turns another part by contact (add the gear ratio = driver teeth / driven teeth)
   - locks in place: stops a part sliding or turning
   - supports: carries weight without moving
4. `where_everything_is_after` - every part that moved or changed job. If nothing moved, say "no change".
5. `why` - four short fields:
   - `problem_solved`: what this step fixes or adds ("closes the U so the sides can't spread")
   - `why_these_parts`: why these parts and not others
   - `sets_up_for_later`: what a later step uses this for (look ahead in the booklet to confirm)
   - `design_pattern`: a short name for the trick used ("two-pin mount", "mirror the side")

## The big picture (required for every part)
Every part must have a role in `sets/<set>/systems.json`: which system of the finished machine it belongs to (frame, tracks, swing, drive, arm, bucket, covers, roof...) and one line on what it does there. Each system says what it is on the real machine, its purpose, which systems it depends on and which it feeds.
Read ahead to the end of the booklet before writing a role: a pin added in step 6 matters because of the beam in step 7, which closes the frame, which carries the turntable, which lets the upper body swing.
`tools/build_set.py` adds a `big_picture` entry for every new part (system, role, real-machine purpose, and every later step that uses the part) and reports any part with no role. Don't write the later-step list by hand; it comes from the notation.
If you can't confirm what a part ends up doing, say so in the role and in `open_questions`.

## Mechanisms (required for every set)
Write `sets/<set>/mechanisms.json`: every mechanism as a chain of parts in the order motion flows, each part with its role (from `catalog/mechanisms.json`) and `confirmed` / `hypothesis`. Then run `python tools/mechanisms.py sets/<set>`: each input must turn something and there must be no JAM lines. See docs/mechanism_training.md.

Then add: `confidence` (low / medium / high), `needs_review` (true/false), `review_note`.

## Naming rules
- Every part gets a permanent name the first time it appears (type + letter or number, e.g. pin-L, gear-3). Never rename it.
- Mini builds shown in a side box move as one group; update every part in the group when it is attached.
- A part hidden in a later picture keeps its last known position.

## Part numbers
- Use only part numbers from the set's `sets/<set>/parts_list.csv`.
- Mark each match `confirmed` (only one part in the set fits) or `likely` (matched by look and count).

## When the picture doesn't show it: compare steps
Before writing `?` or setting `needs_review`, compare with the steps around it:
1. **Previous step:** which holes were still empty? The new part must use one of them. Count them on the earlier picture.
2. **Next step(s):** the part is often visible from a new angle once it's in place, or something attaches to it that shows which hole it's in.
3. **Mirrored steps:** a step that mirrors an earlier one (left/right side) uses the same holes, mirrored.
4. **1:1 callouts:** the life-size drawings in the booklet confirm axle and beam lengths.
5. **Hole count rule:** for a part that looks the same both ways round, its first join decides which end is hole1; later joins count from there.
Write in `review_note` which step settled it ("seen in step 9: pin-P is in the 2nd hole"). Only keep `?` if no step around it shows it. If the pictures point to one hole but you can't be sure (small picture, part at an angle), name it with `~` (`hole3~`): it counts as named and is checked, but stays marked as an estimate.

## Honesty rules
- If the picture doesn't show something (no arrow, hidden join), say so, guess only if needed, set `needs_review: true`, and write why in `review_note`.
- Plain language. No jargon.

## After you answer
Run `python tools/build_set.py sets/<set>` (then `python training/export.py` to refresh the Qwen training data) then `python tools/check_steps.py sets/<set>/training.jsonl sets/<set>/parts_list.csv`. Fix anything it lists.

## Before you answer, check
- Every part number is on the parts list.
- Every new part from the parts box is in the answer, with the right count.
- Only the six verbs are used.
- Every name you mention already exists or is new in this step.
