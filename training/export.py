"""Turns every labeled set into chat examples for fine-tuning Qwen.
Usage: python training/export.py            (all sets under sets/)
Writes training/data/train.jsonl and training/data/test.jsonl (one set held out for testing when there are 2+ sets).

Two kinds of example:
  build   "Here is the build so far, write step N"  ->  THINK lines, then the moves, then MECH/STATE/MOTION lines
  motion  "Here is the build so far, what turns when you turn <knob>?"  ->  the MOTION line and a plain sentence
Earlier steps are condensed (parts list + the last few steps in full) so each example fits the context."""
import csv, glob, json, os, random, re, sys
sys.path.insert(0, "tools")
from mechanisms import Tracker

SYSTEM = (open("training/system_prompt.md", encoding="utf-8").read().strip())
FULL_STEPS = 4          # how many previous steps are shown line by line
OUT = "training/data/"


def clean(notation):
    """Drop people-notes (#) and blank lines."""
    out = []
    for l in notation.split("\n"):
        l = l.split("#")[0].rstrip()
        if l.strip(): out.append(l)
    return out


def condense(lines):
    """Collapse runs of identical-pattern lines (track links) into one line."""
    out, run = [], []
    def flush():
        if len(run) > 3:
            out.append(f"{run[0]}  ... ({len(run)} lines like this) ...  {run[-1]}")
        else:
            out.extend(run)
        run.clear()
    for l in lines:
        key = re.sub(r"\d+", "N", l)
        if run and re.sub(r"\d+", "N", run[-1]) == key: run.append(l)
        else:
            flush(); run.append(l)
    flush()
    return out


def examples_for(set_dir):
    d = set_dir.rstrip("/") + "/"
    rows = list(csv.DictReader(open(d + "booklet_map.csv")))
    ann = {json.loads(l)["example_id"]: json.loads(l) for l in open(d + "training.jsonl", encoding="utf-8")}
    order = [json.loads(l)["example_id"] for l in open(d + "training.jsonl", encoding="utf-8")]
    tracker = Tracker(d)
    set_name = ann[order[0]]["set"]
    parts_so_far, history, out = [], [], []
    for r, eid in zip(rows, order):
        e = ann[eid]
        notation = clean(open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read())
        info = tracker.step(eid, open(f"{d}steps/{r['folder']}/notation.tbl", encoding="utf-8").read())
        mech = tracker.lines(info)
        where = f"main step {e['step']}" if r["build"] == "main" else f"{r['build']} side build, step {e['step']} (attaches at main step {r['attaches_at_main_step']})"
        context = [f"SET {set_name}",
                   "PARTS SO FAR " + (", ".join(parts_so_far) if parts_so_far else "none"),
                   "LAST STEPS"] + [l for h in history[-FULL_STEPS:] for l in h]
        prompt = "\n".join(context) + f"\n\nWrite {where}. Think first (THINK lines), then the moves, then the mechanism lines."
        answer = "\n".join(e["answer"]["think"] + condense(notation) + mech)
        out.append({"kind": "build", "set": set_name, "id": eid, "messages": [
            {"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}, {"role": "assistant", "content": answer}]})
        for mo in info["motion"]:
            m = next(x for x in tracker.mechs if x["id"] == mo["mechanism"])
            if "ERROR" in m["does"]: continue  # known jam: don't teach it
            sure = {c["part"] for c in m["chain"] if c.get("status", "confirmed") == "confirmed"}
            mo = dict(mo, per_input_turn={p: v for p, v in mo["per_input_turn"].items() if p in sure})
            if not mo["per_input_turn"]: continue  # nothing confirmed to teach
            mo["says"] = f"Turn {mo['input']} once: " + ", ".join(f"{p} turns {v.lstrip('-')} {'turn' if v.lstrip('-') == '1' else 'turns'}{' the other way' if v.startswith('-') else ''}" for p, v in mo["per_input_turn"].items())
            q = "\n".join(context + [l for l in notation]) + f"\n\nTURN {mo['input']}. What turns, how far and which way?"
            a = "MOTION " + mo["input"] + " " + " ".join(f"{p}={v}" for p, v in mo["per_input_turn"].items()) + "\n" + mo["says"]
            out.append({"kind": "motion", "set": set_name, "id": eid, "messages": [
                {"role": "system", "content": SYSTEM}, {"role": "user", "content": q}, {"role": "assistant", "content": a}]})
        for l in notation:
            t = l.split()
            if t[:1] == ["ADD"]: parts_so_far.append(f"{t[1]} {t[2]}")
        parts_so_far[:] = condense(parts_so_far) if len(parts_so_far) > 400 else parts_so_far
        history.append([f"STEP {where}"] + condense(notation))
    return out


if __name__ == "__main__":
    sets = sorted(glob.glob("sets/*/"))
    by_set = {s: examples_for(s) for s in sets}
    os.makedirs(OUT, exist_ok=True)
    test_set = sets[-1] if len(sets) > 1 else None  # hold out a whole set, never single steps
    with open(OUT + "train.jsonl", "w", encoding="utf-8", newline="\n") as tr, open(OUT + "test.jsonl", "w", encoding="utf-8", newline="\n") as te:
        for s, exs in by_set.items():
            for x in exs:
                (te if s == test_set else tr).write(json.dumps(x, ensure_ascii=False) + "\n")
    n = {k: sum(1 for s in by_set.values() for x in s if x["kind"] == k) for k in ("build", "motion")}
    print(f"{len(sets)} set(s): {n['build']} build + {n['motion']} motion examples -> {OUT}"
          + (f" (test set: {test_set})" if test_set else " (only one set: no test split yet)"))
