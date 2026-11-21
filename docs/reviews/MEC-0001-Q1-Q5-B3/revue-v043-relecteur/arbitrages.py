import sys, re
v3 = open(sys.argv[1], encoding="utf-8").read(); v2 = open(sys.argv[2], encoding="utf-8").read()
p6 = open(sys.argv[3], encoding="utf-8").read().splitlines()
diff = open(sys.argv[4], encoding="utf-8").read().splitlines()
arb = {"M-04=B": (32, 42), "M-05=A": (45, 56), "R-5=A": (59, 70), "R-6=A": (73, 82), "R-7=A": (85, 93), "R-8=A": (96, 107)}
s2b3 = v3[v3.index("## 2 bis."):v3.index("## 3. Géométrie")]
s2b2 = v2[v2.index("## 2 bis."):v2.index("## 3. Géométrie")]
for k, (lt, ls) in arb.items():
    texte = p6[lt-1].strip().strip("«»").strip()
    statut = p6[ls-1].replace("Statut :", "").strip().rstrip(".")
    row = [l for l in s2b3.splitlines() if l.startswith("| **" + k)][0]
    print(k, "| texte P6 l.%d dans la ligne du §2 bis :" % lt, ("« %s »" % texte) in row, "| statut l.%d :" % ls, ("« %s »" % statut) in row,
          "| occurrences du texte dans v0.4.2 / v0.4.3 :", v2.count(texte), "/", v3.count(texte))
# lignes du §2 bis modifiees
a = set(s2b2.splitlines()); b = set(s2b3.splitlines())
print("§2 bis, lignes retirees :", [l[:110] for l in a - b])
print("§2 bis, lignes ajoutees :", [l[:110] for l in b - a])
# lignes du diff qui mentionnent un arbitrage
pat = re.compile(r"M-04|M-05|R-5|R-6|R-7|R-8")
for l in diff:
    if (l.startswith("+") or l.startswith("-")) and not l.startswith(("+++", "---")) and pat.search(l):
        print(l[0], l[1:150])
