# Writes the THINK lines that come before each step's moves in the build language.
# Order: have (earlier parts this step builds on) -> goal -> need (mechanism rule) -> choose (parts and why)
#        -> check (each join and how it moves) -> result (motion or what it sets up).
import json

LIB = {m["type"]: m for m in json.load(open("catalog/mechanisms.json", encoding="utf-8"))["mechanisms"]}


def short(s, n=14):
    return " ".join(str(s).split()[:n]).rstrip(".,;")


def think(e, info):
    a = e["answer"]
    out = []
    for bo in info["builds_on"]:
        for x in bo["builds_on"][:2]:
            role = short(x["that_part_is"][0], 10) if x["that_part_is"] else "already in the model"
            out.append("THINK have %s (%s): %s" % (x["joins"], x["added_in"].split("-", 1)[1], role))
    out = list(dict.fromkeys(out))[:4]
    out.append("THINK goal " + short(a["why"]["problem_solved"], 18))
    for t in dict.fromkeys(x["type"] for x in info["advances"]):
        lib = LIB.get(t)
        if lib and lib["rules"]:
            out.append("THINK need %s: %s" % (t, short(lib["rules"][0], 18)))
    parts = list(dict.fromkeys("%s %s" % (p["name"], p["part_number"]) for p in a["new_parts"]))
    if parts:
        listed = ", ".join(parts[:4]) + (" and %d more" % (len(parts) - 4) if len(parts) > 4 else "")
        out.append("THINK choose %s because %s" % (listed, short(a["why"]["why_these_parts"], 16)))
    for j in a["joins"][:4]:
        if j["named"] and j["fit"]:
            out.append("THINK check %s.%s in %s.%s: %s" % (j["part"], j["point"], j["into"], j["into_point"], j["fit"]))
    for x in info["advances"]:
        if x["status"] == "hypothesis":
            out.append("THINK unsure %s role in %s not confirmed" % (x["part"], x["mechanism"]))
    if info["motion"]:
        out.append("THINK result " + short(info["motion"][0]["says"], 22))
    else:
        out.append("THINK result " + short(a["why"]["sets_up_for_later"], 18))
    return out
