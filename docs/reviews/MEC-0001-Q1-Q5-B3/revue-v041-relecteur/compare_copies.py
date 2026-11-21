import re, sys
D = sys.argv[1]
msgs_txt = open(D + "/revue-v03/MESSAGES-PROPRIETAIRE-JOURNAL-SESSION.md", encoding="utf-8").read()
parts = re.split(r"\n\n======== MESSAGE (\d+) — horodatage du journal : (\S+) ========\n\n", msgs_txt)
msgs = {}
for i in range(1, len(parts), 3):
    msgs[int(parts[i])] = (parts[i+1], parts[i+2].rstrip("\n"))
def piece_sections(path, header_re):
    t = open(path, encoding="utf-8").read()
    secs = re.split(header_re, t)
    return t, secs
def norm(s):
    return re.sub(r"\s+", " ", s).strip()
def check(name, body, mnum):
    ts, m = msgs[mnum]
    body = body.strip("\n")
    # strip trailing separator
    body = re.sub(r"\n+---\s*$", "", body).strip("\n")
    exact = body in m
    normd = norm(body) in norm(m)
    equal = body == m
    print(f"{name} vs MESSAGE {mnum} ({ts}): egal={equal} sous-chaine_exacte={exact} sous-chaine_normalisee={normd} len_piece={len(body)} len_msg={len(m)}")
    return body, m
# P1
p1 = open(D + "/revue-v03/PIECES-Q1-Q3-TRANSMISES.md", encoding="utf-8").read()
a = p1.index("## Message 1 (reçu en premier)"); b = p1.index("## Message 2 (reçu ensuite)")
m1 = p1[a:b].split("\n", 1)[1]
m2 = p1[b:].split("\n", 1)[1]
body, m = check("P1 message 1", m1, 30)
body2, m = check("P1 message 2", m2, 31)
# Where does P1 msg2 end in msg 31
print("  P1 msg2 = prefixe du message 31 :", m.startswith(body2.strip()))
print("  reste du message 31 non copie commence par :", repr(m[len(body2.strip()):][:40]))
# P2
p2 = open(D + "/revue-v03/PIECES-Q4-Q5-B3-DECLARATIONS.md", encoding="utf-8").read()
heads = [("A", "## Message A", 24), ("B", "## Message B", 25), ("C", "## Message C", 26), ("D", "## Message D", 27), ("E", "## Message E", 28)]
idx = [p2.index(h) for _, h, _ in heads] + [len(p2)]
for k, (n, h, mn) in enumerate(heads):
    sec = p2[idx[k]:idx[k+1]].split("\n", 1)[1]
    check("P2 message " + n, sec, mn)
# P3
p3 = open(D + "/revue-v03/PIECES-MANDATS-ET-CONFIRMATIONS.md", encoding="utf-8").read()
heads = [("F", "## Message F", 32), ("G", "## Message G", 33), ("H", "## Message H", 34)]
idx = [p3.index(h) for _, h, _ in heads] + [len(p3)]
for k, (n, h, mn) in enumerate(heads):
    sec = p3[idx[k]:idx[k+1]].split("\n", 1)[1]
    check("P3 message " + n, sec, mn)
# P5
p5 = open(D + "/revue-v03/PIECE-Q1.1-Q1.4-OPTIONS-B.md", encoding="utf-8").read()
a = p5.index("## Message I"); b = p5.index("## Reconstitution")
sec = p5[a:b].split("\n", 1)[1]
check("P5 message I", sec, 35)
