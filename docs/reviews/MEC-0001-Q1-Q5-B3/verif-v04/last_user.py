import json, sys
path = sys.argv[1]
marker = "complément de provenance et revue v0.4"
hits = []
with open(path, encoding="utf-8") as f:
    for n, line in enumerate(f):
        try:
            o = json.loads(line)
        except Exception:
            continue
        if o.get("type") != "user":
            continue
        c = o.get("message", {}).get("content")
        texts = []
        if isinstance(c, str):
            texts = [c]
        elif isinstance(c, list):
            texts = [x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text"]
        for t in texts:
            if marker in t:
                hits.append((n, t))
print("occurrences:", len(hits), file=sys.stderr)
n, t = hits[0]
sys.stdout.write(t)
