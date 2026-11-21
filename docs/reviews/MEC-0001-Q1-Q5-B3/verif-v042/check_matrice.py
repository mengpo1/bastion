import sys, re
v = open(sys.argv[1], encoding="utf-8").read()
def sec(a, b): return v[v.index(a):v.index(b)]
m = sec("## 12. Matrice", "## 13. Scénarios"); sc = sec("## 13. Scénarios", "**Sort des cas")
rows = lambda s: [ [c.strip() for c in l.strip().strip("|").split("|")] for l in s.splitlines() if l.startswith("| ") and not l.startswith("| ID") and not l.startswith("| ---")]
S = {}
for r in rows(sc):
    if re.match(r"T\d", r[0]): S[r[0]] = r
def expand(src):
    toks = set()
    for a, b, c in re.findall(r"Q(\d)\.(\d+) à Q\1\.(\d+)", src):
        for k in range(int(b), int(c) + 1): toks.add(f"Q{a}.{k}")
    for x in re.findall(r"Q\d\.\d+", src): toks.add(x)
    for x in re.findall(r"\b(?:[A-Z]{1,3}\d?-?\d+(?:=[AB])?|W-\d\d|B3|S\d+|Z1|N\d+)\b", src): toks.add(x)
    return toks
bad = 0; n = 0
for r in rows(m):
    if len(r) < 7: continue
    did = r[0].replace("Confirmation ", "")
    if did.startswith("PNV"): continue
    for t in re.findall(r"T\d+[ab]?", r[6]):
        if "aucun" in r[6] and "vérifie la règle" in r[6]: continue
        key = t if t in S else t.rstrip("ab")
        if key not in S: print("scénario inconnu", did, t); bad += 1; continue
        n += 1
        if did not in expand(S[key][3]):
            print("NON CITÉ :", did, "->", t, "| sources :", S[key][3][:80]); bad += 1
print("rattachements contrôlés :", n, "; non cités :", bad)
# PNV dans un scénario Sp ?
for k, r in S.items():
    st = r[4]
    if st.startswith("Sp") and "PNV" in " ".join(r): print("PNV dans un Sp :", k)
sys.exit(1 if bad else 0)
