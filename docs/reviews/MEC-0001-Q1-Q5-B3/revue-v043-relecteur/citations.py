import sys, re, glob
doc_path, diff_path = sys.argv[1], sys.argv[2]
prim = sys.argv[3].split(",")
second = sys.argv[4].split(",")
def norm(s):
    s = s.replace(" ", " ").replace(" ", " ")
    s = re.sub(r"\s+", " ", s)
    s = s.replace(" × ", "×").replace("×", " × ")
    return s.strip()
def load(ps):
    return [(p.split("/")[-1], norm(open(p, encoding="utf-8", errors="replace").read())) for p in ps]
P = load(prim); S = load(second)
def quotes(line):
    out, stack = [], []
    for i, ch in enumerate(line):
        if ch == "«": stack.append(i)
        elif ch == "»" and stack:
            j = stack.pop(); out.append(line[j+1:i])
    return out
added = set()
for l in open(diff_path, encoding="utf-8"):
    if l.startswith("+") and not l.startswith("+++"): added.add(l[1:].rstrip("\n"))
doc = open(doc_path, encoding="utf-8").read().split("\n")
res = {"prim":0, "second":0, "none":0}
for ln, line in enumerate(doc, 1):
    isnew = line in added
    for q in quotes(line):
        nq = norm(q)
        if len(nq) < 3: continue
        cands = [nq, nq[0].lower()+nq[1:], nq[0].upper()+nq[1:], nq.replace(" (recommandé)", "")]
        hit = next((n for n, t in P if any(c in t for c in cands)), None)
        if hit:
            res["prim"] += 1
            if isnew: print("NEW  l.%d PRIM [%s] « %s »" % (ln, hit, q[:90]))
            continue
        hit = next((n for n, t in S if any(c in t for c in cands)), None)
        if hit:
            res["second"] += 1
            print("%s l.%d SECONDAIRE [%s] « %s »" % ("NEW " if isnew else "OLD ", ln, hit, q[:90]))
        else:
            res["none"] += 1
            print("%s l.%d INTROUVABLE « %s »" % ("NEW " if isnew else "OLD ", ln, q[:120]))
print(res)
