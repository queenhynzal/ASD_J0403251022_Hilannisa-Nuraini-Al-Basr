#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 5 - Materi 3
# Contoh Rekursi 3: Menjumlahkan Elemen List 
# ======================================================================================

def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0

    # Recursive case: jumlah elemen sekarang + elemen berikutnya
    return data[index] + jumlah_list(data, index + 1)

# Contoh penggunaan
print(jumlah_list([2, 4, 6, 8]))  # Output: 20

'''
==========================
PENJELASAN ALUR PROGRAM
==========================
data = [2, 4, 6, 8]

Proses rekursi:
index 0 → 2 + (rekursi index 1)
index 1 → 4 + (rekursi index 2)
index 2 → 6 + (rekursi index 3)
index 3 → 8 + (rekursi index 4)
index 4 → base case → 0

Total = 2 + 4 + 6 + 8 = 20

'''