# Agent task: write one set

Work only inside `sets/<SET>/`.

## Setup
```
git clone https://github.com/Denisuper/Lego-AI.git lego-<SET>
cd lego-<SET>
pip install pymupdf
python tools/get_set.py <SET> -      (booklet PDF + 3D model if one exists; parts list is in the repo)
```
Read `CLAUDE.md` first.

## Job
1. If `sets/<SET>/model.mpd` exists, the step folders already have exact parts and joins: do not change them unless the booklet clearly shows an error. Add only the missing reasoning (`why` in each annotation.json, plain sentences).
2. If there is no 3D model: read the booklet pages and write `sets/<SET>/steps.md` as described in CLAUDE.md. No picture crops, no annotation.json, no systems.json / mechanisms.json.
3. Check: `python tools/check_notation.py` on the joins, and every part in the parts list used exactly once.

## Saving
Commit only `sets/<SET>/` (never booklet PDFs). No "Co-Authored-By" or "Generated with" lines. Push every ~20 steps: `git add sets/<SET> && git commit -m "<SET>: steps ..." && git pull --rebase && git push`. Never force-push. Never edit outside `sets/<SET>/`.

## Final report (short)
Steps done, open questions, tool bugs found.
