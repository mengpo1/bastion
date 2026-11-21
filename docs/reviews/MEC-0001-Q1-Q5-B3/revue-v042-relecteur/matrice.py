import re, sys
t = open(sys.argv[1], encoding="utf-8").read().split("\n")
def section(title_start, title_end):
    s = next(i for i,l in enumerate(t) if l.startswith(title_start))
    e = next(i for i,l in enumerate(t) if i > s and l.startswith(title_end))
    return s, e
s12, e12 = section("## 12.", "## 13.")
s13, e13 = section("## 13.", "## 14.")
def rows(s, e):
    out = []
    for i in range(s, e):
        l = t[i]
        if l.startswith("|") and not l.startswith("|---") and not l.startswith("| ID"):
            out.append((i+1, [c.strip() for c in l.strip("|").split("|")]))
    return out
def expand(src):
    ids = set()
    for a,b,c in re.findall(r"Q(\d)\.(\d+) à Q\d\.(\d+)", src):
        for k in range(int(b), int(c)+1): ids.add(f"Q{a}.{k}")
    for a,b in re.findall(r"Q(\d)\.(\d+)", src): ids.add(f"Q{a}.{b}")
    for m in re.findall(r"\b(?:M-0[45]|R-[5-8])=?[AB]?", src): ids.add(m.split("=")[0])
    if "W-01" in src: ids.add("W-01")
    if "B3" in src: ids.add("B3")
    return ids
scen = {}
for ln, c in rows(s13, e13):
    if len(c) >= 5 and re.match(r"T\d", c[0]): scen[c[0]] = (ln, c[3], c[4])
print("scenarios au par.13 :", len(scen), sorted(scen, key=lambda x:(int(re.sub(r'\D','',x)), x)))
probs = []; n = 0
for ln, c in rows(s12, e12):
    if len(c) < 8: continue
    did, sc = c[0], c[6]
    ts = re.findall(r"T\d+[ab]?", sc)
    key = did.split("=")[0]
    if key.startswith("Confirmation W-01"): key = "W-01"
    for tt in ts:
        n += 1
        if tt not in scen: probs.append((ln, did, tt, "scenario inexistant")); continue
        if did.startswith("PNV"): continue
        ids = expand(scen[tt][1])
        if key not in ids and not (key=="Rectificatif B3"):
            probs.append((ln, did, tt, "ne cite pas la decision : sources = " + scen[tt][1]))
print("rattachements examines :", n)
for p in probs: print("  l.%d %s -> %s : %s" % p)
# PNV : scenarios cites et statut
for ln, c in rows(s12, e12):
    if c[0].startswith("PNV"):
        for tt in re.findall(r"T\d+[ab]?", c[6]):
            print("  PNV ->", tt, "statut :", scen[tt][2])
# Scenarios Sp citant une PNV
for k,(ln,src,st) in scen.items():
    if st.startswith("Sp") and "PNV" in (src+st): print("  Sp avec PNV :", k, st)
