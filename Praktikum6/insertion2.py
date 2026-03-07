#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Insertion Sort : Descending 
# ======================================================================================

def insertionSort(alist):

    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        # kondisi dibalik agar urutan dari terbesar ke terkecil
        while position > 0 and alist[position-1] < currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi insertionSort().
2. Data diambil satu per satu mulai dari elemen kedua.
3. Elemen tersebut disimpan dalam variabel currentvalue.
4. Elemen dibandingkan dengan elemen sebelumnya pada list.
5. Jika elemen sebelumnya lebih kecil dari currentvalue,
   maka elemen tersebut digeser ke kanan.
6. Proses ini dilakukan sampai posisi yang tepat ditemukan.
7. Nilai currentvalue dimasukkan ke posisi yang sesuai.
8. Proses diulang sampai semua data terurut dari terbesar ke terkecil.

================
OUTPUT PROGRAM
================
[93, 77, 55, 54, 44, 31, 26, 20, 17]

'''