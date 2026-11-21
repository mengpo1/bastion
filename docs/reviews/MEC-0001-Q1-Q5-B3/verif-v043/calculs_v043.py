from math import sqrt, ceil, floor
from fractions import Fraction as Fr
def pair_sup(n):
    n = ceil(n); return n if n % 2 == 0 else n + 1
# T47 (a)
tu, en = 60, 100
for c in [(4,2),(6,3),(4,2)]:
    assert c[0] <= tu and c[1] <= en; tu -= c[0]; en -= c[1]
assert (tu, en) == (46, 93); print("T47 (a)", tu, en)
# T47 (b) : 12 TU, 100 d'énergie à la sélection ; trajet connu 3 x (4,2)
tu, en = 12, 100
assert 3*4 <= tu and 3*2 <= en, "sélection admissible (Z1, G3)"
tu, en = tu-4, en-2; print("T47 (b) après pas 1", tu, en); assert (tu, en) == (8, 98)
assert 6 <= tu and 3 <= en; tu, en = tu-6, en-3; print("T47 (b) après pas 2", tu, en); assert (tu, en) == (2, 95)
assert not (4 <= tu); print("T47 (b) pas 3 non payable : arrêt sans débit ; reste", tu, en)
# T48 (b)
x = 1205/sqrt(2)
assert 852**2*2 < 1205**2 < Fr(1705,2)**2*2
print("T48 étendue", x, "exact ->", pair_sup(x), "; au plus proche ->", pair_sup(round(x)), "; inférieur ->", pair_sup(floor(x)), "; supérieur ->", ceil(x), "puis", pair_sup(ceil(x)))
assert (pair_sup(x), pair_sup(round(x)), pair_sup(floor(x)), ceil(x), pair_sup(ceil(x))) == (854, 852, 852, 853, 854)
print("OK")
