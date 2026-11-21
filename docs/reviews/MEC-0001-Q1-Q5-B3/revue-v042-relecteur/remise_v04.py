import json, sys
src, v04 = sys.argv[1], open(sys.argv[2], encoding="utf-8").read()
target = sys.argv[3]
with open(src, encoding="utf-8") as f:
    for line in f:
        try: o = json.loads(line)
        except Exception: continue
        if o.get("timestamp") != target: continue
        c = o.get("message", {}).get("content")
        texts = [c] if isinstance(c, str) else [x.get("text","") for x in (c or []) if isinstance(x, dict) and x.get("type")=="text"]
        t = "\n".join(texts)
        print("type:", o.get("type"), "| longueur texte:", len(t))
        print("v0.4 (fichier) contenue telle quelle dans ce message :", v04.rstrip("\n") in t)
        print("debut du message :", repr(t[:80]))
        i = t.find(v04.rstrip("\n")[:200])
        print("position du debut de la v0.4 dans le message :", i)
