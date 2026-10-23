"""Downloads what a set needs: official 3D model (LDraw OMR), parts list (Rebrickable, spares left out), booklet PDFs (LEGO).
Usage: python tools/get_set.py <set number> <rebrickable dir or ->   ("-" = skip the parts list, only booklets + 3D model)
<rebrickable dir> holds parts.csv, colors.csv, inventories.csv, inventory_parts.csv from cdn.rebrickable.com/media/downloads/.
Writes sets/<set>/model.mpd (if one exists), sets/<set>/parts_list.csv, sets/<set>/booklet*.pdf."""
import csv, os, re, sys, urllib.request

SET, RB = sys.argv[1], sys.argv[2].rstrip("/") + "/"
OUT = f"sets/{SET}/"
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


# parts list
if RB != "-/":
    inv = next((r["id"] for r in csv.DictReader(open(RB + "inventories.csv", encoding="utf-8")) if r["set_num"] == SET + "-1"), None)
    names = {r["part_num"]: r["name"] for r in csv.DictReader(open(RB + "parts.csv", encoding="utf-8"))}
    colors = {r["id"]: r["name"] for r in csv.DictReader(open(RB + "colors.csv", encoding="utf-8"))}
    rows = [r for r in csv.DictReader(open(RB + "inventory_parts.csv", encoding="utf-8")) if r["inventory_id"] == inv and r["is_spare"] in ("f", "False", "0")]
    with open(OUT + "parts_list.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["qty", "part_number", "colour", "name"])
        for r in rows:
            w.writerow([r["quantity"], r["part_num"], colors.get(r["color_id"], r["color_id"]), names.get(r["part_num"], "")])
    print(f"parts list: {sum(int(r['quantity']) for r in rows)} pieces, {len(rows)} lines")

# booklet PDFs (main booklets only, not the alternate-model extras)
page = get(f"https://www.lego.com/en-us/service/buildinginstructions/{SET}").decode("utf-8", "ignore")
pdfs = sorted(set(re.findall(r"https://www.lego.com/cdn/product-assets/product\.bi\.core\.pdf/\d+\.pdf", page)))
for i, u in enumerate(pdfs, 1):
    open(OUT + (f"booklet{i}.pdf" if len(pdfs) > 1 else "booklet.pdf"), "wb").write(get(u))
print(f"booklets: {len(pdfs)}")

# official 3D model
listing = ""
for p in range(1, 120):
    html = get(f"https://library.ldraw.org/omr/sets?page={p}").decode("utf-8", "ignore")
    if f">{SET}-1<" in html:
        i = html.index(f">{SET}-1<")
        sid = re.findall(r"/omr/sets/(\d+)", html[max(0, i - 3000):i])[-1]
        listing = get(f"https://library.ldraw.org/omr/sets/{sid}").decode("utf-8", "ignore")
        break
models = re.findall(r"https://library\.ldraw\.org/media/omr_models/\d+/[^\"?]+\.mpd", listing)
main = [m for m in models if re.search(rf"/{SET}-1\.mpd$", m)] or models[:1]
if main:
    open(OUT + "model.mpd", "wb").write(get(main[0]))
    print("3D model:", main[0].rsplit("/", 1)[-1])
else:
    print("3D model: none in the OMR")
