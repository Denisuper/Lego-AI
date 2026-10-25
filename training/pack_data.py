"""Combine audited training JSONL without rewriting the source set files.

Run tools/audit_dataset.py first. Only sets marked ready are included.
One whole set is held out, keeping its steps out of the training split.
"""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--holdout", help="Set folder relative to sets/; defaults to the last ready set")
    args = parser.parse_args()
    report = ROOT / "docs/dataset_status.csv"
    if not report.exists():
        parser.error("Run python tools/audit_dataset.py first")
    with report.open(encoding="utf-8", newline="") as stream:
        sets = [r["set"] for r in csv.DictReader(stream) if r["status"] == "ready"]
    if not sets:
        parser.error("No ready sets in the audit")
    holdout = args.holdout or (sets[-1] if len(sets) > 1 else None)
    if holdout and holdout not in sets:
        parser.error("Holdout must be a ready set")
    output = ROOT / "training/data"
    output.mkdir(exist_ok=True)
    counts = {"train": 0, "test": 0}
    with (output / "train.jsonl").open("w", encoding="utf-8", newline="\n") as train, (output / "test.jsonl").open("w", encoding="utf-8", newline="\n") as test:
        for name in sets:
            split = "test" if name == holdout else "train"
            target = test if split == "test" else train
            for line in (ROOT / "sets" / name / "training.jsonl").read_text(encoding="utf-8").splitlines():
                if line.strip():
                    json.loads(line)
                    target.write(line + "\n")
                    counts[split] += 1
    print(json.dumps({"sets": len(sets), "holdout": holdout, **counts}, indent=2))


if __name__ == "__main__":
    main()
