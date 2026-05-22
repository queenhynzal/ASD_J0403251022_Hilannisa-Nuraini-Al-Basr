# ======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
# ======================================================================================

# ======================================================================================
# Latihan 1 - Weighted Graph  dan Perhitungan Jalur 
# ======================================================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ======================================================================================
# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobot jalur A -> B -> D adalah 9
#
# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobot jalur A -> C -> D adalah 3
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur terpendek adalah A -> C -> D
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Karena shortest path ditentukan berdasarkan total bobot terkecil, bukan jumlah edge.
# ======================================================================================