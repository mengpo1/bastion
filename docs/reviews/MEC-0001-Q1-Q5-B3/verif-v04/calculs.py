from fractions import Fraction as Fr
from math import floor, ceil, sqrt, atan2, degrees, cos, sin
import itertools
def up(x): return -((-x.numerator)//x.denominator)
def dn(x): return x.numerator//x.denominator
def cout(tu, en, fac, diag):
    tu2, en2 = up(Fr(tu)*fac), up(Fr(en)*fac)
    if diag: return dn(Fr(tu2)*Fr(3,2)), up(Fr(en2)*Fr(3,2))
    return tu2, en2
R = {}
for nom, fac in (("normal", Fr(1)), ("difficile", Fr(3,2)), ("tres difficile", Fr(2))):
    R[nom] = (cout(4,2,fac,False), cout(4,2,fac,True))
print("bareme", R)
assert R == {"normal":((4,2),(6,3)), "difficile":((6,3),(9,5)), "tres difficile":((8,4),(12,6))}
print("T01", 60-4, 100-2); print("T02", 60-9, 100-5, "loi OXCE energie", (9)//2)
# T05 : enumeration exhaustive des suites de pas (au plus 4) de (0,0) a (2,-1), y vers le sud
D = {"N":(0,-1),"NE":(1,-1),"E":(1,0),"SE":(1,1),"S":(0,1),"SW":(-1,1),"W":(-1,0),"NW":(-1,-1)}
ordre = list(D)
best = []
for n in range(1,5):
    for seq in itertools.product(ordre, repeat=n):
        x=y=0; tu=en=0
        for s in seq:
            dx,dy=D[s]; x+=dx; y+=dy
            c = (6,3) if dx and dy else (4,2); tu+=c[0]; en+=c[1]
        if (x,y)==(2,-1): best.append((tu,en,[ordre.index(s) for s in seq],seq))
best.sort()
m = [b for b in best if b[:2]==best[0][:2]]
print("T05 minimum", best[0][:2], "ex aequo", [b[3] for b in m], "choix", best[0][3])
print("T18", cout(3,1,Fr(3,2),False), cout(3,1,Fr(3,2),True)); print("T19", dn(Fr(5)*Fr(3,2)))
def surch(total, cap, charge):
    F = Fr(1) if charge==0 else min(Fr(1), Fr(cap,charge)); return dn(Fr(total)*F)
print("T20", surch(60,30,40), surch(60,30,0), surch(22,15,22), "flottant naif", floor(22*(15/22)))
def arbd(sol, rec, mx, F): return dn(Fr(min(sol+rec, mx))*F)
print("T21", arbd(7,15,20,Fr(3,4)), arbd(2,15,20,Fr(1)), arbd(4,12,20,Fr(3,4)), dn(Fr(20)*Fr(30,45)))
print("min(s+60,60) pour s=0..60:", {min(s+60,60) for s in range(61)})
print("T22 diag", R["normal"][1], "detour", tuple(a+b for a,b in zip(R["difficile"][0], R["normal"][0])))
print("T23", "A" if (17<=20 and 11<=12) else "B", "B" if not (11<=10) else "A")
print("T37", min([("A",18,10),("B",18,9)], key=lambda c:(c[1],c[2]))[0])
print("T44 cout", 8, 4, "admissible avec 5 TU:", 8<=5, "S5: reste", 5-4)
print("T45", 60-6, 100-3)
print("T26", 1500-2*50, 600*sqrt(2), 850, (1200+600)/sqrt(2), 1274)
th = max((1200*cos(a)+600*sin(a), a) for a in [i*1e-5 for i in range(int(1.5708/1e-5))])
print("rotation max", round(th[0],1), "a", round(degrees(th[1]),2), "deg ; sqrt", round(sqrt(1200**2+600**2),1))
print("rapport", Fr(1500,3000))
# enveloppes paires superieures
def pair_sup(x): n = ceil(x); return n if n%2==0 else n+1
assert pair_sup(600*sqrt(2))==850 and pair_sup((1200+600)/sqrt(2))==1274
print("enveloppes paires OK")
