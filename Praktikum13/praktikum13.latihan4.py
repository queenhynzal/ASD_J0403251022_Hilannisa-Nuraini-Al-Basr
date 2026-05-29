# ======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================================================================
# ======================================================================================
# Latihan 4 - Studi Kasus: Jaringan Kabel Antar Gedung
# ======================================================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'GedungC', 'GedungD'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (4, 'GedungA', 'GedungB'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)

# ======================================================================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge mana saja yang dipilih?
#    Edge yang dipilih adalah:
#    GedungC - GedungD (1)
#    GedungA - GedungC (2)
#    GedungB - GedungD (3)
#
# 3. Berapa total biaya minimum?
#    Total biaya minimum adalah 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST dapat menghubungkan seluruh gedung dengan biaya pemasangan kabel yang 
#    paling minimum tanpa membentuk cycle.
# ======================================================================================