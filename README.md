# Lego AI

Training data for an AI that designs LEGO Technic builds. Read [CLAUDE.md](CLAUDE.md) for the build language and editing rules.

Each set has its booklet PDF and parts list. Transcribed sets also have `training.tbl` and matching chat-format `training.jsonl`. Official sets and fan MOCs are kept separate under `sets/`, `sets/differentials/` and `sets/gearboxes/`.

Booklets use Git LFS so the originals can stay unchanged, including files larger than GitHub's normal limit:

```sh
git lfs install
git lfs pull
python tools/audit_dataset.py
```

See [dataset_status.csv](docs/dataset_status.csv) for all sets, booklet coverage, step counts, inventory differences and checker errors. “Ready” means the automated checks passed; it does not prove full mechanical motion. [booklets.csv](docs/booklets.csv) records PDF page counts, hashes and available source information.

To combine the ready sets for training:

```sh
python training/pack_data.py
```

This holds out one whole set and writes ignored files under `training/data/`. It does not rewrite any set's training files. The current trainer consumes text messages; PDF page images are not yet wired into training.

See [cleanup.md](docs/cleanup.md) for the merge and cleanup notes, including unresolved legacy data issues.
