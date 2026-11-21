import sys, re
exec(open(sys.argv[1] + "/compare_extractions.py").read().split("mine = parse")[0])
msgs = {n: b for n, ts, b in parse(sys.argv[2])}
for p, nums in ((sys.argv[3], range(24, 29)), (sys.argv[4], range(32, 35)), (sys.argv[5], [30, 31]), (sys.argv[6], [35]), (sys.argv[7], [36]), (sys.argv[8], [38])):
    t = open(p, encoding="utf-8").read()
    heads = [(m.start(), m.group(0)) for m in re.finditer(r"^## Message [^\n]*", t, re.M)]
    for n in nums:
        b = msgs[n]
        key = b if b in t else b[:1000]
        pos = t.find(key)
        h = [x for x in heads if x[0] < pos]
        print("JS-%d -> %s : %s" % (n, p.split("/")[-1], h[-1][1][:70] if h else "?"))
