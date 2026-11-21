import json, sys, re
src, dst = sys.argv[1], sys.argv[2]
out = []
k = 0
with open(src, encoding="utf-8") as f:
    for line in f:
        try:
            o = json.loads(line)
        except Exception:
            continue
        if o.get("type") != "user" or o.get("isMeta") or o.get("isCompactSummary"):
            continue
        c = o.get("message", {}).get("content")
        if isinstance(c, str):
            texts = [c]
        elif isinstance(c, list):
            texts = [x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text"]
        else:
            texts = []
        t = "\n".join(texts)
        t = re.sub(r"<system-reminder>.*?</system-reminder>", "", t, flags=re.S).strip()
        if not t or t.startswith("This session is being continued from a previous conversation"):
            continue
        if t.startswith("<command-") or t.startswith("<local-command"):
            continue
        k += 1
        out.append("\n\n======== MESSAGE %d — horodatage du journal : %s ========\n\n%s" % (k, o.get("timestamp", "?"), t))
hdr = ("# Messages du propriétaire reçus dans la session (extraction mécanique)\n\n"
       "Extraits par script du journal de session (`" + src + "`) : seules les entrées de type « user » "
       "contenant du texte ; résumés de compaction, résultats d'outils et blocs <system-reminder> exclus. "
       "Aucune réponse de Claude Code n'y figure. Texte non modifié.\n")
open(dst, "w", encoding="utf-8").write(hdr + "".join(out) + "\n")
print("messages:", k)
