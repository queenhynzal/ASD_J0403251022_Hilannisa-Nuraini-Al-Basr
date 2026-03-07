#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Selection Sort : Descending 
# ======================================================================================

def selectionSort(data):

    for fillslot in range(len(data)-1,0,-1):
        positionOfMin = 0

        for location in range(1,fillslot+1):
            if data[location] < data[positionOfMin]:
                positionOfMin = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMin]
        data[positionOfMin] = temp


data = [54,26,93,17,77,31,44,55,20]

selectionSort(data)

print(data)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi selectionSort().
2. Program melakukan perulangan untuk menentukan posisi pengurutan.
3. Pada setiap iterasi, program mencari nilai terkecil dari data.
4. Nilai terkecil tersebut disimpan pada variabel positionOfMin.
5. Setelah ditemukan, nilai tersebut ditukar dengan elemen pada posisi fillslot.
6. Proses ini diulang sampai seluruh data terurut dari terbesar ke terkecil.

================
OUTPUT PROGRAM
================
[93, 77, 55, 54, 44, 31, 26, 20, 17]

'''