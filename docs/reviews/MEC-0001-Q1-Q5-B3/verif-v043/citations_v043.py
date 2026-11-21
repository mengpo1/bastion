import sys, re, subprocess
doc_path, SP = sys.argv[1], sys.argv[2]
doc = open(doc_path, encoding="utf-8").read()
def norm(s):
    # tolérances admises (revue de la v0.4.1, §4.3) : casse, mention « (recommandé) », espacement autour de ×
    s = s.replace("**", "").replace("`", "").replace("’", "'").replace("*", "").replace("(recommandé)", "")
    s = re.sub(r"\s*×\s*", " × ", s)
    s = re.sub(r"\s+([.,])", r"\1", s)  # espace laissée avant le point par le retrait de « (recommandé) »
    return re.sub(r"\s+", " ", s).strip().lower()
def quotes(t):
    st, out = [], []
    for i, ch in enumerate(t):
        if ch == "«": st.append(i)
        elif ch == "»" and st:
            j = st.pop(); out.append(t[j+1:i])
    return out
R = "/home/user/bastion"
def git(p): return subprocess.run(["git", "-C", R, "show", "origin/main:" + p], capture_output=True, text=True, check=True).stdout
prim = [open(SP + "/" + p, encoding="utf-8").read() for p in (
    "revue-v03/PIECES-Q1-Q3-TRANSMISES.md", "revue-v03/PIECES-Q4-Q5-B3-DECLARATIONS.md", "revue-v03/PIECES-MANDATS-ET-CONFIRMATIONS.md",
    "revue-v03/RAPPORT-REVUE-INDEPENDANTE-v0.3.md", "revue-v03/PIECE-Q1.1-Q1.4-OPTIONS-B.md", "revue-v03/PIECE-MANDAT-v0.4.2-ARBITRAGES.md",
    "revue-v03/PIECE-MANDAT-v0.4.3-CORRECTIONS.md", "verif-v043/messages-extraction-3.md",
    "revue-v041-relecteur/RAPPORT-REVUE-INDEPENDANTE-v0.4.1.md", "revue-v042-relecteur/RAPPORT-REVUE-INDEPENDANTE-v0.4.2.md")]
prim.append(open("/root/.claude/uploads/7361641c-6eb6-5649-a764-279757212cf3/4f625a0d-BASTION-MEC-0001-CONSOLIDATION-Q1-Q4-REVUE.md", encoding="utf-8").read())
for p in ("docs/gameplay/GAMEPLAY-DECISIONS.md", "docs/reviews/BASTION-MEC-0001-CONSOLIDATION-v1.4.1-CORRECTIFS-MINEURS.md",
          "docs/mandates/BASTION-MANDAT-INSCRIPTION-DOCUMENTAIRE-MEC-0001-v1.0-VALIDE.md", "docs/reviews/MEC-0001-INSCRIPTION-ARB-G-2026-11-17.md",
          "docs/reviews/MEC-0001-ARCHIVAGE-SOURCES-2026-11-17.md", "docs/reviews/LOT-2A-MOUVEMENT-TACTIQUE.md", "docs/references/OXCE-BASELINE.md"):
    prim.append(git(p))
P = norm("\n".join(prim))
anc = norm("\n".join(open(SP + "/revue-v03/BASTION-MEC-0001-CONSOLIDATION-Q1-Q5-B3-" + v + ".md", encoding="utf-8").read() for v in ("v0.3", "v0.4", "v0.4.1", "v0.4.2")))
D = norm(doc)
qs = quotes(doc); n_p = n_s = 0; introuvables = []
for q in qs:
    frags = [f for f in (norm(x) for x in re.split(r"…|\[…\]", q)) if len(f) >= 3]
    if not frags: n_s += 1; continue
    if all(f in P for f in frags): n_p += 1
    elif all(f in anc or D.count(f) >= 2 for f in frags): n_s += 1
    else: introuvables.append(q)
print("citations :", len(qs), "; sources primaires :", n_p, "; document ou versions antérieures :", n_s, "; introuvables :", len(introuvables))
for q in introuvables: print("  INTROUVABLE :", norm(q)[:150])
