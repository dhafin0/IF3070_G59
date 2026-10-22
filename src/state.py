import random

def ukuran(k, o):
    w,l = k["Dimensi"]["w"], k["Dimensi"]["l"]
    if o == "H":
        return l, w
    else:
        return w, l

def state_awal_acak(kendaraan, kapal):
    terisi, berat, state = set(), 0, {}
    for k in random.sample(kendaraan, len(kendaraan)):
        o = random.choice(["H", "V"])
        lebar, tinggi = ukuran(k,o)
        x = random.randint(0, kapal["Dimensi"]["l"] - lebar)
        y = random.randint(0, kapal["Dimensi"]["w"] - tinggi)
        sel = {(x + i, y + j) for i in range(lebar) for j in range(tinggi)}

        menimpa = False
        for s in sel:
            if s in terisi:
                menimpa = True

        if menimpa or berat + k["Weight"] > kapal["MaxCapacity"]:
            state[k["id"]] = None
        else:
            state[k["id"]] = (x, y, o)
            terisi.update(sel)
            berat += k["Weight"]
    return state


def show_geladak(state, kendaraan, kapal):
    geladak = [["."] * kapal["Dimensi"]["l"] for _ in range(kapal["Dimensi"]["w"])]
    for k in kendaraan:
        if state[k["id"]] is None:
            continue
        x, y, o = state[k["id"]]
        lebar, tinggi = ukuran(k,o)
        for j in range(tinggi):
            for i in range(lebar):
                geladak[y + j][x + i] = k["id"]
    for baris in geladak:
        print(" ".join(f"{s:>12}" for s in baris))