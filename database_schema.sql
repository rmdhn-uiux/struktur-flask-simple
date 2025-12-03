-- Create the database
-- This command should only be executed if the database does not exist.
-- If the database already exists, you can connect to it directly.
-- For example: psql -U your_user -d kampus

-- DROP DATABASE IF EXISTS kampus;
-- CREATE DATABASE kampus;

-- Use the database (this command is for psql client, not part of a transaction)
-- \c kampus;

-- Ensure uuid-ossp extension is available for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for Mahasiswa (Students)
CREATE TABLE mahasiswa (
    kode UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nama VARCHAR(255) NOT NULL,
    nim VARCHAR(255) UNIQUE NOT NULL,
    ket TEXT,
    jurusan VARCHAR(255)
);

-- Table for Matakuliah (Courses)
-- kode_mk remains VARCHAR as it is not an auto-generated numeric ID
CREATE TABLE matakuliah (
    kode_mk VARCHAR(255) PRIMARY KEY,
    nama_mk VARCHAR(255) NOT NULL,
    sks INTEGER
);

-- Table for Kelas (Classes)
CREATE TABLE kelas (
    id_kelas UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    kode_mahasiswa UUID REFERENCES mahasiswa(kode) ON DELETE CASCADE,
    kode_mk VARCHAR(255) REFERENCES matakuliah(kode_mk) ON DELETE CASCADE,
    tahun INTEGER,
    semester INTEGER
);

-- Insert sample data for Mahasiswa
INSERT INTO mahasiswa (nama, nim, ket, jurusan) VALUES
('Budi', '101', 'Mahasiswa aktif', 'Teknik Informatika'),
('Ani', '102', 'Mahasiswa aktif', 'Sistem Informasi'),
('Candra', '103', 'Cuti', 'Teknik Informatika');

-- Insert sample data for Matakuliah
INSERT INTO matakuliah (kode_mk, nama_mk, sks) VALUES
('IF101', 'Dasar Pemrograman', 3),
('SI101', 'Pengantar Sistem Informasi', 3),
('IF102', 'Struktur Data', 3);

-- Insert sample data for Kelas
-- You will need to get the actual UUIDs from the 'mahasiswa' table
-- after inserting the sample data above. For demonstration, we'll use
-- placeholders or assume some specific UUIDs. In a real scenario,
-- you would query for these UUIDs.
-- For now, I will use placeholder UUIDs. The user will need to adjust these.
INSERT INTO kelas (kode_mahasiswa, kode_mk, tahun, semester) VALUES
((SELECT kode FROM mahasiswa WHERE nim = '101'), 'IF101', 2023, 1),
((SELECT kode FROM mahasiswa WHERE nim = '102'), 'SI101', 2023, 1),
((SELECT kode FROM mahasiswa WHERE nim = '101'), 'IF102', 2024, 2);
