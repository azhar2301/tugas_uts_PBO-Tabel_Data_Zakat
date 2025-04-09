import csv
import os
from datetime import date
import openpyxl

file_csv = "data_zakat.csv"
file_excel = "report_zakat.xlsx"
file_harga_beras = "harga_beras.csv"

def load_harga_beras():
    harga = []
    if os.path.exists(file_harga_beras):
        with open(file_harga_beras, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skip baris kosong
                    harga.append(int(row[0]))
    return harga

def simpan_harga_beras(harga):
    with open(file_harga_beras, mode="w", newline="") as file:
        writer = csv.writer(file)
        for h in harga:
            writer.writerow([h])

def tampilkan_harga_beras(harga_list):
    if not harga_list:
        print("Belum ada harga beras.")
    for i, h in enumerate(harga_list):
        print("Daftar Harga Beras:")
        print(f"({i+1}) Rp {h}")

def input_harga_beras(harga_list):
    harga = int(input("Masukkan Harga Beras Per-Kilo: "))
    harga_list.append(harga)
    print("Harga berhasil ditambahkan.")
    simpan_harga_beras(harga_list)

def simpan_data_csv(data):
    file_exists = os.path.exists(file_csv)
    with open(file_csv, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["NIK", "Nama", "Tanggal Bayar", "Harga Per-Kg", "Jumlah Kepala"])
        for row in data:
            writer.writerow(row)

def tampilkan_data():
    if not os.path.exists(file_csv):
        print("Belum ada data zakat.")
        return
    with open(file_csv, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def pembayaran_zakat(harga_list):
    tampilkan_harga_beras(harga_list)
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")
    id_beras = int(input("Pilih nomor harga beras: "))
    jumlah_kepala = int(input("Masukkan Jumlah Kepala: "))
    harga_total = harga_list[id_beras - 1] * jumlah_kepala
    print("Total yang harus dibayar: Rp", harga_total)
    bayar = int(input("Masukkan jumlah uang yang dibayar: "))
    kembali = bayar - harga_total
    print("Kembalian Anda: Rp", kembali)

    data = [(nik, nama, date.today(), harga_list[id_beras - 1], jumlah_kepala)]
    simpan_data_csv(data)

def export_to_excel():
    if not os.path.exists(file_csv):
        print("Tidak ada data untuk di-export.")
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Data Zakat"

    with open(file_csv, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            ws.append(row)

    wb.save(file_excel)
    print(f"Data berhasil diekspor ke {file_excel}")

def main():
    harga_beras = load_harga_beras()

    while True:
        print("""
=== Aplikasi Pembayaran Zakat ===
1. Tampilkan Harga Beras
2. Input Harga Beras
3. Tampilkan Data Zakat
4. Pembayaran Zakat
5. Export ke Excel
6. Keluar
""")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_harga_beras(harga_beras)
        elif pilihan == '2':
            input_harga_beras(harga_beras)
        elif pilihan == '3':
            tampilkan_data()
        elif pilihan == '4':
            if not harga_beras:
                print("Masukkan dulu harga beras (menu 2).")
            else:
                pembayaran_zakat(harga_beras)
        elif pilihan == '5':
            export_to_excel()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()