import re, sys
# Variante : renvoi AVANT la citation, forme « (P1 l.N-M) : « ... » » ou « (P6 l.N) : « ... » »,
# et lignes de tableau du par.3.1 / par.4 : citation en colonne 2, source « P1 l.N-M » en colonne 3.
v = open(sys.argv[1], encoding="utf-8").read().split("\n")
P = {}
for spec in sys.argv[2:]:
    k, p = spec.split("=", 1); P[k] = open(p, encoding="utf-8").read().split("\n")
NBSP = chr(0xA0); NNBSP = chr(0x202F)
def norm(s):
    s = s.replace(" (recommandé)", "").replace(NBSP, " ").replace(NNBSP, " ").replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip().lower().strip(" .;:,")
def check(ln, q, k, a, b):
    zone = norm(" ".join(P[k][a-1:b]))
    frags = [f for f in re.split(r"\s*(?:\[…\]|…)\s*", q) if len(norm(f)) >= 6]
    return all(norm(f) in zone for f in frags)
ok = ko = 0
pat = re.compile(r"\((P[1-6]|R|D)[: ](?:l\.)?(\d+)(?:-(\d+))?\)\s*:\s*«\s*([^«»]{6,}?)\s*»")
for ln, line in enumerate(v, 1):
    for m in pat.finditer(line):
        k, a, b, q = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2)), m.group(4)
        if check(ln, q, k, a, b): ok += 1
        else: ko += 1; print(f"  ECART l.{ln} : « {q[:70]} » ({k} l.{a}-{b})")
    # lignes de tableau : | ID | « ... » | P1 l.a-b, c ; P5 l.d | ...
    if line.startswith("| Q") or line.startswith("| **"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3:
            quotes = re.findall(r"«\s*([^«»]{6,}?)\s*»", cells[1])
            refs = re.findall(r"(P[1-6]) l\.(\d+)(?:-(\d+))?", cells[2])
            for q in quotes:
                if not refs: continue
                good = any(check(ln, q, k, int(a), int(b or a)) for k, a, b in refs)
                if good: ok += 1
                else: ko += 1; print(f"  ECART tableau l.{ln} : « {q[:70]} » refs {refs}")
print("renvois concordants :", ok, "; ecarts :", ko)
