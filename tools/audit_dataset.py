"""Audit the hand-written training pairs and booklet coverage.

Run from the repository root: python tools/audit_dataset.py
Writes docs/dataset_status.csv. --strict exits nonzero if any set needs review.
Checker success is a notation check, not proof of mechanical correctness.
"""
import argparse
import collections
import csv
import json
from pathlib import Path
import re

import check_notation

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {
    "lightgray": "lightbluishgray", "darkgray": "darkbluishgray",
    "brown": "reddishbrown", "anycolor": "nocoloranycolor",
}
PARTIAL = {"42006", "42110", "42129"}


def color(value):
    value = re.sub(r"[^a-z0-9]", "", value.lower().replace("grey", "gray"))
    return ALIASES.get(value, value)


def audit(folder, header, system):
    row = {"set": folder.relative_to(ROOT / "sets").as_posix(),
           "steps": 0, "inventory_parts": 0, "training_parts": 0,
           "booklets": len(list(folder.glob("booklet*.pdf"))),
           "checker_errors": 0, "missing_parts": 0, "extra_parts": 0,
           "unknown_endpoints": 0, "estimated_endpoints": 0, "status": "not started", "notes": ""}
    stock = collections.Counter()
    with (folder / "parts_list.csv").open(encoding="utf-8-sig", newline="") as stream:
        for part in csv.DictReader(stream):
            stock[(part["part_number"], color(part["colour"]))] += int(part["qty"])
    row["inventory_parts"] = sum(stock.values())
    table, chat = folder / "training.tbl", folder / "training.jsonl"
    if not table.exists():
        if not row["booklets"]: row["notes"] = "Missing booklet"
        return row
    text = table.read_text(encoding="utf-8")
    chunks = re.split(r"^STEP (\d+)\n", text, flags=re.M)
    blocks = list(zip(chunks[1::2], chunks[2::2]))
    used = collections.Counter()
    names = set()
    notes = []
    try:
        records = [json.loads(line) for line in chat.read_text(encoding="utf-8").splitlines() if line.strip()]
        assert chunks[0] == header, "Header differs from 42175"
        assert len(records) == len(blocks), "JSONL/STEP count mismatch"
        assert [int(n) for n, _ in blocks] == list(range(1, len(blocks) + 1)), "Nonconsecutive STEP numbers"
        history = []
        for (n, block), record in zip(blocks, records):
            block = block.strip()
            assert record["step"] == n, "Step identifier mismatch"
            assert [m["role"] for m in record["messages"]] == ["system", "user", "assistant"], "Message schema differs"
            assert record["messages"][0]["content"] == system, "System prompt differs"
            assert record["messages"][2]["content"] == block, "Assistant/table mismatch"
            assert len(re.findall(r"^WHY ", block, re.M)) == 1, "Expected one WHY per step"
            assert all(old in record["messages"][1]["content"] for old in history[-4:]), "Previous four steps differ"
            history.append(f"STEP {n}\n{block}")
        assert not re.search(r"TO WRITE|PLACEHOLDER_REPLACED|^THINK ", text, re.M), "Obsolete placeholder/THINK content"
    except (AssertionError, ValueError, KeyError, OSError) as exc:
        notes.append(str(exc))
    for line in text.splitlines():
        if line.startswith("ADD "):
            _, name, part, shade = line.split()
            if name in names: notes.append(f"Duplicate name: {name}")
            names.add(name)
            used[(part, color(shade))] += 1
    row.update(steps=len(blocks), training_parts=sum(used.values()),
               missing_parts=sum((stock - used).values()), extra_parts=sum((used - stock).values()))
    parsed, critiques, unknown = check_notation.stage1(str(table))
    critiques += check_notation.stage2(str(table), parsed)
    row["checker_errors"] = sum(c["severity"] == "error" for c in critiques)
    row["unknown_endpoints"] = sum(v for k, v in unknown.items() if "(~)" not in k)
    row["estimated_endpoints"] = sum(v for k, v in unknown.items() if "(~)" in k)
    if folder.name in PARTIAL: notes.append("Incomplete training or unresolved main/optional-build inventory scope")
    if not row["booklets"]: notes.append("Missing booklet")
    if row["checker_errors"]: notes.append("Run check_notation.py for existing connection errors")
    if row["missing_parts"] or row["extra_parts"]: notes.append("Inventory differs by part and colour")
    row["status"] = "ready" if not notes else "needs review"
    row["notes"] = "; ".join(dict.fromkeys(notes))
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    template = ROOT / "sets/42175"
    header = (template / "training.tbl").read_text(encoding="utf-8").split("STEP 1\n")[0]
    system = json.loads((template / "training.jsonl").read_text(encoding="utf-8").splitlines()[0])["messages"][0]["content"]
    rows = [audit(p.parent, header, system) for p in sorted((ROOT / "sets").rglob("parts_list.csv"))]
    with (ROOT / "docs/dataset_status.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"sets": len(rows), "with_booklets": sum(bool(r["booklets"]) for r in rows),
                      "training_steps": sum(r["steps"] for r in rows),
                      "status": dict(collections.Counter(r["status"] for r in rows)),
                      "checker_errors": {r["set"]: r["checker_errors"] for r in rows if r["checker_errors"]}}, indent=2))
    if args.strict and any(r["status"] == "needs review" for r in rows):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
