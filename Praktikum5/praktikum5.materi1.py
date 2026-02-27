#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 5 - Materi 1
# Rekursi: Faktorial
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

"""
Penjelasan Alur Program:
1. faktorial(5) memanggil faktorial(4)
2. faktorial(4) memanggil faktorial(3)
3. faktorial(3) memanggil faktorial(2)
4. faktorial(2) memanggil faktorial(1)
5. faktorial(1) memanggil faktorial(0)
6. Base case tercapai → mengembalikan 1
7. Mulai proses naik (unwinding):
   1 * 1 = 1
   2 * 1 = 2
   3 * 2 = 6
   4 * 6 = 24
   5 * 24 = 120
"""