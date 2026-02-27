#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 5 - Materi 2
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ======================================================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)   # Fase masuk (stacking)
    hitung(n - 1)        # Pemanggilan rekursif
    print("Keluar:", n)  # Fase keluar (unwinding)

hitung(3)

'''
==========================
PENJELASAN ALUR PROGRAM
==========================
Urutan output:

Masuk: 3
Masuk: 2
Masuk: 1
Selesai
Keluar: 1
Keluar: 2
Keluar: 3

==================================
DISKUSI:
Mengapa 'Keluar' muncul terbalik?
==================================
Karena 'Keluar' dicetak saat fungsi SELESAI dipanggil.
Proses rekursi bekerja seperti tumpukan (stack):

- Masuk direkam dari atas ke bawah.
- Keluar muncul dari bawah ke atas.

Itulah sebabnya nilai 'Keluar' tampil terbalik.

'''