# Variante facultative (observation OC-04) : 12 TU / 100 energie, trajet connu 3 x (4, 2), le TROISIEME pas passe a (6, 3)
tu, en = 12, 100
assert 12 <= tu and 6 <= en                      # selection admissible (Z1, G3)
reel = [(4, 2), (4, 2), (6, 3)]
for i, (t, e) in enumerate(reel, 1):
    if t <= tu and e <= en: tu -= t; en -= e
    else: print("arret avant le pas", i, "sans debit ; reste", tu, en); break
assert (tu, en) == (4, 96); print("OK")
