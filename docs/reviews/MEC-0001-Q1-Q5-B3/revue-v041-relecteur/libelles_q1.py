import sys
D = sys.argv[1]
p1 = open(D + "/revue-v03/PIECES-Q1-Q3-TRANSMISES.md", encoding="utf-8").read().split("\n")
p5 = open(D + "/revue-v03/PIECE-Q1.1-Q1.4-OPTIONS-B.md", encoding="utf-8").read().split("\n")
v = open(D + "/revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md", encoding="utf-8").read().split("\n")
A = {f"Q1.{k+1}": p1[300 + 2*k] for k in range(4)}          # lignes 301, 303, 305, 307 (index 0)
B = {}
for k in range(4):
    l = p5[13 + k]                                            # lignes 14 a 17
    B[f"Q1.{k+1}"] = l.split("« ", 1)[1].rsplit(" »", 1)[0]
ok = True
for q in A:
    row = next(x for x in v[100:110] if x.startswith(f"| {q}=A"))
    ra, rb = ("« " + A[q] + " »") in row, ("« " + B[q] + " »") in row
    ok &= ra and rb
    print(q, "A present :", ra, "| B present :", rb)
# reconstitution P5 l.45-48 conforme a P1 et au message I ?
for k in range(4):
    row = p5[44 + k]; q = f"Q1.{k+1}"
    print(q, "reconstitution P5 : A =", ("« " + A[q] + " »") in row, "; B =", ("« " + B[q] + " »") in row, "; validation =", f"{q}=A" in row)
print("validation P1 l.309 :", "je valide Q1.1=A, Q1.2=A, Q1.3=A, Q1.4=A" in p1[308])
raise SystemExit(0 if ok else 1)
