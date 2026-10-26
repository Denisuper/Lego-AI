# Lego AI - project guide

Training data for LEGO Technic builds, transcribed from instruction booklets. Owner: Dennis. Use plain language.

## Source files and layout

- `sets/<set>/booklet.pdf`: source booklet. Preserve official originals unchanged.
- `booklet-part2.pdf`, `booklet-part3.pdf`, etc.: additional volumes. Some older local sources include alternate models; check the cover before transcribing.
- `booklet-compressed.pdf` and similar names: optional reading copies; keep the original.
- `parts_list.csv`: inventory, with quantity, part number, colour and name.
- `training.tbl` and `training.jsonl`: the hand-written build steps and matching chat examples.
- `catalog/connections.csv`: named connection points and allowed connection types.
- `catalog/technic_parts.csv`, `catalog/mechanisms.json`: part and mechanism references.
- `docs/dataset_status.csv`: current coverage, inventory differences and checker results for every set.
- `docs/booklets.csv`: PDF page counts, hashes and available source information.

Fan models live in `sets/differentials/`, `sets/gearboxes/` and the existing `sets/MOC-183729/`. They are not official LEGO sets. Question marks in MOC inventory part numbers indicate unresolved identification.

All booklet PDFs use Git LFS. Run `git lfs install` and `git lfs pull` after cloning. The 8862 and 8880 PDFs contain the unmodified numbered page scans from Brick Instructions; they are not original LEGO digital PDFs. The merged 42129 `booklet-reference.pdf` is a compressed 384-page edition; `booklet.pdf` is the official 388-page edition. Do not assume their page numbers match.

Optional `model.mpd` reference files remain for unfinished official sets. They can help check geometry, but the PDF takes precedence. Obsolete per-step annotation folders, booklet maps, systems sidecars and their generators are retired; backups were saved outside the repo during cleanup.

## Writing training data

1. Read the source booklet directly. Do not create `steps.md`, cropped annotations, `annotation.json`, `booklet_map.csv`, `systems.json` or per-set `mechanisms.json`.
2. Copy the header of `sets/42175/training.tbl` verbatim. Use consecutive global `STEP N` numbers in source order, including side-build steps.
3. Write the build block and one plain `WHY` line explaining what the step builds and why. Keep estimates visible: `~` means estimated, `?` means unknown. Do not replace unknown points with invented exact joins.
4. Write matching JSONL: one object with `set`, string `step` and `messages` containing system, user and assistant. The system text is identical to 42175. The user has SET, PARTS SO FAR, LAST STEPS (the previous four full steps), and the write-step prompt with the source page. Condense parts to counts after 60 items. The assistant is exactly the STEP body without its STEP heading.
5. Keep the original PDF and inventory. Compare the complete build against every inventory part and colour; optional motor conversions may need a separate inventory scope.

## Build language

- `ADD name partnumber colour`: add one uniquely named part instance. Names do not change after introduction.
- `CONNECT a.point -> b.point LOCKED|TURNS|STIFF`: join catalog points.
- `LOCKED`: axle cross in cross hole, turning together.
- `TURNS`: shaft in a round bearing or a frictionless pin connection.
- `STIFF`: friction pin in a round hole or a known friction fit.
- Points use catalog names such as `hole1`, `axlehole1`, `pin1`, `axle1` and `teeth`.
- Optional `MESH a.teeth b.teeth`, `RATIO a b x/y`, `GROUP name` / `END` / `ATTACH name`, `DOES a DRIVES b` and `PATTERN name`.
- `WHY`: one grounded explanation per step. Legacy THINK, MECH, STATE and MOTION scaffolding is retired.

Use the arrow, visible pin exits and neighbouring pages to identify the join. Count holes at high zoom when needed. Shafts that must turn need round bearings; cross holes lock shafts. Friction on a moving pivot must agree with the actual part. Preserve uncertainty when the picture or catalog does not resolve an interface.

## Validation and training

```sh
python tools/audit_dataset.py
python tools/check_notation.py sets/<set>/training.tbl
python -m unittest discover -s tools -p test_check_notation.py
python training/pack_data.py
```

The audit checks matching table/chat content, the shared prompt, sequential steps, one WHY, unique names, previous-step context, booklet coverage, inventory by part and colour, and checker findings. It updates `docs/dataset_status.csv`. `--strict` fails when any transcribed set needs review; existing unfinished data currently causes that failure.

The notation checker checks catalog legality and applies mechanism heuristics. It is not a physical simulation and does not prove full motion or geometry. Its warnings and uncertainty markers still matter when there are zero errors.

`training/pack_data.py` only includes sets marked ready by the audit and holds out one entire set for testing. `--holdout <set-folder>` chooses it explicitly. Generated `training/data/` and model output are ignored. The current trainer consumes text chat messages; PDF page images are not yet connected to it.

## Current work

Use `docs/dataset_status.csv` for actual state instead of a duplicated completed-set list. The cleanup normalized 29 training pairs with 1,779 steps. No new booklet steps were invented during formatting.

- The user resumed 42094 and 42114 and requested complete training for both, followed by Defender 42110. Finish their source builds and reconcile every inventory part and colour. 42094 is now complete through source step 221, page 135, including both logs: all 827 inventory parts match by part and colour, zero notation errors, no duplicate names and balanced side-build groups. Its 138 unknown and 50 estimated endpoints remain explicit; catalog checks do not establish physical correctness. The earlier pause is revoked by the user's request. 42114 is now complete through source step 691, page 436, with all 2,193 inventory entries accounted for, including the sticker sheet: zero missing or extra parts, zero notation errors and 93 balanced assembly groups. Its 474 unknown and 402 estimated endpoints remain explicit. Defender 42110 is now transcribed through step 342, page 208: 1000 introduced parts, zero inventory excess and zero notation errors. Continue at step 343, page 209, then complete and reconcile 42110 before other sets.
- 42006 has all 89 main-build steps and 695 inventory entries. Its 25 remaining parts are reserved for the optional 8293 conversion, which also uses external kit components. Do not add those parts to arbitrary main-build steps.
- 42114's original 54-step draft was replaced after 572 notation errors. Its source transcription is now complete through step 691, page 436. The table and JSONL match, all 2,193 inventory entries reconcile by part and colour, and there are no notation errors or duplicate names. The audit marks it ready; its 474 unknown and 402 estimated endpoints still require physical/interface review. See `docs/42114-repair.md`.
- 8047's 56 main steps and 32 side-build steps are now 88 consecutive global steps. Six ADD records present only in the old JSON were retained. Its existing worm-stop check remains unresolved.
- 42129's separate training branch was merged. It has 409 steps and passes notation checks after two frictionless-pin mode corrections, but duplicate names and inventory differences still need review.

## Saving

Work in an isolated worktree when another task is using the shared checkout. Stage explicit task paths. Commit and push useful checkpoints, roughly every 20 transcribed steps. Merge current main before pushing; never force-push or overwrite another task's work. Preserve original booklets and back up reference material before removing anything obsolete.
