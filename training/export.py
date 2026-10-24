"""Turns every set's steps.md into chat examples for fine-tuning Qwen.
Usage: python training/export.py            (every sets/<set>/steps.md)
Writes training/data/train.jsonl and training/data/test.jsonl (one whole set held out when there are 2+).
Also writes sets/<set>/training.jsonl and sets/<set>/training.tbl for each set (same examples, plain text).

One example per step: "here is the build so far, write step N" -> that step's ADD/CONNECT/WHY lines
(plus GROUP/END/ATTACH when the step opens, closes or attaches a side build).
Earlier steps are condensed (parts list + the last few steps in full) so each example fits the context."""
import glob, json, os, re

SYSTEM = open("training/system_prompt.md", encoding="utf-8").read().strip()
FULL_STEPS = 4          # how many previous steps are shown line by line
OUT = "training/data/"

STEP_RE = re.compile(r"^## Step (\S+) \(page (\S+)\)(.*)$")


def parse_steps_md(path):
    """Returns a list of {order, page, note, lines} in booklet order."""
    paragraphs = open(path, encoding="utf-8").read().split("\n\n")
    steps, pending_group = [], None
    for para in paragraphs:
        para = para.strip("\n")
        if not para.strip():
            continue
        first = para.splitlines()[0].strip()
        if first.startswith("GROUP "):
            pending_group = first
            continue
        if first == "END":
            if steps:
                steps[-1]["lines"].append("END")
            continue
        m = STEP_RE.match(first)
        if not m:
            continue  # the "# Set ... - Title" line
        order, page, note = m.groups()
        lines = para.splitlines()[1:]
        if pending_group:
            lines = [pending_group] + lines
            pending_group = None
        steps.append({"order": order, "page": page, "note": note.strip(" -"), "lines": lines})
    return steps


def condense(parts_so_far):
    """Collapse a long parts list down to counts per part number so the prompt stays short."""
    if len(parts_so_far) <= 60:
        return ", ".join(parts_so_far)
    counts = {}
    for p in parts_so_far:
        counts[p] = counts.get(p, 0) + 1
    return ", ".join(f"{k} x{v}" if v > 1 else k for k, v in counts.items())


def examples_for(set_dir):
    steps = parse_steps_md(set_dir + "steps.md")
    title = open(set_dir + "steps.md", encoding="utf-8").readline().strip("# \n")
    parts_so_far, history, out = [], [], []
    for s in steps:
        where = f"step {s['order']}" + (f" ({s['note']})" if s["note"] else "")
        context = [f"SET {title}",
                    "PARTS SO FAR " + (condense(parts_so_far) if parts_so_far else "none"),
                    "LAST STEPS"] + [l for h in history[-FULL_STEPS:] for l in h]
        prompt = "\n".join(context) + f"\n\nWrite {where} (page {s['page']})."
        answer = "\n".join(s["lines"])
        out.append({"set": title, "step": s["order"], "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": answer}]})
        for l in s["lines"]:
            if l.startswith("ADD "):
                t = l.split()
                parts_so_far.append(f"{t[1]} {t[2]}")
        history.append([f"STEP {where}"] + s["lines"])
    return out


def write_set_files(set_dir, examples):
    with open(set_dir + "training.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for e in examples:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    with open(set_dir + "training.tbl", "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join("# " + l for l in SYSTEM.splitlines()) + "\n")
        for e in examples:
            f.write(f"STEP {e['step']}\n")
            f.write(e["messages"][-1]["content"] + "\n")


if __name__ == "__main__":
    set_dirs = sorted(os.path.dirname(p) + "/" for p in glob.glob("sets/*/steps.md") + glob.glob("sets/*/*/steps.md"))
    by_set = {d: examples_for(d) for d in set_dirs}
    for d, examples in by_set.items():
        write_set_files(d, examples)

    os.makedirs(OUT, exist_ok=True)
    test_dir = set_dirs[-1] if len(set_dirs) > 1 else None
    with open(OUT + "train.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for d, examples in by_set.items():
            if d != test_dir:
                for e in examples:
                    f.write(json.dumps({"messages": e["messages"]}, ensure_ascii=False) + "\n")
    with open(OUT + "test.jsonl", "w", encoding="utf-8", newline="\n") as f:
        if test_dir:
            for e in by_set[test_dir]:
                f.write(json.dumps({"messages": e["messages"]}, ensure_ascii=False) + "\n")
    print(f"{len(set_dirs)} sets, held out for test: {test_dir or 'none'}")
    for d, examples in by_set.items():
        print(f"  {d}: {len(examples)} steps")
