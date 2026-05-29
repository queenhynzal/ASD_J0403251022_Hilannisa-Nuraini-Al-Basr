# ======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================================================================
# ======================================================================================
# Latihan 1 - Memahami Konsep Spanning Tree 
# ======================================================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ======================================================================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki semua edge yang tersedia dan dapat mengandung cycle, sedangkan
#    spanning tree hanya menggunakan edge yang diperlukan untuk menghubungkan seluruh
#    node tanpa cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena cycle menyebabkan penggunaan edge berlebih sehingga koneksi menjadi kurang
#    efisien dan biaya dapat meningkat.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya membutuhkan n-1 edge untuk menghubungkan seluruh
#    node tanpa membentuk cycle.
# ======================================================================================