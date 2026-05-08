#=======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 3 - Konversi Matrix ke List 
# ======================================================================================

# Adjacency Matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# Dictionary untuk adjacency list
graph = {}

# Konversi matrix ke adjacency list
for i in range(len(matrix)):
    neighbors = []

    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            neighbors.append(j)

    graph[i] = neighbors

# Menampilkan adjacency list
print("Adjacency List:\n")

for node in graph:
    print(node, "->", graph[node])

# Penjelasan
print("\nPenjelasan:\n")
print("Node 0 terhubung ke node 1 dan 2")
print("Node 1 terhubung ke node 0 dan 2")
print("Node 2 terhubung ke node 0, 1, dan 3")
print("Node 3 hanya terhubung ke node 2")