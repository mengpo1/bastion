import re, sys
D, R = sys.argv[1], sys.argv[2]
src_paths = {
 "P1": D + "/revue-v03/PIECES-Q1-Q3-TRANSMISES.md",
 "P2": D + "/revue-v03/PIECES-Q4-Q5-B3-DECLARATIONS.md",
 "P3": D + "/revue-v03/PIECES-MANDATS-ET-CONFIRMATIONS.md",
 "P4": D + "/revue-v03/RAPPORT-REVUE-INDEPENDANTE-v0.3.md",
 "P5": D + "/revue-v03/PIECE-Q1.1-Q1.4-OPTIONS-B.md",
 "v0.2": "/root/.claude/uploads/7361641c-6eb6-5649-a764-279757212cf3/4f625a0d-BASTION-MEC-0001-CONSOLIDATION-Q1-Q4-REVUE.md",
 "R": R + "/registre.md", "v1.4.1": R + "/v141.md", "LOT-2A": R + "/lot2a.md",
}
def norm(s):
    s = re.sub(r"\s*\(recommandé\)\s*", "", s)
    s = re.sub(r"\s*×\s*", "×", s)
    s = s.lower()
    s = s.replace("**", "").replace("*", "").replace("`", "")
    s = s.replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()
srcs = {k: norm(open(p, encoding="utf-8").read()) for k, p in src_paths.items()}
doc = open(D + "/revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-v0.4.1.md", encoding="utf-8").read()
lines = doc.split("\n")
def quotes(line):
    # extraction des citations « ... » avec imbrication
    out = []; depth = 0; start = None
    for i, ch in enumerate(line):
        if ch == "«":
            if depth == 0: start = i + 1
            depth += 1
        elif ch == "»" and depth > 0:
            depth -= 1
            if depth == 0: out.append(line[start:i])
    return out
nf = []
total = 0
for n, line in enumerate(lines, 1):
    for q in quotes(line):
        total += 1
        qn = norm(q)
        # les citations elidees ou imbriquees : tester chaque fragment separe par « … » ou « [...] »
        frags = [norm(f) for f in re.split(r"…|\[…\]|\[\.\.\.\]|«|»", q) if len(norm(f)) >= 6]
        where = [k for k, s in srcs.items() if qn in s]
        if not where and frags:
            fw = [[k for k, s in srcs.items() if f in s] for f in frags]
            if all(fw): where = ["fragments:" + ",".join(sorted(set(sum(fw, []))))]
        if not where:
            nf.append((n, q))
print("citations examinees :", total, "; introuvables telles quelles :", len(nf))
for n, q in nf:
    print(f"  l.{n}: «{q[:160]}»")
