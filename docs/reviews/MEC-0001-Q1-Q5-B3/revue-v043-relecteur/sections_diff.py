import sys, re, difflib
a = open(sys.argv[1], encoding="utf-8").read().splitlines(); b = open(sys.argv[2], encoding="utf-8").read().splitlines()
def secmap(L):
    cur = "en-tete"; m = []
    for l in L:
        if re.match(r"^#{2,3} ", l): cur = l.split(" ", 1)[1][:40]
        m.append(cur)
    return m
ma, mb = secmap(a), secmap(b)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
touched = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal": continue
    secs = set(ma[i1:i2]) | set(mb[j1:j2]) or {mb[j1] if j1 < len(mb) else ma[i1]}
    for s in secs: touched.setdefault(s, [0, 0]); touched[s][0] += i2 - i1; touched[s][1] += j2 - j1
allsecs = []
for s in mb:
    if s not in allsecs: allsecs.append(s)
for s in allsecs:
    print(("MODIFIEE   " if s in touched else "inchangee  ") + s + ("   (-%d / +%d lignes)" % tuple(touched[s]) if s in touched else ""))
