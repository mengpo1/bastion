import sys, re
sys.path.insert(0, sys.argv[1])
exec(open(sys.argv[1] + "/compare_extractions.py").read().split("mine = parse")[0])
msgs = parse(sys.argv[2])
copies = {}
for p in sys.argv[3:]:
    copies[p.split('/')[-1]] = open(p, encoding="utf-8").read()
def norm(s): return re.sub(r"\s+", " ", s).strip()
ncopies = {k: norm(v) for k, v in copies.items()}
for n, ts, body in msgs[:38]:
    if n < 22: continue
    hits = [k for k, v in copies.items() if body in v]
    nhits = [k for k, v in ncopies.items() if norm(body) in v]
    if hits:
        print(n, ts, "INTEGRAL exact dans", hits)
    elif nhits:
        print(n, ts, "INTEGRAL a l'espacement pres dans", nhits)
    else:
        # longest prefix found
        best = (0, None)
        nb = norm(body)
        for k, v in ncopies.items():
            lo, hi = 0, len(nb)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if nb[:mid] in v: lo = mid
                else: hi = mid - 1
            if lo > best[0]: best = (lo, k)
        print(n, ts, "NON INTEGRAL ; plus long prefixe copie :", best[0], "/", len(nb), "car. dans", best[1], "| debut :", nb[:best[0]][:60].replace("\n"," "))
