def swap(state, id_a, id_b):
    baru = dict(state)
    baru[id_a], baru[id_b] = baru[id_b], baru[id_a]
    return baru

def pindahkan(state, id_k, x, y, o):
    baru = dict(state)
    baru[id_k] = (x, y, o)
    return baru

def keluarkan(state, id_k):
    baru = dict(state)
    baru[id_k] = None
    return baru

def rotate(state, id_k):
    baru = dict(state)
    x, y, o = baru[id_k]
    baru[id_k] = (x, y, "V" if o == "H" else "H")
    return baru