# Agent task: write the reasoning for one set

You label ONE set (`sets/<SET>/`) in the same style as `sets/8047/`, the finished example. Work only inside `sets/<SET>/`.

## Setup
```
git clone https://github.com/Denisuper/Lego-AI.git lego-<SET>   (use a fresh temp folder; gh is logged in)
cd lego-<SET>
pip install pymupdf        (if missing)
python tools/get_set.py <SET> -        (downloads the booklet PDF(s) + 3D model; parts list is already in the repo)
```
Read first: `CLAUDE.md`, `docs/labeling_instructions.md`, `docs/mechanism_training.md`, `catalog/mechanisms.json`, and `sets/8047/` (`systems.json`, `mechanisms.json`, a few `steps/*/annotation.json` and `notation.tbl`, and `preview.md`).

## Two kinds of set
- **Imported from a 3D model** (`sets/<SET>/model.mpd` exists): every step folder already has the exact parts, `POS` lines and joins (`CONNECT ... LOCKED|TURNS|STIFF`, `MESH`/`RATIO`). Do NOT change those lines unless a booklet picture clearly shows the import is wrong (then fix it and say so in `review_note`). Your job is the reasoning (below).
- **No 3D model** (8043, 8069, 42009, 42030): label from the booklet pictures exactly like 8047: crop each step picture into `steps/<build>-NN/picture.png` (PyMuPDF), write `notation.tbl` (ADD + CONNECT with catalog point names from `catalog/connections.csv`, `~` for estimates, `?` for unseen) and `annotation.json`, and create `booklet_map.csv`. Compare with the previous and next steps before writing `?`.

## The reasoning to write
1. Look through the booklet (render pages with PyMuPDF and read them) and the finished model. Work out every mechanism: what each knob, lever or motor moves, and how.
2. Write `sets/<SET>/systems.json` (same format as 8047): every system of the machine, what it is on the real machine, its purpose, depends_on / feeds, and a one-line role for EVERY part name used in the notation (regex keys like `"tread-.*"` are allowed for repeated parts).
3. Write `sets/<SET>/mechanisms.json` (same format as 8047): every mechanism as a chain of parts in the order motion flows, each with a role, a link and `confirmed` / `hypothesis`.
4. In every `steps/*/annotation.json`, replace every `TO WRITE`:
   - `input.model_so_far`: one sentence on what is built before this step.
   - each new part's `rotation`: fixed / spins / swings / spins with <part>.
   - `where_everything_is_after`: what changed, plus "everything else: no change".
   - `why`: `problem_solved`, `why_these_parts`, `sets_up_for_later` (read ahead in the booklet), `design_pattern`.
   - Keep `confidence` / `needs_review` / `review_note` honest.
   Plain language, no jargon. Full sentences, like 8047.
5. Check:
```
python tools/build_set.py sets/<SET>              (must print no "NO ROLE" line)
python tools/check_steps.py sets/<SET>/training.jsonl sets/<SET>/parts_list.csv
python tools/check_notation.py sets/<SET>/training.tbl
python tools/mechanisms.py sets/<SET>             (no JAM lines; if there is one, fix the label or explain it in mechanisms.json)
grep -rl "TO WRITE" sets/<SET>/steps               (must find nothing)
```

## Saving
- Commit only `sets/<SET>/` (booklet PDFs are git-ignored; never add them). No "Co-Authored-By" or "Generated with" lines in commit messages.
- Push often (e.g. every ~20 steps) so work isn't lost:
```
git add sets/<SET> && git commit -m "<SET>: reasoning for steps ..." && git pull --rebase && git push
```
  If the push is rejected, `git pull --rebase` and push again. Never force-push. Never edit files outside `sets/<SET>/`; if a shared tool has a bug, describe it in your final report instead.

## Final report (short)
Steps done, open questions, any import errors you fixed, any tool bugs found.
