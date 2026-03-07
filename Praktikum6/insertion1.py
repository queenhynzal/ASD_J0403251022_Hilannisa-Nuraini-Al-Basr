#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Insertion Sort : Ascending 
# ======================================================================================

def insertionSort(data): 

    for index in range(1,len(data)):

        currentvalue = data[index]
        position = index

        while position > 0 and data[position-1] > currentvalue:
            data[position] = data[position-1]
            position = position-1

        data[position] = currentvalue


data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi insertionSort().
2. Data diambil satu per satu mulai dari elemen kedua.
3. Elemen tersebut dibandingkan dengan elemen sebelumnya.
4. Jika lebih kecil maka elemen digeser ke kanan.
5. Nilai dimasukkan ke posisi yang sesuai.
6. Proses diulang sampai semua data terurut.

================
OUTPUT PROGRAM
================
[17, 20, 26, 31, 44, 54, 55, 77, 93]

'''