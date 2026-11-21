import sys, re
def parse(p):
    t = open(p, encoding="utf-8").read()
    parts = re.split(r"\n\n======== MESSAGE (\d+) — horodatage du journal : (\S+) ========\n\n", t)
    hdr = parts[0]
    msgs = [(int(parts[i]), parts[i+1], parts[i+2].rstrip("\n")) for i in range(1, len(parts), 3)]
    return hdr, msgs
h_mine, mine = parse(sys.argv[1])
for other in sys.argv[2:]:
    h_o, o = parse(other)
    n = len(o)
    same = all(mine[i] == o[i] for i in range(n))
    print(other.split("/")[-1], "messages:", n, "| en-tetes identiques:", h_mine == h_o, "| les", n, "premiers messages identiques:", same)
    # reconstruct prefix file
    rebuilt = h_mine + "".join("\n\n======== MESSAGE %d — horodatage du journal : %s ========\n\n%s" % m for m in mine[:n]) + "\n"
    print("   reconstruction octet a octet identique au fichier:", rebuilt == open(other, encoding="utf-8").read())
print("dernier message de mon extraction:", mine[-1][0], mine[-1][1], repr(mine[-1][2][:90]))
