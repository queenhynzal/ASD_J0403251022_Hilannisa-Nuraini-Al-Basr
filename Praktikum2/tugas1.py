# ===============================================================
# Tugas Hands-on Modul 1
# Studi kasus sistem stok barang kantin (berbasis file .txt)
# ===============================================================

nama_file = r"F:\IPB\IPB Smester 2\File orang\hilann\ASD_J0403251022_Hilannisa-Nuraini-Al-Basr\Pertemuan2\stok_barang.txt"

# -----------------------------------------------------------
# Fungsi Membaca data dari File
# -----------------------------------------------------------

def baca_stok(nama_file):
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            kode, nama, stok = baris.split(",")
            stok_dict[kode] = {
                "nama": nama,
                "stok": int(stok)
            }
    return stok_dict

# -----------------------------------------------------------
# Fungsi Menampilkan semua data
# -----------------------------------------------------------

def tampil_stok(stok_dict):
    print("\n============ DAFTAR BARANG ============")
    print(f"| {'Kode Barang':<11} | {'Nama':<12} | {'Stok':>5} |")
    print("-" * 37)

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"| {kode:<11} | {nama:<12} | {stok:>5} |")

    print("-" * 37)

# -----------------------------------------------------------
# Fungsi Menyimpan data ke file
# -----------------------------------------------------------

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# -----------------------------------------------------------
# Fungsi Cari barang
# -----------------------------------------------------------

def cari_barang(stok_dict):
    kode = input("Masukan kode barang: ").strip().upper()

    if kode in stok_dict:
        print("\n===== DATA BARANG DITEMUKAN =====")
        print(f"Kode Barang : {kode}")
        print(f"Nama Barang : {stok_dict[kode]['nama']}")
        print(f"Jumlah Stok : {stok_dict[kode]['stok']}")
    else:
        print("Kode barang tidak ditemukan")

# -----------------------------------------------------------
# Fungsi Tambah barang baru
# -----------------------------------------------------------

def tambah_barang(stok_dict):
    kode = input("Masukan kode barang baru: ").strip().upper()

    if kode in stok_dict:
        print("Kode barang sudah ada")
        return

    nama = input("Masukan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif")
            return
    except ValueError:
        print("Stok harus berupa angka")
        return

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    simpan_stok(nama_file, stok_dict)
    print("Barang berhasil ditambahkan dan disimpan")

# -----------------------------------------------------------
# Fungsi Update stok
# -----------------------------------------------------------

def update_barang(stok_dict):
    # tampilkan data sebelum update
    print("\nDATA SEBELUM UPDATE")
    tampil_stok(stok_dict)

    kode = input("\nMasukan kode barang yang ingin diupdate: ").strip().upper()

    if kode not in stok_dict:
        print("Kode barang tidak ditemukan")
        return

    print("\nPilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Pilih (1/2): ").strip()

    try:
        jumlah = int(input("Masukan jumlah: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
    except ValueError:
        print("Jumlah harus berupa angka")
        return

    stok_lama = stok_dict[kode]["stok"]

    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_lama + jumlah
        print("Stok berhasil ditambahkan")

    elif pilihan == "2":
        if jumlah > stok_lama:
            print("Stok tidak mencukupi")
            return
        stok_dict[kode]["stok"] = stok_lama - jumlah
        print("Stok berhasil dikurangi")

    else:
        print("Pilihan tidak valid")
        return

    # simpan otomatis setelah update
    simpan_stok(nama_file, stok_dict)

    # tampilkan data setelah update
    print("\nDATA SETELAH UPDATE")
    tampil_stok(stok_dict)

# -----------------------------------------------------------
# Program Utama (Menu simpan ada saat update)
# -----------------------------------------------------------

def main():
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n============= MENU =============")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampil_stok(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)
            simpan_stok(nama_file, stok_barang)
            print("\nDATA SETELAH PENAMBAHAN BARANG")
            tampil_stok(stok_barang)

        elif pilihan == "4":
            update_barang(stok_barang)
            simpan_stok(nama_file, stok_barang)
            print("\nDATA TERKINI SETELAH UPDATE")
            tampil_stok(stok_barang)

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# -----------------------------------------------------------
# Jalankan Program
# -----------------------------------------------------------

if __name__ == "__main__":
    main()
