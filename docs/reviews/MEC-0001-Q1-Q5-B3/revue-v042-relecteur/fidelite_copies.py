import sys, re
ext = open(sys.argv[1], encoding="utf-8").read()
parts = re.split(r"\n\n======== MESSAGE (\d+) — horodatage du journal : (\S+) ========\n\n", ext)
msgs = {int(parts[i]): (parts[i+1], parts[i+2].rstrip("\n")) for i in range(1, len(parts), 3)}
copies = {}
for p in sys.argv[2:]:
    copies[p.split("/")[-1]] = open(p, encoding="utf-8").read()
def lcp_in(body, t):
    lo, hi = 0, len(body)
    while lo < hi:
        mid = (lo+hi+1)//2
        if body[:mid] in t: lo = mid
        else: hi = mid-1
    return lo
print("== Sens 1 : chaque message du proprietaire (1 a 36) est-il present en entier dans une copie ? ==")
for n in sorted(msgs):
    if n > 36: continue
    ts, body = msgs[n]
    full = [c for c, t in copies.items() if body in t]
    if full:
        print(f"{n:2d} {ts} INTEGRAL {full} ({len(body)} car.)"); continue
    best = max(((lcp_in(body, t), c) for c, t in copies.items()))
    if best[0] >= 40:
        print(f"{n:2d} {ts} PARTIEL {best[1]} prefixe {best[0]}/{len(body)} ; suite omise : {body[best[0]:best[0]+70]!r}")
    elif n >= 22:
        print(f"{n:2d} {ts} NON COPIE : {body[:70]!r}")
print()
print("== Sens 2 : chaque bloc copie (entre l'en-tete '## Message' et '---') est-il une sous-chaine d'un message ? ==")
for c, t in copies.items():
    blocks = re.split(r"\n---\n", t)
    for b in blocks[1:]:
        m = re.match(r"\n## (Message[^\n]*)\n\n(.*)", b, flags=re.S)
        if not m:
            print(c, "bloc sans en-tete Message :", repr(b[:60])); continue
        title, body = m.group(1), m.group(2).rstrip("\n")
        hits = [n for n,(ts,mb) in msgs.items() if body in mb]
        print(f"{c} | {title[:60]} | {len(body)} car. | sous-chaine du message {hits}")
