import json, sys, hashlib
journal, v04path = sys.argv[1], sys.argv[2]
v04 = open(v04path, encoding="utf-8").read()
title = "# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4\n"
hits = []
with open(journal, encoding="utf-8") as f:
    for line in f:
        try: o = json.loads(line)
        except Exception: continue
        if o.get("type") != "assistant": continue
        c = o.get("message", {}).get("content")
        if not isinstance(c, list): continue
        for x in c:
            if isinstance(x, dict) and x.get("type") == "text" and title in x.get("text", ""):
                hits.append((o.get("timestamp"), o.get("isSidechain"), x["text"]))
print("messages de l'auteur contenant le titre v0.4 :", len(hits))
for ts, side, t in hits:
    i = t.index(title)
    body = t[i:]
    # comparer le fichier a la portion du message qui commence au titre
    same_prefix = body.startswith(v04.rstrip("\n"))
    print("horodatage", ts, "sidechain", side, "| fichier == message[titre:] :", body.rstrip("\n") == v04.rstrip("\n"), "| fichier prefixe :", same_prefix, "| len msg", len(body), "len fichier", len(v04))
    if body.rstrip("\n") != v04.rstrip("\n"):
        # premier ecart
        a, b = body, v04
        k = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), min(len(a), len(b)))
        print("  premier ecart a l'index", k, ": message", repr(a[k-60:k+80]), "\n  fichier", repr(b[k-60:k+80]))
        print("  reste du message apres le fichier :", repr(a[len(b.rstrip(chr(10))):][:300]))
