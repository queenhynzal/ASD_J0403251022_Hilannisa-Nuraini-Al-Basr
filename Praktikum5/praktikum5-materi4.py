#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 5 - Materi 4
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ======================================================================================

def biner(n, hasil=""):
    # Base case: panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0")
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1")

# Contoh
biner(3)

'''
==========================
PENJELASAN ALUR PROGRAM
==========================
Untuk n = 3, kombinasi yang dihasilkan:
000
001
010
011
100
101
110
111

Total kombinasi = 2^n = 8

'''