#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 5 - Latihan 3
# Latihan 3: Mencari Nilai Maksimum 
# ======================================================================================
 
def cari_maks(data, index=0): 
 
    # Base case 
    if index == len(data) - 1: 
        return data[index] 
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
 
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))


'''
=======================
DISKUSI DAN PENJELASAN
=======================
Program bekerja dengan memeriksa elemen dari depan ke belakang menggunakan rekursi.
Base case terjadi ketika index berada pada elemen terakhir.
Setiap recursive call mengembalikan nilai maksimum dari elemen-elemen setelahnya.
Saat proses kembali (unwinding), setiap elemen dibandingkan untuk menentukan nilai maksimum.
Hasil akhirnya adalah nilai terbesar dalam list.

'''