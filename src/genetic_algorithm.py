import random
import time
from state import state_awal_acak, ukuran
from objective import nilai
from hill_climbing import semua_neighbor


def perbaiki(state, kendaraan, kapal):
    baru, terisi, berat = {}, set(), 0
    for k in kendaraan:
        posisi = state[k["id"]]
        if posisi is None:
            baru[k["id"]] = None
            continue
        x, y, o = posisi
        lebar, tinggi = ukuran(k, o)
        sel = {(x + i, y + j) for i in range(lebar) for j in range(tinggi)}
        menimpa = False
        for s in sel:
            if s in terisi:
                menimpa = True
        if menimpa or berat + k["Weight"] > kapal["MaxCapacity"]:
            baru[k["id"]] = None
        else:
            baru[k["id"]] = posisi
            terisi.update(sel)
            berat += k["Weight"]
    return baru


def seleksi(populasi, kendaraan):
    bobot = [nilai(s, kendaraan) + 1 for s in populasi]
    return random.choices(populasi, weights=bobot, k=1)[0]


def crossover(ayah, ibu, kendaraan, kapal):
    titik = random.randint(1, len(kendaraan) - 1)
    anak = {}
    for i, k in enumerate(kendaraan):
        anak[k["id"]] = ayah[k["id"]] if i < titik else ibu[k["id"]]
    return perbaiki(anak, kendaraan, kapal)


def mutasi(state, kendaraan, kapal):
    return random.choice(semua_neighbor(state, kendaraan, kapal))


def genetic_algorithm(kendaraan, kapal, jumlah_populasi, banyak_iterasi):
    mulai = time.time()
    populasi = [state_awal_acak(kendaraan, kapal) for _ in range(jumlah_populasi)]
    awal = max(populasi, key=lambda s: nilai(s, kendaraan))
    riwayat_maks, riwayat_rata = [], []

    for _ in range(banyak_iterasi):
        nilai_populasi = [nilai(s, kendaraan) for s in populasi]
        riwayat_maks.append(max(nilai_populasi))
        riwayat_rata.append(sum(nilai_populasi) / len(nilai_populasi))

        terbaik = max(populasi, key=lambda s: nilai(s, kendaraan))
        populasi_baru = [terbaik]
        while len(populasi_baru) < jumlah_populasi:
            ayah = seleksi(populasi, kendaraan)
            ibu = seleksi(populasi, kendaraan)
            anak = crossover(ayah, ibu, kendaraan, kapal)
            anak = mutasi(anak, kendaraan, kapal)
            populasi_baru.append(anak)
        populasi = populasi_baru

    nilai_populasi = [nilai(s, kendaraan) for s in populasi]
    riwayat_maks.append(max(nilai_populasi))
    riwayat_rata.append(sum(nilai_populasi) / len(nilai_populasi))
    akhir = max(populasi, key=lambda s: nilai(s, kendaraan))
    return {
        "awal": awal,
        "akhir": akhir,
        "nilai_akhir": nilai(akhir, kendaraan),
        "riwayat_maks": riwayat_maks,
        "riwayat_rata": riwayat_rata,
        "populasi": jumlah_populasi,
        "iterasi": banyak_iterasi,
        "durasi": time.time() - mulai,
    }