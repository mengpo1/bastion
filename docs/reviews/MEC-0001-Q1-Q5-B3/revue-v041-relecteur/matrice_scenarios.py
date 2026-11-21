import re, sys
doc = open(sys.argv[1], encoding="utf-8").read().split("\n")
def rows(start, end):
    s = next(i for i, l in enumerate(doc) if l.startswith(start))
    e = next(i for i, l in enumerate(doc) if i > s and l.startswith(end))
    return [(i + 1, [c.strip() for c in doc[i].strip().strip("|").split("|")]) for i in range(s, e) if doc[i].startswith("| ") and not doc[i].startswith("|---")]
m12 = rows("## 12.", "## 13.")
s13 = rows("## 13.", "**Sort des cas")
scen = {}
for ln, c in s13:
    if re.match(r"T\d+[ab]?$", c[0]): scen[c[0]] = (ln, c)
def expand_ids(txt):
    ids = set()
    for a, b in re.findall(r"(Q\d\.\d+) à (Q\d\.\d+)", txt):
        p = a.split(".")[0]
        if p == b.split(".")[0]:
            for k in range(int(a.split(".")[1]), int(b.split(".")[1]) + 1): ids.add(f"{p}.{k}")
    ids |= set(re.findall(r"Q\d\.\d+", txt))
    ids |= set(re.findall(r"\b(?:ARB-[A-E]|G[1-4]|S\d+|Z1|N\d+|GE-\d+|CH-\d+|ES-\d+|W-01)\b", txt))
    return ids
probs = []
for ln, c in m12:
    if len(c) < 7 or not re.match(r"Q\d|B3|Rect|Conf|PNV", c[0]): continue
    did = c[0]
    for t in re.findall(r"T\d+[ab]?", c[6]):
        if t not in scen: probs.append((ln, did, t, "scenario inexistant")); continue
        srcs = expand_ids(scen[t][1][3])
        key = did if did.startswith("Q") else None
        if key and key not in srcs:
            probs.append((ln, did, t, "sources de " + t + " : " + scen[t][1][3]))
print("anomalies de rattachement :", len(probs))
for p in probs: print("  §12 l.%d %s -> %s : %s" % p)
# statuts Sp contenant une PNV dans les sources ou le statut
for t, (ln, c) in scen.items():
    if "PNV" in " ".join(c) and c[4].startswith("Sp"):
        print("  PNV dans un Sp :", t, c[4])
print("statuts :", {t: c[4].split(" ")[0] for t, (ln, c) in scen.items()})
