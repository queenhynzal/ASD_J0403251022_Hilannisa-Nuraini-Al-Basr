#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

# ======================================================================================
# Praktikum 6 - Latihan
# Latihan : Soal Pengurutan
# ======================================================================================

# Data skor tes potensi akademik
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Mengurutkan data dari terbesar ke terkecil
data.sort(reverse=True)

print("Data setelah diurutkan:", data)

# Mengambil 5 nilai tertinggi
top5 = data[:5]

print("5 nilai tertinggi:", top5)

print("\nKandidat yang lolos seleksi:")
for i in range(len(top5)):
    print("Kandidat", i+1, ":", top5[i])


'''
=================
ALUR PROGRAM
=================
1. Program diawali dengan membuat sebuah list bernama data yang berisi skor
   tes potensi akademik para pelamar kerja:
   [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

2. Program kemudian mengurutkan data tersebut menggunakan fungsi
   sort(reverse=True). Fungsi sort() digunakan untuk mengurutkan elemen
   dalam list, sedangkan parameter reverse=True membuat urutan menjadi
   dari nilai terbesar ke nilai terkecil.

3. Setelah proses pengurutan selesai, urutan data menjadi:
   [98, 89, 76, 68, 57, 43, 33, 22, 12, 9]

4. Selanjutnya program mengambil lima nilai pertama dari list tersebut
   menggunakan teknik slicing dengan sintaks data[:5].

5. Lima elemen pertama ini merupakan lima nilai tertinggi dan disimpan
   dalam variabel top5.

6. Program kemudian menampilkan hasil pengurutan seluruh data serta
   lima nilai tertinggi yang menjadi kandidat yang lolos seleksi.

=================
OUTPUT PROGRAM
=================
Data setelah diurutkan: [98, 89, 76, 68, 57, 43, 33, 22, 12, 9]
5 nilai tertinggi: [98, 89, 76, 68, 57]

Kandidat yang lolos seleksi:
Kandidat 1 : 98
Kandidat 2 : 89
Kandidat 3 : 76
Kandidat 4 : 68
Kandidat 5 : 57

=================
KESIMPULAN
=================
Pak Budi meloloskan lima kandidat dengan skor tertinggi yaitu
98, 89, 76, 68, dan 57 karena mereka memiliki nilai paling tinggi
dibandingkan kandidat lainnya.

'''