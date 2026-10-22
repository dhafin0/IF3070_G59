from state import ukuran

def nilai(state, kendaraan):
    total = 0
    for k in kendaraan:
        if state[k["id"]] is not None:
            total += k["ShippingFee"]
    return total

def valid(state, kendaraan, kapal):
    terisi, berat = set(), 0
    for k in kendaraan:
        if state[k["id"]] is None:
            continue
        x, y, o = state[k["id"]]
        lebar, tinggi = ukuran(k, o)
        if x < 0 or y < 0 or x + lebar > kapal["Dimensi"]["l"] or y + tinggi > kapal["Dimensi"]["w"]:
            return False
        sel = {(x + i, y + j) for i in range(lebar) for j in range(tinggi)}
        for s in sel:
            if s in terisi:
                return False
        terisi.update(sel)
        berat += k["Weight"]
    return berat <= kapal["MaxCapacity"]