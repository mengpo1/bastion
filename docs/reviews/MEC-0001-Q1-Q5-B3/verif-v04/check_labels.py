import sys, re
v, p1, p5 = (open(a, encoding="utf-8").read().splitlines() for a in sys.argv[1:4])
vt = "\n".join(v)
# section 3.1 seulement
s = vt.index("### 3.1 Décisions Q1"); e = vt.index("### 3.2 ")
sec = vt[s:e]
A = [p1[i-1] for i in (301, 303, 305, 307)]
B = []
for i in (14, 15, 16, 17):
    m = re.search(r"« (.*) »", p5[i-1]); B.append(m.group(1))
ok = True
for lab in A + B:
    found = ("« " + lab + " »") in sec
    print(("OK  " if found else "ABS ") + lab[:70])
    ok &= found
val = p1[308]
print("validation l.309:", "Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A" in val)
sys.exit(0 if ok else 1)
