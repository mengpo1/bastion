import sys, re
def parse(p):
    t = open(p, encoding="utf-8").read()
    parts = re.split(r"\n\n======== MESSAGE (\d+) — horodatage du journal : (\S+) ========\n\n", t)
    hdr = parts[0]
    msgs = []
    for i in range(1, len(parts), 3):
        msgs.append((int(parts[i]), parts[i+1], parts[i+2]))
    # last message body ends with a trailing "\n" added by the script
    if msgs:
        n, ts, body = msgs[-1]
        msgs[-1] = (n, ts, body[:-1] if body.endswith("\n") else body)
    return msgs
mine = parse(sys.argv[1])
for name in sys.argv[2:]:
    other = parse(name)
    n = len(other)
    same = all(mine[i] == other[i] for i in range(n))
    diffs = [i+1 for i in range(n) if mine[i] != other[i]]
    print(name.split('/')[-1], "nb =", n, "; identiques a mes", n, "premiers :", same, "; ecarts :", diffs)
print("mes messages :", len(mine))
