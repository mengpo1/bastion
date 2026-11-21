import re, sys
# Pour chaque citation « ... » immediatement suivie d'un renvoi (P1 l.N), (P6 l.N-M), (R:N) ou (D:N),
# verifie que la citation figure dans les lignes indiquees de la piece.
v = open(sys.argv[1], encoding="utf-8").read().split("\n")
P = {}
for spec in sys.argv[2:]:
    k, p = spec.split("=", 1)
    P[k] = open(p, encoding="utf-8").read().split("\n")
NBSP = chr(0xA0); NNBSP = chr(0x202F)
def norm(s):
    s = s.replace(" (recommandé)", "").replace(NBSP, " ").replace(NNBSP, " ").replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip().lower().strip(" .;:,")
pat = re.compile(r"«\s*([^«»]{6,}?)\s*»\s*\((P[1-6]) l\.(\d+)(?:-(\d+))?\)|«\s*([^«»]{6,}?)\s*»\s*\((R|D):(\d+)(?:-(\d+))?\)")
ok = ko = 0
for ln, line in enumerate(v, 1):
    for m in pat.finditer(line):
        if m.group(1):
            q, k, a, b = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
        else:
            q, k, a, b = m.group(5), m.group(6), int(m.group(7)), int(m.group(8) or m.group(7))
        if k not in P: continue
        zone = norm(" ".join(P[k][a-1:b]))
        frags = [f for f in re.split(r"\s*(?:\[…\]|…)\s*", q) if len(norm(f)) >= 6]
        good = all(norm(f) in zone for f in frags)
        if good: ok += 1
        else:
            ko += 1; print(f"  ECART l.{ln} : « {q[:80]} » ({k} l.{a}-{b})")
print("renvois concordants :", ok, "; ecarts :", ko)
