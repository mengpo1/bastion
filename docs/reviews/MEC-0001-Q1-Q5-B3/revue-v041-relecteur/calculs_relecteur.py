from fractions import Fraction as F
import math, itertools
ok = True
def chk(name, got, exp):
    global ok
    r = (got == exp)
    ok &= r
    print(f"{'OK ' if r else 'KO '} {name}: calcule={got} attendu={exp}")
ceil = math.ceil; floor = math.floor
def terrain(base, fac):  # Q3.13 : base x facteur, arrondi superieur par ressource
    return ceil(F(base) * fac)
def diag_tu(c): return floor(c * F(3, 2))   # S2
def diag_e(c):  return ceil(c * F(3, 2))    # Q3.9
B_TU, B_E = 4, 2   # Q3.7
fac = {"normal": F(1), "difficile": F(3, 2), "tres difficile": F(2)}  # Q3.8
attendu = {"normal": ((4, 2), (6, 3)), "difficile": ((6, 3), (9, 5)), "tres difficile": ((8, 4), (12, 6))}
for t, f in fac.items():
    o = (terrain(B_TU, f), terrain(B_E, f)); d = (diag_tu(o[0]), diag_e(o[1]))
    chk("bareme " + t, (o, d), attendu[t])
    print("    OXCE floor(TU/2) ortho/diag :", o[0] // 2, d[0] // 2, "| Bastion E :", o[1], d[1])
# T01
chk("T01 restes", (60 - 4, 100 - 2), (56, 98))
# T02
chk("T02 cout", (diag_tu(terrain(4, F(3, 2))), diag_e(terrain(2, F(3, 2)))), (9, 5))
chk("T02 restes", (60 - 9, 100 - 5), (51, 95))
chk("T02 OXCE energie floor(9/2)", 9 // 2, 4)
# T05 : enumeration exhaustive des chemins de 1 a 4 pas vers (+2, -1) (est = +x, nord = -y)
dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
vec = {"N": (0, -1), "NE": (1, -1), "E": (1, 0), "SE": (1, 1), "S": (0, 1), "SW": (-1, 1), "W": (-1, 0), "NW": (-1, -1)}
best = None; cands = []
for n in range(1, 5):
    for p in itertools.product(dirs, repeat=n):
        x = sum(vec[d][0] for d in p); y = sum(vec[d][1] for d in p)
        if (x, y) != (2, -1): continue
        tu = sum(6 if vec[d][0] and vec[d][1] else 4 for d in p)
        e = sum(3 if vec[d][0] and vec[d][1] else 2 for d in p)
        cands.append(((tu, e), [dirs.index(d) for d in p], p))
mincost = min(c[0] for c in cands)
ties = [c for c in cands if c[0] == mincost]
chk("T05 cout minimal", mincost, (10, 5))
chk("T05 ex aequo", sorted(c[2] for c in ties), sorted([("NE", "E"), ("E", "NE")]))
chk("T05 choix lexicographique", min(ties, key=lambda c: c[1])[2], ("NE", "E"))
# T11a
chk("T11a restes", (60 - 4, 100 - 2), (56, 98))
# T18
o = (terrain(3, F(3, 2)), terrain(1, F(3, 2)))
chk("T18 orthogonal", o, (5, 2))
chk("T18 diagonal (A)", (diag_tu(o[0]), diag_e(o[1])), (7, 3))
print("    T18 option B, TU 3x1,5x1,5 =", F(3) * F(9, 4), "-> plancher", floor(F(27, 4)), "plafond", ceil(F(27, 4)), "; E 1x2,25 =", F(9, 4))
# T19
chk("T19", diag_tu(5), 7)
# T20
def surcharge(total, cap, charge):
    f = F(1) if charge == 0 else min(F(1), F(cap, charge))
    return floor(total * f)
chk("T20 a", surcharge(60, 30, 40), 45)
chk("T20 b", surcharge(60, 30, 0), 60)
chk("T20 c exact", surcharge(22, 15, 22), 15)
chk("T20 c flottant naif", math.floor(22 * (15 / 22)), 14)
print("    22*(15/22) en flottant =", repr(22 * (15 / 22)))
# T21 (max 20)
def arbd(solde, recup, mx, f): return floor(min(solde + recup, mx) * f)
chk("T21 a", arbd(7, 15, 20, F(3, 4)), 15)
chk("T21 b", arbd(2, 15, 20, F(1)), 17)
chk("T21 c", arbd(4, 12, 20, F(3, 4)), 12)
chk("T21 d", floor(20 * F(30, 45)), 13)
print("    T21 d valeur exacte :", 20 * F(30, 45))
chk("W-03 min(solde+60,60) pour solde 0..60", {min(s + 60, 60) for s in range(0, 61)}, {60})
chk("P0-05 (v1.4.1) min(7+15,20)", min(7 + 15, 20), 20)
chk("P0-06 (v1.4.1) 20x0,75", floor(20 * F(3, 4)), 15)
# T22 : carte 2x2 ; arrivee normale ; cases intermediaires difficiles
diag = (6, 3); det = (terrain(4, F(3, 2)) + 4, terrain(2, F(3, 2)) + 2)
chk("T22 diagonale", diag, (6, 3)); chk("T22 detour", det, (10, 5))
for e in (2, 3):
    adm = [n for n, c in (("diag", diag), ("detour", det)) if c[0] <= 20 and c[1] <= e]
    print(f"    T22 energie {e} : chemins admissibles (1-2 pas) = {adm}")
# borne : tout chemin quitte (0,0) par un pas coutant >= 3 energie (diag 3, ortho difficile 3)
chk("T22 borne premier pas", min(3, terrain(2, F(3, 2))), 3)
# T23 / T37
def g4(c, bud):
    adm = [k for k, v in c.items() if v[0] <= bud[0] and v[1] <= bud[1]]
    return min(adm, key=lambda k: (c[k][0], c[k][1])) if adm else None
chk("T23 a", g4({"A": (17, 11), "B": (18, 2)}, (20, 12)), "A")
chk("T23 b", g4({"A": (17, 11), "B": (18, 2)}, (20, 10)), "B")
chk("T37", g4({"A": (18, 10), "B": (18, 9)}, (20, 12)), "B")
# T26 et §3.6
chk("largeur interieure", 1500 - 2 * 50, 1400)
s2 = math.sqrt(2)
debout45 = 600 * s2; couche45 = (1200 + 600) / s2
def pair_sup(x):
    n = math.ceil(x)
    return n if n % 2 == 0 else n + 1
print("    debout 45 deg =", debout45, "; couche 45 deg =", couche45)
chk("enveloppe debout 45", pair_sup(debout45), 850)
chk("enveloppe couche 45", pair_sup(couche45), 1274)
# verification exacte : 850^2/2 > ... : 600*sqrt2 <= 850 <=> 720000 <= 722500 ; 849 < 600 sqrt2 ?
chk("600*sqrt2 dans ]848, 850] (exact, carres)", (848**2 < 2 * 600**2 <= 850**2), True)
chk("1800/sqrt2 dans ]1272, 1274] (exact, carres)", (2 * 1272**2 < 1800**2 <= 2 * 1274**2), True)
mx = math.hypot(1200, 600); ang = math.degrees(math.atan2(600, 1200))
print(f"    etendue max couche = {mx:.4f} mm a {ang:.2f} deg")
chk("etendue max couche < 1400 (exact)", 1200**2 + 600**2 < 1400**2, True)
chk("etendue max arrondie 0,1", round(mx, 1), 1341.6)
chk("rapport case/etage", F(1500, 3000), F(1, 2))
# T39, T43, T44, T45
chk("T39 debit unique", (4, 2), (4, 2))
chk("T44 cout 2 pas", (8, 4), (2 * 4, 2 * 2))
chk("T44 hors zone (5 TU < 8)", 5 < 8, True)
chk("T44 ancienne S5 : 5-4", 5 - 4, 1)
chk("T45 restes", (60 - 6, 100 - 3), (54, 97))
chk("T28 sans supplement", (4, 2), (B_TU, B_E))
print("TOUS_OK =", ok)
raise SystemExit(0 if ok else 1)
