import time
from state import state_awal_acak, ukuran
from objective import nilai, valid
from langkah import swap, pindahkan, keluarkan, rotate


def semua_neighbor(state, kendaraan, kapal):
    hasil = []
    ids = list(state)

    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            if state[ids[a]] != state[ids[b]]:
                hasil.append(swap(state, ids[a], ids[b]))

    for k in kendaraan:
        for o in ["H", "V"]:
            lebar, tinggi = ukuran(k, o)
            for y in range(kapal["Dimensi"]["w"] - tinggi + 1):
                for x in range(kapal["Dimensi"]["l"] - lebar + 1):
                    if state[k["id"]] != (x, y, o):
                        hasil.append(pindahkan(state, k["id"], x, y, o))

    for id_k in ids:
        if state[id_k] is not None:
            hasil.append(keluarkan(state, id_k))
            hasil.append(rotate(state, id_k))

    return [n for n in hasil if valid(n, kendaraan, kapal)]


def steepest_ascent(kendaraan, kapal):
    mulai = time.time()
    state = state_awal_acak(kendaraan, kapal)
    awal = state
    nilai_sekarang = nilai(state, kendaraan)
    riwayat = [nilai_sekarang]
    iterasi = 0

    while True:
        terbaik = None
        nilai_terbaik = nilai_sekarang
        for n in semua_neighbor(state, kendaraan, kapal):
            if nilai(n, kendaraan) > nilai_terbaik:
                terbaik = n
                nilai_terbaik = nilai(n, kendaraan)

        if terbaik is None:
            break

        state = terbaik
        nilai_sekarang = nilai_terbaik
        riwayat.append(nilai_sekarang)
        iterasi += 1          

    return {
        "awal": awal,
        "akhir": state,
        "nilai_akhir": nilai_sekarang,
        "riwayat": riwayat,
        "iterasi": iterasi,
        "durasi": time.time() - mulai,
    }