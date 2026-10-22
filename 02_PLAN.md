# Lego AI: Build Plan

Live version: https://claude.ai/artifact/3UqS1JRTkBuiq9jE5KFjfm

## Goal
Build a brand-new AI made only for Technic. We invent a simple build language that writes a LEGO model as exact moves ("put this part into that hole"), translate real booklets into it, and train the new AI on that language. It then designs its own working Technic builds, and every design comes with what each part does and why.

## Where we are (Oct 22, 2026)
| Item | Status |
| --- | --- |
| Steps labeled | 14 of ~150 (set 8047, pages 3-6), read from the pictures, with the why |
| Confidence | 11 high, 3 medium |
| Needs review | 3, 8, 12 |
| Part numbers | 34/34 confirmed |
| Step pictures | Saved, one per step |
| Positions | Words only, no 3D coordinates yet |

## Next steps
- [ ] Write the build language rules and connection points for set 8047's parts
- [ ] Rewrite steps 1-14 in the build language
- [ ] Check whether set 8047 is in the LDraw library of official sets
- [ ] Clear steps 3, 8, 12
- [ ] Label step 15 onward

## 6-week build plan
1. Week 1 - language + checker + converter for LPub3D. Target: steps 1-14 in the language, passing the checker.
2. Week 2 - translate booklets (Claude writes moves + why; LDraw files where they exist). Target: 3 full sets passing.
3. Week 3 - scale + generator. Target: 1,000+ real steps, 100,000+ generated builds.
4. Week 4 - stage 1, learn the language from scratch. Target: 90%+ of finished builds pass.
5. Week 5 - stage 2, design on request. Target: half of designs pass.
6. Week 6 - stage 3, GRPO. Target: 80% pass on 20 new requests, each printed as a booklet.

## The build language
| Word | Meaning | Example |
| --- | --- | --- |
| STEP | starts a step | STEP 14 |
| ADD | new part: name, part number, color | ADD gear-1 4019 lightgray |
| CONNECT | exact join, point to point | CONNECT gear-1.axlehole -> tan-1.axle |
| ANGLE | turn around a joint, only if needed | ANGLE bentbeam-D 90 |
| MESH | gears touching | MESH gear-A.teeth gear-B.teeth |
| GROUP / ATTACH | side mini build, attached as one | GROUP side-1 ... END; ATTACH side-1 rod-A.pin |
| DOES | function, six verbs | DOES tan-1 CARRIES gear-1 |
| RATIO | driver teeth / driven teeth | RATIO gear-A gear-B 20/12 |
| PATTERN | design idea | PATTERN gears_as_track_wheels |
| REQUEST | what a design should do | REQUEST turn_platform INPUT knob MAXPARTS 150 |

Example, steps 13-14 of set 8047:
```
STEP 13
ADD tan-1 3749 tan
CONNECT tan-1.pin -> beam9-X.hole1
DOES tan-1 SPINS_ON beam9-X
PATTERN free_spinning_axle
STEP 14
ADD gear-1 4019 lightgray
CONNECT gear-1.axlehole -> tan-1.axle
DOES tan-1 CARRIES gear-1
PATTERN gears_as_track_wheels
```
Translating: Claude writes the moves + why from each picture; LDraw files of official sets give exact joins where they exist; the checker draws it in 3D and compares. A generator adds millions of small random mechanisms that pass the checker.

## How we train it
A small transformer built from scratch, trained only on the build language (10-50 million settings to start).
| Stage | Method | Plain words | Score |
| --- | --- | --- | --- |
| 1. Learn the language | Next-move prediction, from scratch | Reads millions of builds and keeps guessing the next line | Next-move accuracy on unseen builds |
| 2. Design on request | Supervised fine-tuning on request cards | REQUEST line in, whole build out | Share passing the checker |
| 3. Get good | GRPO | ~8 designs per request, checker scores each, nudged toward the better ones | Share passing every check on unseen requests |
Software: PyTorch + a small GPT-style setup (nanoGPT) for stages 1-2; Hugging Face TRL GRPO for stage 3.
Designs carry DOES and PATTERN lines; Claude turns them into plain English.

## Making the instruction booklets
The AI doesn't draw. It writes the build in the build language; software draws every picture from the exact 3D model.
1. AI writes the build, step by step.
2. Converter turns ADD/CONNECT into an LDraw 3D file, with a step marker at each STEP.
3. LPub3D (free) turns that into a LEGO-style booklet: picture per step, parts box, side boxes for each GROUP, page numbers.
4. Output: PDF booklet plus a page with the why for each step.
The same drawing step lets the checker compare translated steps with the real booklet pictures.

## What it learns from
See 03_training_data/8047_preview.md: every step with its picture and explanation.
