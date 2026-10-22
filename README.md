# IF3070_G59
Tugas Besar 1 IF3070 Dasar Inteligensi Artifisial

## Deskripsi Singkat
Repository ini berisi implementasi algoritma local search untuk menentukan solusi optimum

Algoritma yang diimplementasikan:
- Hill Climbing
- Simulated Annealing
- Genetic Algorithn

## Struktur Repository
```
IF3070_GXX_NamaKelompok/
├── data/
│   └── data_uji.json            data kapal dan kendaraan
├── src/
│   ├── main.py                  program utama, menjalankan seluruh eksperimen
│   ├── state.py                 representasi state, initial state acak, tampilan geladak
│   ├── objective.py             objective function dan pengecekan constraint
│   ├── langkah.py               langkah neighbor: swap, pindahkan, keluarkan, rotate
│   ├── hill_climbing.py         Steepest Ascent Hill-climbing
│   ├── simulated_annealing.py   Simulated Annealing
│   └── genetic_algorithm.py     Genetic Algorithm
├── output/                      hasil run (state awal/akhir dan grafik)
├── docs/                        laporan (pdf)
└── README.md
```

## Pembagian Tugas
Muhammad Dhafin Faidhulhaq (18223103) mengerjakan tugas besar 1 IF3070
