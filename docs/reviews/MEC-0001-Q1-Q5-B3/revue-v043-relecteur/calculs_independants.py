from fractions import Fraction as Fr
from math import isqrt
ok = True
def chk(nom, c):
    global ok; ok &= bool(c); print(("OK    " if c else "ECHEC ") + nom)
# Barème (Q3.7, Q3.8, Q3.13, S2, Q3.9) : coût orthogonal en terrain difficile
def ceil_fr(x): return -((-x.numerator) // x.denominator)
def floor_fr(x): return x.numerator // x.denominator
base = (4, 2)
diff = (ceil_fr(Fr(4) * Fr(3, 2)), ceil_fr(Fr(2) * Fr(3, 2)))
chk("pas orthogonal difficile = (6, 3) (Q3.8, Q3.13)", diff == (6, 3))
# Simulation M-05=A : contrôle avant chaque pas, débit au coût réel, arrêt sans débit si non payable
def selection(tu, en, connu):
    return sum(c[0] for c in connu) <= tu and sum(c[1] for c in connu) <= en   # Z1 + G3 (R:90, R:141)
def execute(tu, en, reel):
    faits = 0
    for c in reel:
        if c[0] <= tu and c[1] <= en:
            tu -= c[0]; en -= c[1]; faits += 1
        else:
            return tu, en, faits, "arret avant le pas %d, sans debit" % (faits + 1)
    return tu, en, faits, "ordre acheve"
connu = [base] * 3
reel = [base, diff, base]
# (a) profil Q4.6
chk("T47 (a) selection admissible", selection(60, 100, connu))
r = execute(60, 100, reel); print("   T47 (a) ->", r)
chk("T47 (a) reste 46 TU / 93 energie, 3 pas", r[:3] == (46, 93, 3))
# (b) 12 TU / 100 energie
chk("T47 (b) selection admissible (12 <= 12 TU, 6 <= 100)", selection(12, 100, connu))
tu, en = 12 - 4, 100 - 2
chk("T47 (b) apres le premier pas : 8 / 98", (tu, en) == (8, 98))
r = execute(12, 100, reel); print("   T47 (b) ->", r)
chk("T47 (b) deuxieme pas execute, arret avant le troisieme : 2 / 95, 2 pas", r[:3] == (2, 95, 2) and "pas 3" in r[3])
# ancien (b) de la v0.4.2 : 5 TU avant le 2e pas => 9 TU a la selection, non selectionnable
chk("v0.4.2 T47 (b) : 9 TU a la selection, trajet non selectionnable (AN-03)", not selection(9, 100, connu))
# Domaine des etats initiaux selectionnables qui exercent les deux comportements
dom = [t for t in range(0, 61) if selection(t, 100, connu) and execute(t, 100, reel)[2] == 2]
print("   TU initiales selectionnables donnant 'pas 2 execute, arret avant pas 3' :", dom)
chk("12 TU est dans ce domaine", 12 in dom)
# T48 (b) : etendue d'un rectangle 600 x 605 tourne de 45 degres = 1205 / sqrt(2) ; e^2 = 1205^2 / 2
e2 = Fr(1205 ** 2, 2)
chk("852 < e < 852,5 (e^2 entre 852^2 et 852,5^2)", Fr(852) ** 2 < e2 < Fr(1705, 2) ** 2)
fl = isqrt(int(e2)); ce = fl + 1; pp = fl if e2 < Fr(2 * fl + 1, 2) ** 2 else ce
def pair_sup_entier(n): return n if n % 2 == 0 else n + 1
def pair_sup_exact(e2):   # plus petit pair p tel que p >= e
    p = 0
    while Fr(p) ** 2 < e2: p += 2
    return p
print("   plancher", fl, "; plafond", ce, "; plus proche", pp)
chk("enveloppe sans arrondi prealable = 854 (Q2.6)", pair_sup_exact(e2) == 854)
chk("arrondi prealable au plus proche -> 852", pair_sup_entier(pp) == 852)
chk("arrondi prealable inferieur -> 852", pair_sup_entier(fl) == 852)
chk("arrondi prealable superieur -> 853 puis 854", ce == 853 and pair_sup_entier(ce) == 854)
chk("852 ne contient pas le volume (852^2 < e^2)", Fr(852) ** 2 < e2)
# §3.6 et T26 (inchanges, controle de non-regression)
chk("1 400 mm", 1500 - 2 * 50 == 1400)
chk("debout 45 deg : 1200/sqrt2 -> 850", pair_sup_exact(Fr(1200 ** 2, 2)) == 850)
chk("couche 45 deg : 1800/sqrt2 -> 1274", pair_sup_exact(Fr(1800 ** 2, 2)) == 1274)
print("TOUS_OK", ok)
