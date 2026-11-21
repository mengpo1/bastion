import sys, re
ext = open(sys.argv[1], encoding="utf-8").read()
copies = {p: open(p, encoding="utf-8").read() for p in sys.argv[2:]}
parts = re.split(r"\n\n======== MESSAGE (\d+) — horodatage du journal : (\S+) ========\n\n", ext)
msgs = [(int(parts[i]), parts[i+1], parts[i+2].rstrip("\n")) for i in range(1, len(parts), 3)]
for n, ts, body in msgs:
    if n < 22: continue
    where = [p.split("/")[-1] for p, t in copies.items() if body in t]
    if where:
        print(f"{n:2d} {ts}  INTEGRAL dans {where}  ({len(body)} car.)")
        continue
    # plus long préfixe présent
    best = (0, None)
    for p, t in copies.items():
        lo, hi = 0, len(body)
        while lo < hi:
            mid = (lo + hi + 1)//2
            if body[:mid] in t: lo = mid
            else: hi = mid - 1
        if lo > best[0]: best = (lo, p.split("/")[-1])
    k, p = best
    first = body.splitlines()[0][:70]
    if k < 40:
        print(f"{n:2d} {ts}  NON COPIE  « {first} »")
    else:
        rest = body[k:].strip().splitlines()[0][:80]
        print(f"{n:2d} {ts}  PARTIEL dans {p} : {k}/{len(body)} car. ; omis à partir de « {rest} »")
