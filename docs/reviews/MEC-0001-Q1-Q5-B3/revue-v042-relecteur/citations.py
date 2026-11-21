import re, sys
# Controle des citations « ... » d'un document contre des sources.
# Normalisation : espaces insecables, gras, accents graves, mention « (recommande) » des
# propositions P1 (retiree par la consolidation), espacement autour de « x ».
doc = open(sys.argv[1], encoding="utf-8").read()
srcs = {p.split("/")[-1]: open(p, encoding="utf-8").read() for p in sys.argv[2:]}
NBSP = chr(0xA0); NNBSP = chr(0x202F); TIMES = chr(0xD7)
def norm(s):
    s = s.replace(" (recommandé)", "").replace("(recommandé)", "")
    s = s.replace(NBSP, " ").replace(NNBSP, " ").replace("**", "").replace("`", "")
    s = s.replace(TIMES, " " + TIMES + " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()
NS = {k: norm(v) for k, v in srcs.items()}
lines = doc.split("\n")
found = 0
rep = []
for ln, line in enumerate(lines, 1):
    depth = 0; start = None
    for i, ch in enumerate(line):
        if ch == "«":
            if depth == 0: start = i + 1
            depth += 1
        elif ch == "»" and depth > 0:
            depth -= 1
            if depth == 0:
                q = line[start:i]
                frags = [f for f in re.split(r"\s*(?:\[…\]|…)\s*", q) if len(norm(f)) >= 6]
                if not frags: continue
                okall = all(any(norm(f).strip(" .;:,") in v for v in NS.values()) for f in frags)
                if okall: found += 1
                else: rep.append((ln, q[:150]))
print("citations retrouvees dans une source :", found)
print("citations non retrouvees :", len(rep))
for ln, q in rep: print(f"  l.{ln}: « {q} »")
