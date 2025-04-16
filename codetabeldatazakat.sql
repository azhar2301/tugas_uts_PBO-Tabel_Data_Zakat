CREATE DATABASE zakat;

USE zakat;

CREATE TABLE zakat_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    jenis_zakat VARCHAR(50) NOT NULL,
    jumlah DECIMAL(10,2) NOT NULL,
    tanggal DATE NOT NULL
);

CREATE TABLE master_beras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_beras VARCHAR(100) NOT NULL,
    harga_per_kg DECIMAL(10,2) NOT NULL
);

CREATE TABLE transaksi_zakat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_zakat INT NOT NULL,
    id_beras INT NOT NULL,
    jumlah_beras DECIMAL(10,2) NOT NULL,
    total_harga DECIMAL(10,2) NOT NULL,
    tanggal DATE NOT NULL,
    FOREIGN KEY (id_zakat) REFERENCES zakat_data(id),
    FOREIGN KEY (id_beras) REFERENCES master_beras(id)
);