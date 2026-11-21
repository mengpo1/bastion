import sys, re
a = open(sys.argv[1], encoding="utf-8").read(); b = open(sys.argv[2], encoding="utf-8").read()
for tok in ["[OUV]", "[PNV]", "**[PNV]**", "Ouvert", "ouvert", "ouverts", "ouvertes", "Restent ouverts", "non spécifi", "non décid", "à définir"]:
    print("%-18s v0.4.2=%3d  v0.4.3=%3d" % (tok, a.count(tok), b.count(tok)))
# Fragments ouverts des lignes retirees : chaque segment portant [OUV] ou 'ouvert' doit se retrouver dans la v0.4.3
dl = [l[1:] for l in open(sys.argv[3], encoding="utf-8") if l.startswith("-") and not l.startswith("---")]
miss = []
for l in dl:
    for seg in re.split(r"[;|]", l):
        s = seg.strip()
        if ("[OUV]" in s or "ouvert" in s.lower() or "[PNV]" in s) and len(s) > 8:
            core = re.sub(r"\s+", " ", s)
            if core not in re.sub(r"\s+", " ", b):
                miss.append(core[:160])
print("segments ouverts retires et absents de la v0.4.3 :", len(miss))
for m in miss: print("  -", m)
