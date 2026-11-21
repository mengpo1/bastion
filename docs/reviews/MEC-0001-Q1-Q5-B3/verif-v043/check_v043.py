import sys, re, hashlib, os
v = open(sys.argv[1], encoding="utf-8").read(); SP = sys.argv[2]
L = v.splitlines()
def row(prefix):
    r = [l for l in L if l.startswith(prefix)]; assert len(r) == 1, (prefix, len(r)); return r[0]
def sec(a, b): return v[v.index(a):v.index(b)]
ok = True
def t(nom, cond):
    global ok; ok &= bool(cond); print(("OK    " if cond else "ECHEC ") + nom)
t("AN-01 T04 porte ⟨B3-03⟩", "⟨B3-03⟩" in row("| T04 |"))
s0 = sec("## 0. Provenance", "## 1. Périmètre")
t("AN-02 tableau des identifiants JS-22 à JS-38", all(("| JS-%d" % n) in s0 or ("JS-%d à" % n) in s0 or ("à JS-%d" % n) in s0 for n in (22,23,24,28,29,30,31,32,34,35,36,37,38)))
s01 = sec("### 0.1 ", "## 1. Périmètre")
t("AN-02 plus de « message 1 / message 2 » nus au §0.1", not re.search(r"(?<!« )\bmessage [12]\b", s01))
t("AN-02 JS-31 et JS-35 au §0.1", "JS-31" in s01 and "JS-35" in s01)
r47 = row("| T47 |")
t("AN-03 T47 (b) atteignable", "12 TU et 100 d'énergie à la sélection" in r47 and "5 TU et 98 d'énergie avant ce pas" not in r47 and "il reste 2 TU et 95 d'énergie" in r47)
for q in ("« toutes les données géométriques »", "« concordance de troncature »", "« dans sa case »"):
    t("AN-04 absence de " + q, q not in v)
t("AN-04 (a) D:30 cité", "« Unités physiques de géométrie : mm entiers »" in row("| PNV-2 |"))
t("AN-04 (b) citation exacte", "« Concordance d'ordre et de troncature »" in row("| M-15 |"))
t("AN-04 (c) T26", "« le profil ne dépasse pas sa case »" in row("| T26 |"))
t("AN-05 W-11 (a)", "T45 retiré en v0.4.2" in row("| W-11 (a) |"))
for k in ("| T03 |", "| T42 |", "| T43 |", "| T46 |"):
    t("AN-06 %s rattaché à R:134" % k, "R:134" in row(k) and "PNV-6" not in row(k).split("|")[-2])
t("AN-06 ligne PNV du §12", "| T04, T15, T26 (conditionnels) |" in row("| PNV-1 à PNV-9 |"))
s10 = sec("## 10. ", "## 11. ")
t("AN-07 R:166", not [l for l in s10.splitlines() if l.startswith("| R:166") and l.rstrip().endswith("| — |")])
t("AN-07 G3", not [l for l in s10.splitlines() if l.startswith("| G3,") and l.rstrip().endswith("| — |")])
s15 = sec("## 15. ", "## 16. ")
scripts = ["verif-v04/extract.py", "verif-v04/last_user.py", "verif-v04/make_v041.py", "verif-v04/check_labels.py", "verif-v04/calculs.py",
           "verif-v042/make_v042.py", "verif-v042/check_textes.py", "verif-v042/check_matrice.py", "verif-v042/calculs_v042.py",
           "verif-v043/check_v043.py", "verif-v043/citations_v043.py", "verif-v043/calculs_v043.py"]
for s in scripts:
    h = hashlib.sha256(open(os.path.join(SP, s), "rb").read()).hexdigest()
    t("AN-08 script inventorié avec son empreinte : " + s, s in s15 and h in s15)
t("AN-08 JS-29 inventorié (14 bis)", "| 14 bis |" in s15 and "JS-29" in s15)
t("AN-08 concordance fortuite de JS-22 expliquée", "concordance fortuite" in sec("## 17. ", "## 18. "))
t("OB-01", "[INS] (R:124)" in sec("## 5. ", "## 6. "))
t("OB-02", "[DÉD]" in [l for l in sec("## 6. ", "## 7. ").splitlines() if "R:166" in l][0])
t("OB-03", "au millimètre le plus proche, ou inférieur" in row("| T48 |"))
t("OB-04", "R-8=A (« articulation validée »)" in sec("## 2 bis.", "## 3. Géométrie"))
t("OB-05", "**Portée de [TR] et [TR-M]**" in s0)
t("OB-06", "prepareEnergy" in sec("## 5. ", "## 6. ") and "N14" in sec("### 9.2", "## 10. "))
t("OB-07", "| Q1.1 à Q1.3, Q1.5 à Q1.7, Q2.5, Q2.6 |" in row("| T26 |"))
t("Phrase finale", v.rstrip().endswith("MEC-0001 et MEC-0002 restent reportées.") and "**La v0.4.3 n'est pas déclarée conforme**" in v)
print("TOUS_OK", ok); sys.exit(0 if ok else 1)
