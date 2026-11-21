import sys, re
v = open(sys.argv[1], encoding="utf-8").read()
def sec(a, b): return v[v.index(a):v.index(b)]
m = sec("## 12. Matrice", "## 13. Scénarios"); sc = sec("## 13. Scénarios", "**Sort des cas")
def rows(s):
    return [[c.strip() for c in l.strip().strip("|").split("|")] for l in s.splitlines()
            if l.startswith("| ") and not l.startswith("| ID") and not l.startswith("|---")]
scen = {r[0]: r for r in rows(sc) if re.match(r"T\d", r[0])}
def expand(src):
    ids = set()
    for a, b in re.findall(r"(Q\d\.\d+)\s+à\s+(Q\d\.\d+)", src):
        qa, na = a[1], int(a.split(".")[1]); qb, nb = b[1], int(b.split(".")[1])
        if qa == qb:
            for k in range(na, nb + 1): ids.add("Q%s.%d" % (qa, k))
        else:
            ids.add(a); ids.add(b)
    for t in re.findall(r"[A-Z][A-Z0-9]*(?:-[0-9A-Z]+)?(?:\.\d+)?(?:=[AB])?", src):
        ids.add(t); ids.add(t.split("=")[0])
    return ids
n = 0; bad = []
pnv_dep = []
for r in rows(m):
    rid, scen_col = r[0], r[6]
    if rid.startswith("PNV"): continue
    for t in re.findall(r"T\d+[ab]?", scen_col):
        n += 1
        s = scen.get(t)
        if not s: bad.append((rid, t, "scenario absent")); continue
        key = rid.split()[0]
        ids = expand(s[3])
        aliases = {"Confirmation": "W-01", "Rectificatif": "Rectificatif"}
        k = aliases.get(key, key)
        if k not in ids and not (k == "Rectificatif" and "rectificatif" in s[3].lower()):
            bad.append((rid, t, s[3]))
print("rattachements controles :", n)
for b in bad: print("NON CITE :", b)
# Scenarios dont la colonne statut mentionne une PNV (hors negation)
for t, s in scen.items():
    st = s[4]
    pn = re.findall(r"(\*\*pas\*\* )?PNV-\d", st)
    pos = [p for p in re.findall(r"(?:\*\*pas\*\* )?PNV-\d", st) if not p.startswith("**pas**")]
    if pos: pnv_dep.append((t, pos, st.split()[0]))
    if "PNV" in s[1] or "PNV" in s[2]: print("PNV hors statut :", t)
print("scenarios dependant d'une PNV :", pnv_dep)
print("scenarios 'Sp' avec PNV :", [t for t, p, st in pnv_dep if st.startswith("Sp")])
row_pnv = [r for r in rows(m) if r[0].startswith("PNV")][0]
print("ligne PNV du §12 :", row_pnv[6])
