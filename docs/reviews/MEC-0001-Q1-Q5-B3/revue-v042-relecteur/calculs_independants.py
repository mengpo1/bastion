from fractions import Fraction as F
from math import floor, ceil, isqrt
import struct, itertools
ok = True
def chk(label, got, exp):
    global ok
    r = (got == exp); ok &= r
    print(("OK  " if r else "ECHEC"), label, "->", got, "(attendu", exp, ")")
H = F(3,2)
def terrain(base_tu, base_en, fac):  # Q3.8 + Q3.13 : facteur terrain puis arrondi superieur
    return ceil(F(base_tu)*fac), ceil(F(base_en)*fac)
def diag(tu, en):  # S2 (TU x1,5 arrondi inferieur) ; Q3.9 (energie x1,5 arrondi superieur)
    return floor(F(tu)*H), ceil(F(en)*H)
fac = {"normal": F(1), "difficile": F(3,2), "tres difficile": F(2)}
bareme = {}
for k, f in fac.items():
    o = terrain(4, 2, f); d = diag(*o); bareme[k] = (o, d)
chk("bareme normal", bareme["normal"], ((4,2),(6,3)))
chk("bareme difficile", bareme["difficile"], ((6,3),(9,5)))
chk("bareme tres difficile", bareme["tres difficile"], ((8,4),(12,6)))
# par. 11 : coincidence avec floor(TU/2)
coinc = {(k,t): (bareme[k][i][1], bareme[k][i][0]//2) for k in fac for i,t in enumerate(("orth","diag"))}
diff = [kt for kt,(e,o) in coinc.items() if e != o]
chk("par.11 seule difference avec floor(TU/2)", diff, [("difficile","diag")])
chk("par.11 diag difficile : Bastion / OXCE", coinc[("difficile","diag")], (5,4))
# T01
chk("T01", (60-4, 100-2), (56,98))
# T02
(tu,en) = bareme["difficile"][1]; chk("T02 cout", (tu,en), (9,5)); chk("T02 reste", (60-tu,100-en), (51,95)); chk("T02 loi OXCE energie", tu//2, 4)
# T05 : enumeration exhaustive des chemins de 1 a 4 pas, cible (+2 est, +1 nord)
dirs = ["N","NE","E","SE","S","SW","W","NW"]
vec = {"N":(0,1),"NE":(1,1),"E":(1,0),"SE":(1,-1),"S":(0,-1),"SW":(-1,-1),"W":(-1,0),"NW":(-1,1)}
best = None; cands = []
for n in range(1,5):
    for p in itertools.product(dirs, repeat=n):
        x = sum(vec[d][0] for d in p); y = sum(vec[d][1] for d in p)
        if (x,y) != (2,1): continue
        tu = sum(6 if len(d)==2 else 4 for d in p); en = sum(3 if len(d)==2 else 2 for d in p)
        cands.append(((tu,en),[dirs.index(d) for d in p],p))
cands.sort()
mn = cands[0][0]
ties = [c[2] for c in cands if c[0]==mn]
chk("T05 cout minimal", mn, (10,5)); chk("T05 ex aequo", sorted(ties), sorted([("NE","E"),("E","NE")])); chk("T05 retenu", cands[0][2], ("NE","E"))
# T11a, T39
chk("T11a reste", (56,98), (60-4,100-2)); chk("T39 debit unique", bareme["normal"][0], (4,2))
# T18 base 3/1 difficile
o = terrain(3,1,F(3,2)); chk("T18 orth", o, (5,2)); chk("T18 diag (option A)", diag(*o), (7,3))
chk("T18 option B TU non arrondie", F(3)*F(3,2)*F(3,2), F(27,4))
# T19
chk("T19", floor(F(5)*H), 7)
# T20
def surcharge(total, cap, charge):
    f = F(1) if charge == 0 else min(F(1), F(cap, charge)); return floor(total*f)
chk("T20 a", surcharge(60,30,40), 45); chk("T20 b", surcharge(60,30,0), 60); chk("T20 c", surcharge(22,15,22), 15)
chk("T20 c flottant naif", floor(22*(15/22)), 14)
# T21 : max 20
def arbd(solde, recup, mx, f): return floor(min(F(solde+recup), F(mx))*f)
chk("T21 (7,15,0.75)", arbd(7,15,20,F(3,4)), 15); chk("T21 (2,15,1)", arbd(2,15,20,F(1)), 17)
chk("T21 (4,12,0.75)", arbd(4,12,20,F(3,4)), 12); chk("T21 (20, 30/45)", floor(F(20)*F(30,45)), 13)
chk("T21 profil Q4.6 : min(s+60,60)=60 pour s in [0,60]", all(min(s+60,60)==60 for s in range(0,61)), True)
# T22 : 2x2, arrivee normale, intermediaires difficiles
dg = bareme["normal"][1]; det = tuple(a+b for a,b in zip(bareme["difficile"][0], bareme["normal"][0]))
chk("T22 diagonale", dg, (6,3)); chk("T22 detour", det, (10,5))
chk("T22 energie 2 : aucun chemin", [c for c in (dg, det) if c[1] <= 2] + [x for x in [bareme["difficile"][0]] if x[1] <= 2], [])
chk("T22 energie 3 : diagonale seule", [c for c in (dg, det) if c[0]<=20 and c[1]<=3], [(6,3)])
# T23, T37 : G4
def g4(cands, b):
    adm = [c for c in cands if c[1]<=b[0] and c[2]<=b[1]]
    return min(adm, key=lambda c:(c[1],c[2]))[0] if adm else None
chk("T23 20/12", g4([("A",17,11),("B",18,2)],(20,12)), "A"); chk("T23 20/10", g4([("A",17,11),("B",18,2)],(20,10)), "B")
chk("T37", g4([("A",18,10),("B",18,9)],(20,12)), "B")
# T44
chk("T44 hors zone (8 TU > 5)", 8 > 5, True); chk("T44 ancienne S5 : un pas, reste", 5-4, 1)
# T43, T45
chk("T45 reste", (60-6,100-3), (54,97))
# T47 (a) profil Q4.6
tu, en = 60, 100
seq = [bareme["normal"][0], bareme["difficile"][0], bareme["normal"][0]]
for c in seq:
    assert tu >= c[0] and en >= c[1]; tu -= c[0]; en -= c[1]
chk("T47 (a) reste apres le 3e pas", (tu,en), (46,93))
chk("T47 cout reel du 2e pas = terrain difficile", bareme["difficile"][0], (6,3))
# T47 (b) : 5 TU et 98 d'energie avant le 2e pas
chk("T47 (b) 2e pas non payable (6 > 5)", 6 > 5, True); chk("T47 (b) reste", (5,98), (5,98))
# Coherence de T47 (b) avec Z1/G3 : etat initial et cout prevu de l'ordre
init_b = (5+4, 98+2); prevu = (3*4, 3*2)
print("INFO T47 (b) : etat initial reconstitue", init_b, "; cout prevu de l'ordre de trois pas", prevu,
      "; destination dans la zone Z1/G3 :", init_b[0] >= prevu[0] and init_b[1] >= prevu[1])
# minimum de TU avant le 2e pas pour un ordre valide de trois pas (pas 2 et 3 prevus a 4 TU) :
print("INFO T47 : TU minimales avant le 2e pas pour un ordre selectionnable :", 2*4, "; cout reel du 2e pas :", 6, "-> toujours payable :", 2*4 >= 6)
# T48
ext = F(1205,1) ; # (600+605)/sqrt(2) : encadrement exact par les carres
x = 1205*1205  # (1205/sqrt2)^2 = 1205^2/2
v2 = F(x,2)
lo = isqrt(x//2)  # partie entiere
chk("T48 (b) partie entiere de 1205/sqrt(2)", lo, 852)
chk("T48 (b) 852 < 1205/sqrt(2) < 853", (852**2 < v2) and (v2 < 853**2), True)
env = next(e for e in range(0,2000,2) if e*e >= v2)
chk("T48 (b) enveloppe Q2.6 (plus petit pair qui contient)", env, 854)
rp = round(1205/2**0.5); chk("T48 (b) arrondi prealable au mm le plus proche", rp, 852)
chk("T48 (b) 852 contient-il le volume ?", 852*852 >= v2, False)
cp = ceil(1205/2**0.5); env_c = cp if cp%2==0 else cp+1
print("INFO T48 (b) : arrondi prealable SUPERIEUR au mm :", cp, "-> enveloppe paire", env_c, "(donc 852 seulement pour un arrondi au plus proche ou inferieur)")
print("INFO T48 (b) valeur decimale :", 1205/2**0.5)
# par. 3.6 et T26
chk("largeur interieure", 1500-2*50, 1400)
chk("debout 45 deg : 848 < 600*sqrt2 <= 850", (848**2 < 2*600**2) and (2*600**2 <= 850**2), True)
env1 = next(e for e in range(0,2000,2) if e*e >= 2*600**2); chk("enveloppe debout", env1, 850)
env2 = next(e for e in range(0,3000,2) if 2*e*e >= 1800**2); chk("enveloppe couche (1800/sqrt2)", env2, 1274)
import math
mx = math.hypot(1200,600); ang = math.degrees(math.atan2(600,1200))
chk("etendue max couche (arrondie 0,1 mm)", round(mx,1), 1341.6); chk("angle (arrondi 0,1)", round(ang,1), 26.6)
chk("1341,6 < 1400", mx < 1400, True); chk("rapport case/etage", F(1500,3000), F(1,2))
# par. 11 : emulation float32 (pas une execution d'OXCE)
f32 = lambda v: struct.unpack('f', struct.pack('f', v))[0]
enc = f32(f32(1.0)/f32(41.0)); prod = f32(enc*f32(41.0))
chk("emulation float32 1/41 x 41 = 0,99999994", repr(prod)[:10], "0.99999994")
chk("tronque a 0 ; exact = 1", (int(prod), floor(F(1,41)*41)), (0,1))
print("TOUS_OK =", ok)
