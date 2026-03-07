#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Quick Sort : Descending 
# ======================================================================================

def quickSort(data):
    quickSortHelper(data,0,len(data)-1)

def quickSortHelper(data,first,last):
    if first < last:

        splitpoint = partition(data,first,last)

        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)

def partition(data,first,last):

    pivotvalue = data[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark


data = [54,26,93,17,77,31,44,55,20]

quickSort(data)

print(data)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi quickSort() untuk memulai proses pengurutan.
2. Fungsi quickSortHelper() digunakan untuk membagi data menjadi beberapa bagian.
3. Program memilih elemen pertama sebagai pivot.
4. Pointer leftmark bergerak dari kiri untuk mencari nilai yang lebih kecil dari pivot.
5. Pointer rightmark bergerak dari kanan untuk mencari nilai yang lebih besar dari pivot.
6. Jika kedua nilai ditemukan, maka keduanya ditukar.
7. Setelah proses pembagian selesai, pivot ditempatkan pada posisi yang benar.
8. Proses ini dilakukan secara rekursif sampai seluruh data terurut dari terbesar ke terkecil.

================
OUTPUT PROGRAM
================
[93, 77, 55, 54, 44, 31, 26, 20, 17]

'''