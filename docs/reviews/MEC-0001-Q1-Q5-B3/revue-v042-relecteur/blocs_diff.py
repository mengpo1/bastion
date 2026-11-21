import re, sys
patch = open(sys.argv[1], encoding="utf-8").read().split("\n")
v = open(sys.argv[2], encoding="utf-8").read().split("\n")
heads = [(i+1, l) for i,l in enumerate(v) if re.match(r"^#{2,3} ", l)]
def sec_of(n):
    s = "(en-tete)"
    for ln, l in heads:
        if ln <= n: s = l[:60]
    return s
k = 0
for i, l in enumerate(patch):
    m = re.match(r"^@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@", l)
    if m:
        k += 1
        start = int(m.group(3)); length = int(m.group(4) or 1)
        # premiere ligne modifiee du bloc
        j = i+1; n = start; first = None
        while j < len(patch) and not patch[j].startswith("@@"):
            if patch[j].startswith("+") or patch[j].startswith("-"):
                first = n; break
            if not patch[j].startswith("-"): n += 1
            j += 1
        print(f"bloc {k:2d} : v0.4.2 l.{start}-{start+length-1} ; 1re ligne modifiee ~l.{first} ; section : {sec_of(first or start)}")
