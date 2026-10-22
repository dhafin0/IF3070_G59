import contextlib
import json
import os
import matplotlib.pyplot as plt
from state import show_geladak
from objective import nilai
from hill_climbing import steepest_ascent
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm

with open("data/data_uji.json") as f:
    data = json.load(f)
kapal = data["kapal"]
kendaraan = data["kendaraan"]
os.makedirs("output", exist_ok=True)


def simpan_state(nama, hasil):
    with open(f"output/{nama}.txt", "w") as f:
        with contextlib.redirect_stdout(f):
            print("INITIAL STATE, nilai =", nilai(hasil["awal"], kendaraan))
            show_geladak(hasil["awal"], kendaraan, kapal)
            print("Di luar:", [i for i, p in hasil["awal"].items() if p is None])
            print("\nFINAL STATE, nilai =", hasil["nilai_akhir"])
            show_geladak(hasil["akhir"], kendaraan, kapal)
            print("Di luar:", [i for i, p in hasil["akhir"].items() if p is None])
            print("\nIterasi :", hasil["iterasi"])
            print("Durasi  :", round(hasil["durasi"], 4), "detik")
            if "stuck" in hasil:
                print("Stuck   :", hasil["stuck"])
            if "populasi" in hasil:
                print("Populasi:", hasil["populasi"])


def simpan_grafik(nama, judul, garis):
    plt.figure(figsize=(8, 4))
    for label, data_y in garis.items():
        plt.plot(data_y, label=label)
    plt.xlabel("iterasi")
    plt.ylabel("nilai objective")
    plt.title(judul)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"output/{nama}.png")
    plt.close()


def simpan_grafik_probabilitas(nama, judul, probabilitas):
    plt.figure(figsize=(8, 4))
    plt.scatter([i for i, p in probabilitas], [p for i, p in probabilitas], s=4)
    plt.xlabel("iterasi")
    plt.ylabel("e^(dE/T)")
    plt.title(judul)
    plt.tight_layout()
    plt.savefig(f"output/{nama}.png")
    plt.close()


def lapor(nama, hasil):
    teks = f"{nama:22} nilai = {hasil['nilai_akhir']:3}   iterasi = {hasil['iterasi']:4}   durasi = {hasil['durasi']:.3f} s"
    if "stuck" in hasil:
        teks += f"   stuck = {hasil['stuck']}"
    print(teks)


for run in range(1, 4):
    nama = f"steepest_run{run}"
    hasil = steepest_ascent(kendaraan, kapal)
    simpan_state(nama, hasil)
    simpan_grafik(nama, f"Steepest Ascent - run {run}", {"nilai": hasil["riwayat"]})
    lapor(nama, hasil)

for run in range(1, 4):
    nama = f"sa_run{run}"
    hasil = simulated_annealing(kendaraan, kapal)
    simpan_state(nama, hasil)
    simpan_grafik(nama, f"Simulated Annealing - run {run}", {"nilai": hasil["riwayat"]})
    simpan_grafik_probabilitas(nama + "_probabilitas", f"e^(dE/T) - run {run}", hasil["probabilitas"])
    lapor(nama, hasil)

konfigurasi = [(20, 10), (20, 30), (20, 60), (10, 30), (40, 30)]
for populasi, iterasi in konfigurasi:
    for run in range(1, 4):
        nama = f"ga_pop{populasi}_iter{iterasi}_run{run}"
        hasil = genetic_algorithm(kendaraan, kapal, populasi, iterasi)
        simpan_state(nama, hasil)
        simpan_grafik(nama, f"GA populasi {populasi}, iterasi {iterasi} - run {run}",
                      {"maksimum": hasil["riwayat_maks"], "rata-rata": hasil["riwayat_rata"]})
        lapor(nama, hasil)