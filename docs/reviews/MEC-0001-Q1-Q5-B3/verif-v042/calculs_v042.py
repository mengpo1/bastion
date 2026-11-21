from fractions import Fraction as Fr
from math import sqrt, ceil
def pair_sup(x):
    n = ceil(x); return n if n % 2 == 0 else n + 1
# T47 : 3 pas ; 2e pas à 6/3 ; profil 60/100
tu, en = 60, 100
for c in [(4,2),(6,3),(4,2)]:
    assert c[0] <= tu and c[1] <= en; tu -= c[0]; en -= c[1]
print("T47 (a)", tu, en); assert (tu, en) == (46, 93)
tu, en = 5, 98; print("T47 (b) pas payable ?", 6 <= tu and 3 <= en, "-> reste", tu, en)
# T48 (b) : 600 x 605 à 45°
x = 1205 / sqrt(2); print("T48 (b) etendue", round(x, 3), "exact->", pair_sup(x), "arrondi prealable->", pair_sup(round(x)))
assert 852 < x < 852.5 and pair_sup(x) == 854 and pair_sup(round(x)) == 852
# encadrement exact : 852^2*2 < 1205^2 < 852.5^2*2
assert 852**2 * 2 < 1205**2 < Fr(1705,2)**2 * 2
print("T48 (a) entiers", float(1500).is_integer(), float(100).is_integer(), float(600.5).is_integer(), "parite 1500", 1500 % 2 == 0)
print("T21 explication", {min(s + 60, 60) for s in range(0, 61)}, 7+15, 2+15, 4+12, Fr(20)*Fr(30,45))
print("OK")
