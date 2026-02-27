#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 5 - Materi 1
# Contoh Rekursi 1: Faktorial 
# ======================================================================================

# Fungsi faktorial menggunakan rekursi
def faktorial(n):
    # Base case: berhenti jika n == 0
    if n == 0:
        return 1
    
    # Recursive case:
    # faktorial(n) = n * faktorial(n-1)
    return n * faktorial(n - 1)

# Contoh output
print(faktorial(5))  # Output: 120

'''
=========================
PENJELASAN ALUR PROGRAM
=========================
- faktorial(5) memanggil faktorial(4)
- faktorial(4) memanggil faktorial(3)
- faktorial(3) memanggil faktorial(2)
- faktorial(2) memanggil faktorial(1)
- faktorial(1) memanggil faktorial(0)
- faktorial(0) = 1 (BASE CASE TERCAPAI)

Saat proses kembali:
1 * 1 = 1
2 * 1 = 2
3 * 2 = 6
4 * 6 = 24
5 * 24 = 120

============
KESIMPULAN
============
Faktorial selalu memecah masalah menjadi lebih kecil sampai
base case tercapai, lalu hasil dikembalikan secara berurutan
ke atas (unwinding).

'''