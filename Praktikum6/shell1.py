#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Shell Sort : Ascending 
# ======================================================================================

def shellSort(data):
    sublistcount = len(data)//2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(data,startposition,sublistcount)

        print("After increments of size", sublistcount, "The list is", data)

        sublistcount = sublistcount // 2


def gapInsertionSort(data,start,gap):

    for i in range(start+gap,len(data),gap):

        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] > currentvalue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue


data = [54,26,93,17,77,31,44,55,20]

shellSort(data)

print(data)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi shellSort().
2. Nilai gap awal ditentukan dari setengah panjang list.
3. Data dibagi menjadi beberapa kelompok berdasarkan gap.
4. Setiap kelompok diurutkan menggunakan metode insertion sort
   melalui fungsi gapInsertionSort().
5. Setelah satu proses selesai, nilai gap diperkecil menjadi setengahnya.
6. Proses terus dilakukan sampai gap bernilai 0.
7. Setelah seluruh proses selesai, data akan terurut dari kecil ke besar.

================
OUTPUT PROGRAM
================
After increments of size 4 The list is [...]
After increments of size 2 The list is [...]
After increments of size 1 The list is [...]
[17, 20, 26, 31, 44, 54, 55, 77, 93]

'''