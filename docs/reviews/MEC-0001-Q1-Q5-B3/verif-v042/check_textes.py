import sys, re
v = open(sys.argv[1], encoding="utf-8").read()
p1 = open(sys.argv[2], encoding="utf-8").read().splitlines()
p5 = open(sys.argv[3], encoding="utf-8").read().splitlines()
p6 = open(sys.argv[4], encoding="utf-8").read().splitlines()
def sec(a, b): return v[v.index(a):v.index(b)]
s01 = sec("### 0.1 ", "## 1. Périmètre"); s31 = sec("### 3.1 ", "### 3.2 "); s2b = sec("## 2 bis.", "## 3. Géométrie")
ok = True
A = [p1[i-1] for i in (301, 303, 305, 307)]
B = [re.search(r"« (.*) »", p5[i-1]).group(1) for i in (14, 15, 16, 17)]
for lab in A + B:
    for nom, s in (("§0.1", s01), ("§3.1", s31)):
        f = ("« " + lab + " »") in s; ok &= f
        if not f: print("ABSENT", nom, lab[:60])
val = re.search(r"« (.*) »", p1[308]).group(1)
f = ("« " + val + " »") in s01; ok &= f; print("validation dans §0.1:", f)
for i in (32, 45, 59, 73, 85, 96):
    txt = re.search(r"« (.*) »", p6[i-1]).group(1)
    f = ("« " + txt + " »") in s2b; ok &= f; print("arbitrage l.%d dans §2 bis:" % i, f)
for i in (42, 56, 70, 82, 93, 107):
    st = p6[i-1].split("Statut : ")[1].rstrip(".")
    f = ("« " + st + " »") in s2b; ok &= f; print("statut l.%d:" % i, f, st)
print("TOUS_OK", ok); sys.exit(0 if ok else 1)
