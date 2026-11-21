import re, sys
ext = open(sys.argv[1], encoding="utf-8").read()
parts = re.split(r"\n\n======== MESSAGE (\d+) — horodatage du journal : (\S+) ========\n\n", ext)
msgs = {int(parts[i]): (parts[i+1], parts[i+2]) for i in range(1, len(parts), 3)}
p1 = open(sys.argv[2], encoding="utf-8").read().splitlines()
p5 = open(sys.argv[3], encoding="utf-8").read().splitlines()
v = open(sys.argv[4], encoding="utf-8").read()
A = [p1[i-1] for i in (301,303,305,307)]
B = [re.search(r"« (.*) »", p5[i-1]).group(1) for i in (14,15,16,17)]
for lab in B:
    where = [n for n,(ts,b) in msgs.items() if lab in b]
    print("option B", repr(lab[:45]), "-> messages :", where)
for lab in A:
    where = [n for n,(ts,b) in msgs.items() if lab in b]
    print("option A", repr(lab[:45]), "-> messages :", where)
s01 = v[v.index("### 0.1 "):v.index("## 1. Périmètre")]; s31 = v[v.index("### 3.1 "):v.index("### 3.2 ")]
print("8 libelles entre guillemets au par.0.1 :", all(("« "+l+" »") in s01 for l in A+B), "; au par.3.1 :", all(("« "+l+" »") in s31 for l in A+B))
val = re.search(r"« (.*) »", p1[308]).group(1)
print("validation P1 l.309 dans message 31 :", val in msgs[31][1], "; au par.0.1 :", ("« "+val+" »") in s01)
print("mot 'option B' ou ' B :' dans le message 31 :", bool(re.search(r"option B|— B", msgs[31][1])))
