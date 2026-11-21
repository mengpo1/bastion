import struct
from fractions import Fraction as F
def f32(x): return struct.unpack("f", struct.pack("f", x))[0]
# emulation de BattleUnit.cpp:2717-2720 : [code OXCE retiré — D4]
diff = []
for s in range(1, 121):
    for w in range(1, 121):
        enc = f32(f32(float(s)) / f32(float(w)))
        if enc >= 1: continue
        for tu in range(1, 121):
            o = int(f32(enc * f32(float(tu))))
            e = (F(s, w) * tu).__floor__()
            if o != e: diff.append((s, w, tu, o, e))
print("cas (Force, poids, TU) <= 120 ou la troncature float32 differe du plancher exact :", len(diff))
print("exemples :", diff[:5])
print("cas 15/22, 22 TU :", int(f32(f32(f32(15.0) / f32(22.0)) * f32(22.0))), "exact :", (F(15, 22) * 22).__floor__())
