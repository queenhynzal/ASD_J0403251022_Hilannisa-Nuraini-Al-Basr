# ======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================================================================
# ======================================================================================
# Latihan 5 - Tugas Mandiri: Buat Program MST dengan Kasus Baru 
# Kasus 2 : Jaringan Komputer
# ======================================================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'RouterC', 'RouterD'),
    (2, 'RouterA', 'RouterC'),
    (3, 'RouterA', 'RouterB'),
    (4, 'RouterB', 'RouterC'),
    (5, 'RouterB', 'RouterD')
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

print("Total bobot =", total_weight)

# ======================================================================================
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus yang dipilih adalah Jaringan Komputer.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    RouterC - RouterD (1)
#    RouterA - RouterC (2)
#    RouterA - RouterB (3)
#
# 4. Berapa total bobot MST?
#    Total bobot MST adalah 6.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut akan membentuk cycle atau memiliki bobot lebih besar tidak 
#    diperlukan dalam MST.
# ======================================================================================