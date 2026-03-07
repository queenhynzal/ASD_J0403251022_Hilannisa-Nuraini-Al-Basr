#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Merge Sort : Descending
# ======================================================================================

def mergeSort(data):
    print("Splitting ", data)

    if len(data) > 1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]:
                data[k] = lefthalf[i]
                i = i + 1
            else:
                data[k] = righthalf[j]
                j = j + 1

            k = k + 1

        while i < len(lefthalf):
            data[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            data[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging ", data)


data = [54,26,93,17,77,31,44,55,20]

mergeSort(data)

print(data)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi mergeSort().
2. Data dibagi menjadi dua bagian yaitu lefthalf dan righthalf.
3. Fungsi mergeSort() dipanggil kembali secara rekursif
   untuk mengurutkan kedua bagian tersebut.
4. Setelah kedua bagian terurut, program menggabungkannya
   kembali menjadi satu list.
5. Pada saat penggabungan, elemen yang lebih besar
   dimasukkan terlebih dahulu sehingga menghasilkan
   urutan dari terbesar ke terkecil.
6. Proses terus dilakukan sampai seluruh data terurut.

================
OUTPUT PROGRAM
================
[93, 77, 55, 54, 44, 31, 26, 20, 17]

'''