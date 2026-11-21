import re, sys
t = open(sys.argv[1], encoding="utf-8").read().split("\n")
# decoupage en sections (## N. / ## 2 bis / ### N.M)
secs = {}; cur = None
for l in t:
    m = re.match(r"^(#{2,3}) (\d+(?:\.\d+)?|2 bis)\.? ", l)
    if m:
        cur = "§" + m.group(2); secs.setdefault(cur, [])
    if cur: secs[cur].append(l)
def has(sec, key):
    txt = "\n".join(sum((v for k,v in secs.items() if k == sec or k.startswith(sec + ".")), []))
    return key in txt
decl_2bis = {"M-04": "§2, §5, §9.2, §10, §12, §14", "M-05": "§2, §6, §9.2, §10, §12, §13, §14",
  "R-5": "§2, §3.1, §3.5, §9.1, §12, §13, §14", "R-6": "§2, §3.1, §3.2, §9.1, §12, §13",
  "R-7": "§2, §3.1, §3.2, §9.1, §12, §13", "R-8": "§2, §3.1, §3.4, §9.1, §12"}
decl_20 = {"M-04": "§2, §2 bis, §5, §9.2, §10, §12, §14", "M-05": "§2, §2 bis, §6, §9.2, §10, §12, §13, §14",
  "R-5": "§2, §2 bis, §3.1, §3.5, §9.1, §10, §12, §13, §14", "R-6": "§2, §2 bis, §3.1, §3.2, §9.1, §12, §13, §18",
  "R-7": "§2, §2 bis, §3.1, §3.2, §9.1, §12, §13", "R-8": "§2, §2 bis, §3.1, §3.4, §9.1, §10, §12"}
for nom, d in (("§2 bis", decl_2bis), ("§20.1", decl_20)):
    print("Declarations du", nom)
    for k, s in d.items():
        miss = [x for x in [y.strip() for y in s.split(",")] if not has(x, k)]
        print("  ", k, "absent de :", miss if miss else "aucune")
