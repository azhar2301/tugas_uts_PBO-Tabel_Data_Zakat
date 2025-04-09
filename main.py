import pandas as pd
from datetime import date

# List untuk menyimpan data
harga_beras = []
data_zakat = []

# Menu menampilkan harga beras
def tampilkan_harga():
    if not harga_beras:
        print("Belum ada harga beras.")
    for i, harga in enumerate(harga_beras, 1):
        print("Daftar Harga Beras:")
        print(f"({i}, {harga})")

# Menu input harga beras
def input_harga():
    try:
        harga = int(input("Masukkan harga beras per kilo: "))
        harga_beras.append(harga)
        print("Harga berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

# Menampilkan data zakat
def tampilkan_data_zakat():
    if not data_zakat:
        print("Belum ada data zakat.")
        return
    print("\nData Pembayaran Zakat:")
    for item in data_zakat:
        print(item)

# Menu input pembayaran zakat
def pembayaran_zakat():
    if not harga_beras:
        print("Masukkan harga beras dulu sebelum input zakat.")
        return

    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")

    try:
        id_beras = int(input("Masukkan id_beras : "))
        jumlah_kepala = int(input("Masukkan jumlah kepala: "))

        harga_liter = harga_beras[id_beras - 1]
        total = harga_liter * jumlah_kepala
        print(f"Total yang harus dibayar: {total}")

        bayar = int(input("Masukkan jumlah bayar: "))
        kembali = bayar - total
        print(f"Kembalian: {kembali}")

        tanggal = date.today()
        data_zakat.append({
            "nik": nik,
            "nama": nama,
            "tanggal bayar": tanggal,
            "beras/liter": harga_liter,
            "jumlah": jumlah_kepala
        })

    except (ValueError, IndexError):
        print("Input tidak valid. Periksa kembali id_beras dan jumlah kepala.")

# Menu export ke Excel
def export_excel():
    if not data_zakat:
        print("Belum ada data untuk diekspor.")
        return

    df = pd.DataFrame(data_zakat)
    df.to_excel("reportzakat.xlsx", index=False)
    print("Data berhasil diekspor ke file 'reportzakat.xlsx'.")

# Menu utama
while True:
    print("\n=== Aplikasi Pembayaran Zakat ===")
    print("1. Tampilkan Harga Beras")
    print("2. Input Harga Beras")
    print("3. Tampilkan Data Zakat")
    print("4. Pembayaran Zakat")
    print("5. Export ke Excel")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_harga()
    elif pilihan == "2":
        input_harga()
    elif pilihan == "3":
        tampilkan_data_zakat()
    elif pilihan == "4":
        pembayaran_zakat()
    elif pilihan == "5":
        export_excel()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan aplikasi.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        