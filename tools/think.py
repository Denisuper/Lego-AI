# Writes the THINK lines that come before each step's moves in the build language.
# Same content as preview.md, in full sentences:
# have -> goal -> parts (position) -> touches -> does -> need (mechanism rule) -> why -> role (big picture)
# -> check (each join) -> builds on -> result (motion / state) -> later.
import json

LIB = {m["type"]: m for m in json.load(open("catalog/mechanisms.json", encoding="utf-8"))["mechanisms"]}


def clean(s):
    return " ".join(str(s).split())


def think(e, info):
    a, y = e["answer"], e["answer"]["why"]
    out = ["THINK have " + clean(e["input"]["model_so_far"])]
    out.append("THINK goal " + clean(y["problem_solved"]))
    for p in a["new_parts"]:
        if p["name"].startswith("tread-") and p["name"] not in ("tread-1", "tread-29"):
            continue
        out.append("THINK part %s (%s %s): %s; %s" % (p["name"], p["part_number"], p["catalog_name"], clean(p["position"]), clean(p["rotation"])))
    for t in a["what_each_new_part_touches"]:
        out.append("THINK touches " + clean(t))
    for t in a["who_does_what_to_which"]:
        out.append("THINK does " + clean(t))
    for t in dict.fromkeys(x["type"] for x in info["advances"]):
        lib = LIB.get(t)
        if lib:
            out.append("THINK need %s: %s Rules: %s" % (t, clean(lib["does"]), " ".join(lib["rules"])))
    out.append("THINK why " + clean(y["why_these_parts"]))
    for b in a["big_picture"]:
        if b["role"] and not (b["part"].startswith("tread-") and b["part"] not in ("tread-1", "tread-29")):
            out.append("THINK role %s in the %s: %s" % (b["part"], (b["system"] or "").lower(), clean(b["role"])))
    for j in a["joins"]:
        if j["part"].startswith("tread-") and j["part"] not in ("tread-1", "tread-28", "tread-29", "tread-56"):
            continue
        if j["named"] and j["fit"]:
            out.append("THINK check %s.%s goes into %s.%s, %g hole deep, %s%s" % (
                j["part"], j["point"], j["into"], j["into_point"], j["depth_holes"], j["fit"], "" if j["exact"] else " (estimated from the picture)"))
        else:
            out.append("THINK check %s.%s goes into %s.%s (not shown in the booklet)" % (j["part"], j["point"], j["into"], j["into_point"]))
    for bo in info["builds_on"]:
        if bo["part"].startswith("tread-") and bo["part"] not in ("tread-1", "tread-29"):
            continue
        for x in bo["builds_on"]:
            s = "THINK builds_on %s builds on %s (%s)" % (bo["part"], x["joins"], x["added_in"])
            if x["that_part_is"]:
                s += ", which is the " + clean(x["that_part_is"][0])
            if x["which_rests_on"]:
                s += ", and rests on " + ", ".join("%s (%s)" % (w["part"], w["added_in"]) for w in x["which_rests_on"])
            out.append(s)
    for x in info["advances"]:
        flag = " (not confirmed)" if x["status"] == "hypothesis" else ""
        out.append("THINK mechanism %s becomes the %s of the %s%s" % (x["part"], clean(x["role"]), x["name"].lower(), flag))
    for s_ in info["state"]:
        left = "complete" if s_["complete"] else "still missing " + ", ".join(s_["still_missing"])
        out.append("THINK state %s has %d of %d parts, %s" % (s_["mechanism"], s_["parts_present"], s_["parts_total"], left))
    for mo in info["motion"]:
        out.append("THINK result " + clean(mo["says"]))
    out.append("THINK later " + clean(y["sets_up_for_later"]) + " Pattern: " + clean(y["design_pattern"]))
    return out
