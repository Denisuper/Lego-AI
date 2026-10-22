# Lego AI - Technic training data

Real LEGO Technic instruction booklets turned into training data: for every step, the picture, a labeled annotation (parts, joins, what each part does and why) and the same step in our build language. A small AI is trained on the build language to design its own Technic builds.

## Layout
| Path | What it is |
| --- | --- |
| `sets/<set>/` | One folder per instruction booklet |
| `sets/<set>/steps/<build>-NN/` | One folder per step: `picture.png`, `annotation.json`, `notation.tbl` |
| `sets/<set>/booklet_map.csv` | Every step in booklet order, with page and where each side build attaches |
| `sets/<set>/booklet.pdf`, `parts_list.csv` | The booklet and its official parts list |
| `sets/<set>/training.jsonl`, `training.tbl` | The whole set in one file each, ready for training (generated) |
| `sets/<set>/preview.md` | Every step with its picture, easy to read (generated) |
| `catalog/technic_parts.csv` | Every Technic part: number, name, category, colors, which labeled sets use it |
| `docs/` | Labeling instructions, framework |
| `tools/build_set.py` | Rebuilds a set's generated files from its step folders |
| `tools/check_steps.py` | Checks parts, counts, verbs, names, "why" fields |

## Rebuild and check a set
```
python tools/build_set.py sets/8047
python tools/check_steps.py sets/8047/training.jsonl sets/8047/parts_list.csv
```

## Status (Oct 22, 2026)
| Set | Steps | Notes |
| --- | --- | --- |
| 8047 Compact Excavator | 88 (main 1-56 + seat, body, arm, boom side builds) | All 252 pieces used exactly once; checks pass; 47 steps flagged for review |

Catalog: 975 Technic parts from Rebrickable's free data downloads.
