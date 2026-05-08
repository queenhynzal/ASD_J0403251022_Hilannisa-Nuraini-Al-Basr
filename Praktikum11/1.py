#=======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 1 - Membuat Adjacency Matrix 
# ======================================================================================

def create_graph(V, edges):
    # Membuat adjacency matrix berisi 0
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    # Menambahkan edge ke dalam matrix
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # karena graph undirected

    return matrix

# Jumlah vertex
V = 4

# Daftar edge sesuai graph
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3)
]

# Membuat adjacency matrix
matrix = create_graph(V, edges)

# Menampilkan adjacency matrix
print("Adjacency Matrix:\n")

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Penjelasan setiap baris
print("\nPenjelasan Setiap Baris:\n")

print("Baris 1 -> Node 0 terhubung ke node 1 dan node 2")
print("Baris 2 -> Node 1 terhubung ke node 0 dan node 2")
print("Baris 3 -> Node 2 terhubung ke node 0, node 1, dan node 3")
print("Baris 4 -> Node 3 hanya terhubung ke node 2")