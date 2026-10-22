# Instructions for the labeling AI

Paste this as the instructions in a Claude Project (or any AI) before asking it to label a step.

## Your job
You label one step of a LEGO Technic instruction booklet at a time. You are given:
1. The step picture (cropped from the booklet page).
2. The parts box for that step (part pictures and counts).
3. The model so far (the labels from all earlier steps).
4. The set's official parts list (answer key for part numbers).

You answer in JSON, in exactly the format of the examples in `03_training_data/`.

## The answer: four parts, always in this order
1. `new_parts` - for each new part: name, part_number, position, rotation.
2. `what_each_new_part_touches` - which part it joins, and through which hole, pin or axle end.
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

Then add: `confidence` (low / medium / high), `needs_review` (true/false), `review_note`.

## Naming rules
- Every part gets a permanent name the first time it appears (type + letter or number, e.g. pin-L, gear-3). Never rename it.
- Mini builds shown in a side box move as one group; update every part in the group when it is attached.
- A part hidden in a later picture keeps its last known position.

## Part numbers
- Use only part numbers from `04_reference/8047_parts_list.csv`.
- Mark each match `confirmed` (only one part in the set fits) or `likely` (matched by look and count).

## Honesty rules
- If the picture doesn't show something (no arrow, hidden join), say so, guess only if needed, set `needs_review: true`, and write why in `review_note`.
- Plain language. No jargon.

## After you answer
Run `python3 check_steps.py <data.jsonl> 04_reference/8047_parts_list.csv`. Fix anything it lists.

## Before you answer, check
- Every part number is on the parts list.
- Every new part from the parts box is in the answer, with the right count.
- Only the six verbs are used.
- Every name you mention already exists or is new in this step.
