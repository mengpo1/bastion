"""Contrôle du périmètre de l'erratum AR-01/AR-02 (relecteur, lecture seule).
Usage : python3 -I perimetre.py <v0.4.3 initiale> <v0.4.3 erratum>
Code de sortie 0 si tous les contrôles réussissent, 1 sinon."""
import sys, re, difflib
A = open(sys.argv[1], encoding="utf-8").read()
B = open(sys.argv[2], encoding="utf-8").read()
La, Lb = A.splitlines(), B.splitlines()
ok = True
def t(nom, cond):
    global ok
    ok &= bool(cond)
    print(("OK    " if cond else "ECHEC ") + nom)

# 1. Blocs modifiés, ligne à ligne
sm = difflib.SequenceMatcher(a=La, b=Lb, autojunk=False)
ops = [op for op in sm.get_opcodes() if op[0] != "equal"]
for tag, i1, i2, j1, j2 in ops:
    print("  bloc %-7s v043 l.%d-%d -> erratum l.%d-%d" % (tag, i1 + 1, i2, j1 + 1, j2))
ancien = [l for _, i1, i2, _, _ in ops for l in La[i1:i2]]
nouveau = [l for _, _, _, j1, j2 in ops for l in Lb[j1:j2]]
t("trois lignes retirées : titre, l.355 (§5), l.833 (§17)",
  [La.index(l) + 1 for l in ancien] == [1, 355, 833])
t("huit lignes ajoutées", len(nouveau) == 8)

# 2. §5 : seule la phrase visée change dans la ligne 355
old5 = La[354]; new5 = Lb[355]
s_old = "Or OXCE ne réduit pas la récupération d'énergie selon la charge : `prepareEnergy` (`src/Savegame/BattleUnit.cpp:2733-2742`, commit `441cae1b`) ne tient compte que des blessures mortelles au torse."
k = old5.index(s_old)
pre, post = old5[:k], old5[k + len(s_old):]
t("§5 : préfixe de la ligne inchangé", new5.startswith(pre))
t("§5 : suffixe de la ligne inchangé", new5.endswith(post))
milieu = new5[len(pre):len(new5) - len(post)]
print("  §5 : phrase remplacée par %d caractères, %d phrases" % (len(milieu), len(re.findall(r"[.;:]\s+(?=[A-ZÉÀ])|[.]$", milieu))))
t("§5 : [OUV] du point d'articulation conservé", new5.startswith("- **Point d'articulation** [OUV] (OB-06) :"))
t("§5 : phrase finale du point conservée", new5.endswith("L'articulation de N14 et d'ARB-D avec M-04=B, décision postérieure du propriétaire, reste à traiter avec les modalités de M-04=B."))

# 3. §17 : seule l'introduction change
def sec(t_, a, b): return t_[t_.index(a):t_.index(b)]
s17a = sec(A, "## 17. ", "## 18. "); s17b = sec(B, "## 17. ", "## 18. ")
tab = lambda s: [l for l in s.splitlines() if l.startswith("|")]
t("§17 : tableau des contrôles identique (lignes '|')", tab(s17a) == tab(s17b) and len(tab(s17a)) == 15)
corr = lambda s: [l for l in s.splitlines() if l.startswith("**Correspondance")]
t("§17 : correspondance avec le §4 de P7 identique", corr(s17a) == corr(s17b) and len(corr(s17a)) == 1)
imp = lambda s: s[s.index("**Impossibilités"):]
t("§17 : impossibilités de vérification identiques", imp(s17a) == imp(s17b))
t("§17 : phrase fautive retirée", "Chaque contrôle a été exécuté avec" not in B)
t("§17 : suite de l'introduction conservée", "Les scripts sont inventoriés au §15 (S-1 à S-13). Les numéros 1 à 11 sont ceux de la v0.4.2, pour que les renvois restent valables ; les contrôles 12 et 13 sont nouveaux." in s17b)

# 4. Toutes les autres sections identiques
heads = lambda s: re.split(r"(?m)^(?=## )", s)
SA, SB = heads(A), heads(B)
t("même découpage en sections", [x.splitlines()[0] for x in SA[1:]] == [x.splitlines()[0] for x in SB[1:]])
diff_secs = [x.splitlines()[0] for x, y in zip(SA[1:], SB[1:]) if x != y]
print("  sections différentes :", diff_secs)
t("seules §5 et §17 diffèrent (hors en-tête)", diff_secs == ["## 5. Coûts, ressources et surcharge", "## 17. Vérification interne de la v0.4.3"])

# 5. Marqueurs de statut : nombre inchangé
for m in ("[OUV]", "[DÉD]", "[INS]", "[VAL]", "[TR]", "[TR-M]", "[PNV", "(recommandé)", "Sp", "Pa"):
    t("marqueur %s : %d -> %d" % (m, A.count(m), B.count(m)), A.count(m) == B.count(m))

# 6. OC-01 à OC-07 non corrigées : texte d'origine toujours présent
oc = {
 "OC-01 (RD-9)": "ne sont authentifiés que par leur empreinte (RV42, §5)",
 "OC-02 (G1-05)": "géométrie et praticabilité du trajet",
 "OC-03 (§10, G3)": "coûts de chaque connexion (Q3.10=B)",
 "OC-05 (§11)": "Autres décisions, dont les six arbitrages du §2 bis",
 "OC-06 (§5, « n'est fixé ; »)": "Aucun multiplicateur, arrondi ni pénalité d'énergie n'est fixé ;",
 "OC-07 (I-1)": "le message reçu le 19 novembre",
}
for nom, s in oc.items():
    t("%s : %d -> %d occurrence(s)" % (nom, A.count(s), B.count(s)), A.count(s) == B.count(s) and A.count(s) >= 1)
row = lambda L, p: [l for l in L if l.startswith(p)]
t("OC-04 : ligne T47 identique", row(La, "| T47 |") == row(Lb, "| T47 |") and len(row(La, "| T47 |")) == 1)
i6 = [i for i, l in enumerate(Lb) if l.startswith("  - la formule de surcharge des TU") and l.endswith("n'est fixé ;")]
t("OC-06 : au §5, la sous-liste finit toujours par « n'est fixé ; » avant le rappel du registre (OB-01)",
  len(i6) == 1 and Lb[i6[0] + 1].startswith("- **Rappel du registre**"))

# 7. Lignes de tableau (matrices, scénarios, décisions) : toutes identiques
ta = [l for l in La if l.startswith("|")]; tb = [l for l in Lb if l.startswith("|")]
t("toutes les lignes de tableau identiques (%d)" % len(ta), ta == tb)

# 8. Phrase finale et statut inchangés
t("phrase finale inchangée", A.rstrip().splitlines()[-1] == B.rstrip().splitlines()[-1])
st = lambda s: s[s.index("**Statut :**"):s.index("## 0. Provenance")]
t("bloc Statut inchangé", st(A) == st(B))
print("TOUS_OK", ok)
sys.exit(0 if ok else 1)
