import math
import random
import time
from state import state_awal_acak
from objective import nilai
from hill_climbing import semua_neighbor


def simulated_annealing(kendaraan, kapal, suhu_awal=100, laju_pendinginan=0.99, suhu_akhir=0.01):
    mulai = time.time()
    state = state_awal_acak(kendaraan, kapal)
    awal = state
    nilai_sekarang = nilai(state, kendaraan)
    terbaik, nilai_terbaik = state, nilai_sekarang
    riwayat, probabilitas = [nilai_sekarang], []
    stuck = 0
    suhu = suhu_awal
    tetangga = semua_neighbor(state, kendaraan, kapal)

    while suhu > suhu_akhir:
        if all(nilai(n, kendaraan) <= nilai_sekarang for n in tetangga):
            stuck += 1

        n = random.choice(tetangga)
        delta = nilai(n, kendaraan) - nilai_sekarang

        if delta > 0:
            terima = True
        else:
            p = math.exp(delta / suhu)
            probabilitas.append((len(riwayat) - 1, p))
            terima = random.random() < p

        if terima:
            state = n
            nilai_sekarang = nilai(n, kendaraan)
            tetangga = semua_neighbor(state, kendaraan, kapal)
            if nilai_sekarang > nilai_terbaik:
                terbaik, nilai_terbaik = state, nilai_sekarang

        riwayat.append(nilai_sekarang)
        suhu *= laju_pendinginan

    return {
        "awal": awal,
        "akhir": terbaik,
        "nilai_akhir": nilai_terbaik,
        "riwayat": riwayat,
        "probabilitas": probabilitas,
        "stuck": stuck,
        "iterasi": len(riwayat) - 1,
        "durasi": time.time() - mulai,
    }