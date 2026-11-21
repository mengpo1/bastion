import re, sys
v141 = open(sys.argv[1], encoding="utf-8").read()
s5 = v141[v141.index("## 5. Matrice"):v141.index("## 6. Points")]
ids = re.findall(r"^\| \*\*([A-Z0-9]+-[A-Z0-9]+)", s5, flags=re.M)
print("cas des tableaux du §5 v1.4.1 :", len(ids), ids)
tm = sorted(set(re.findall(r"T-M\d+|T-J|T-K|T-D", s5)))
print("anciens tests cités au §5.5 :", tm)
v041 = open(sys.argv[2], encoding="utf-8").read()
sec = v041[v041.index("**Sort des cas de la v1.4.1**"):v041.index("## 14.")]
def expand(txt):
    found = set(re.findall(r"\b([A-Z][A-Z0-9]*-[A-Z0-9]+)\b", txt))
    # ranges "X-01 à X-04"
    for a, b in re.findall(r"\b([A-Z][0-9A-Z]*-\d+) à ([A-Z][0-9A-Z]*-\d+)", txt):
        pa, na = a.rsplit("-", 1); pb, nb = b.rsplit("-", 1)
        if pa == pb:
            for k in range(int(na), int(nb) + 1):
                found.add("%s-%02d" % (pa, k))
    return found
f = expand(sec)
print("absents du sort v0.4.1 :", [i for i in ids if i not in f])
print("mentionnés mais absents du §5 :", sorted(x for x in f if x not in ids))
