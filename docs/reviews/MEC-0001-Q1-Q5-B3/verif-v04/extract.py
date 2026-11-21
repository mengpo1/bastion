import json, sys
path = sys.argv[1]
marker = "# BASTION — MEC-0001 — Consolidation Q1 à Q5 et B3 — v0.4"
hits = []
with open(path, encoding="utf-8") as f:
    for n, line in enumerate(f):
        try:
            o = json.loads(line)
        except Exception:
            continue
        if o.get("type") != "assistant":
            continue
        msg = o.get("message", {})
        for c in msg.get("content", []) or []:
            if isinstance(c, dict) and c.get("type") == "text" and marker in c.get("text", ""):
                hits.append((n, c["text"]))
print("occurrences:", len(hits), file=sys.stderr)
for n, t in hits:
    print("line", n, "len", len(t), file=sys.stderr)
if hits:
    n, t = hits[-1]
    i = t.index(marker)
    sys.stdout.write(t[i:])
