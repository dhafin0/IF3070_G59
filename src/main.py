import json
from objective import nilai
from hill_climbing import steepest_ascent
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm

with open("data/data_uji.json") as f:
    data = json.load(f)
kapal = data["kapal"]
kendaraan = data["kendaraan"]


def lapor(nama, hasil):
    teks = f"{nama:22} awal = {nilai(hasil['awal'], kendaraan):3}   akhir = {hasil['nilai_akhir']:3}   iterasi = {hasil['iterasi']:4}   durasi = {hasil['durasi']:.4f} s"
    if "stuck" in hasil:
        teks += f"   stuck = {hasil['stuck']}"
    if "populasi" in hasil:
        teks += f"   populasi = {hasil['populasi']}"
    print(teks)


for run in range(1, 4):
    lapor(f"steepest_run{run}", steepest_ascent(kendaraan, kapal))

for run in range(1, 4):
    lapor(f"sa_run{run}", simulated_annealing(kendaraan, kapal))

for populasi, iterasi in [(20, 10), (20, 30), (20, 60), (10, 30), (40, 30)]:
    for run in range(1, 4):
        lapor(f"ga_pop{populasi}_iter{iterasi}_run{run}", genetic_algorithm(kendaraan, kapal, populasi, iterasi))