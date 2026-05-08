#=======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
#=======================================================================================

# ======================================================================================
#  Praktikum 2- Membuat Adjacency List
# ======================================================================================

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Menampilkan adjacency list
print("Adjacency List:\n")

for node in graph:
    print(node, "->", graph[node])

# Penjelasan
print("\nPenjelasan:\n")
print("Node A terhubung ke node B dan C")
print("Node B terhubung ke node A dan D")
print("Node C terhubung ke node A dan D")
print("Node D terhubung ke node B dan C")