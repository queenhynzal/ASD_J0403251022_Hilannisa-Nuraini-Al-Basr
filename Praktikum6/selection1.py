#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Selection Sort : Ascending 
# ======================================================================================

def selectionSort(data):

    for fillslot in range(len(data)-1,0,-1):
        positionOfMax = 0

        for location in range(1,fillslot+1):
            if data[location] > data[positionOfMax]:
                positionOfMax = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [54,26,93,17,77,31,44,55,20]

selectionSort(data)

print(data)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi selectionSort().
2. Program melakukan perulangan untuk menentukan posisi akhir dari data.
3. Pada setiap iterasi, program mencari nilai terbesar dalam bagian list
   yang belum terurut.
4. Nilai terbesar tersebut disimpan pada variabel positionOfMax.
5. Setelah ditemukan, nilai terbesar ditukar (swap) dengan elemen
   pada posisi fillslot.
6. Proses ini diulang sampai seluruh data terurut dari kecil ke besar.

================
OUTPUT PROGRAM
================
[17, 20, 26, 31, 44, 54, 55, 77, 93]

'''