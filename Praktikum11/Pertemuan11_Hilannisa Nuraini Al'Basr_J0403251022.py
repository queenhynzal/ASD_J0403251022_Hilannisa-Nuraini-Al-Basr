#=======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
#=======================================================================================

# ======================================================================================
#  Praktikum 4 – Studi Kasus Dunia Nyata 
# ======================================================================================

# Adjacency List
graph = {
    "Hilen": ["Nanuy", "Apiw"],
    "Nanuy": ["Apiw"],
    "Ahmad": ["Hilen"],
    "Rhei": ["Ahmad"],
    "Apiw": ["Ahmad"]
}

print("=== ADJACENCY LIST ===\n")

for node in graph:
    print(node, "->", graph[node])


# Adjacency Matrix
matrix = [
    [0,1,0,0,1],
    [0,0,0,0,1],
    [1,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0]
]

print("\n=== ADJACENCY MATRIX ===\n")

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Nama Node
print("\n=== NAMA NODE ===\n")
print("0 = Hilen")
print("1 = Nanuy")
print("2 = Ahmad")
print("3 = Rhei")
print("4 = Apiw")

# Hubungan Antar Node
print("\n=== HUBUNGAN ANTAR NODE ===\n")
print("Hilen -> Nanuy")
print("Hilen -> Apiw")
print("Nanuy -> Apiw")
print("Ahmad -> Hilen")
print("Rhei -> Ahmad")
print("Apiw -> Ahmad")