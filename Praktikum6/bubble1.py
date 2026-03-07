#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Sorting
# Bubble Sort : Ascending 
# ======================================================================================

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):

            # kondisi ascending (kecil ke besar)
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        passnum = passnum - 1


alist = [20,30,40,90,50,60,70,80,100,110]

shortBubbleSort(alist)

print(alist)


'''
================
ALUR PROGRAM
================
1. Program mendefinisikan fungsi shortBubbleSort().
2. Variabel exchanges digunakan untuk mengecek apakah terjadi pertukaran data.
3. Variabel passnum menentukan jumlah iterasi pengurutan.
4. Program membandingkan dua elemen yang bersebelahan pada list.
5. Jika elemen kiri lebih besar dari elemen kanan maka dilakukan pertukaran.
6. Proses ini terus dilakukan sampai tidak ada lagi pertukaran data.
7. Hasil pengurutan kemudian ditampilkan menggunakan print().

================
OUTPUT PROGRAM
================
[20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

'''