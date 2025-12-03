# Penjelasan Proyek Kampus Service

Proyek ini adalah sebuah layanan API (Application Programming Interface) yang dibangun menggunakan framework Flask dalam bahasa Python. API ini berfungsi untuk mengelola data akademik sederhana yang meliputi data mahasiswa, matakuliah, dan kelas.

Arsitektur proyek ini dirancang secara modular, memisahkan setiap entitas utama (Mahasiswa, Matakuliah, Kelas) ke dalam direktorinya masing-masing. Setiap direktori entitas memiliki struktur file yang sama, yang memisahkan tanggung jawab (separation of concerns) menjadi beberapa lapisan:

- **Handler (`heandler.py`)**: Lapisan ini bertanggung jawab untuk menangani request HTTP yang masuk. Fungsinya adalah menerima data dari request, melakukan validasi input sederhana (misalnya, memeriksa apakah ada data yang kosong), dan kemudian memanggil lapisan `usecase` untuk pemrosesan lebih lanjut. (Terdapat kesalahan penulisan nama file, seharusnya `handler.py`).

- **Usecase (`usecase.py`)**: Merupakan lapisan logika bisnis. Lapisan ini menjadi perantara antara `handler` dan `repo`. Fungsinya adalah mengkoordinasikan operasi yang perlu dilakukan. Misalnya, saat menambah data baru, `usecase` akan memanggil fungsi `insert` dari `repo` dan mengembalikan respons yang sesuai ke `handler`.

- **Repository (`repo.py`)**: Lapisan ini bertanggung jawab penuh atas interaksi dengan database. Semua query SQL untuk operasi CRUD (Create, Read, Update, Delete) didefinisikan di sini. Lapisan ini menggunakan library `psycopg2` untuk terhubung dan berinteraksi dengan database PostgreSQL.

- **Model (`model.py`)**: File ini tampaknya dimaksudkan untuk mendefinisikan struktur atau model data dari setiap entitas, meskipun saat ini isinya masih kosong.

## File Utama

### `main.py`
File ini adalah titik masuk utama dari aplikasi Flask. Di dalamnya, semua rute (endpoints) API didefinisikan. Setiap rute dipetakan ke fungsi yang sesuai di dalam file `heandler` dari setiap modul (mahasiswa, kelas, matakuliah).

### `database_schema.sql`
File ini berisi skrip SQL untuk membuat skema database di PostgreSQL. Ini mendefinisikan tiga tabel utama:
1.  **`mahasiswa`**: Menyimpan data mahasiswa (kode, nama, nim, keterangan, jurusan).
2.  **`matakuliah`**: Menyimpan data matakuliah (kode_mk, nama_mk, sks).
3.  **`kelas`**: Merupakan tabel relasi yang menghubungkan mahasiswa dengan matakuliah yang diambil dalam periode tahun dan semester tertentu.

File ini juga menyertakan beberapa data contoh (sample data) untuk setiap tabel.

## Modul/Entitas

### 1. Mahasiswa (`/mahasiswa`)
Modul ini mengelola data mahasiswa. API yang tersedia meliputi:
- `GET /mahasiswa/get-all`: Mengambil semua data mahasiswa.
- `GET /mahasiswa/get-single`: Mengambil satu data mahasiswa berdasarkan `kode`.
- `POST /mahasiswa/post`: Menambahkan data mahasiswa baru.
- `POST /mahasiswa/update`: Memperbarui data mahasiswa yang ada.
- `POST /mahasiswa/delete`: Menghapus data mahasiswa.

### 2. Matakuliah (`/matakuliah`)
Modul ini mengelola data matakuliah. API yang tersedia meliputi:
- `GET /matakuliah/get-all`: Mengambil semua data matakuliah.
- `GET /matakuliah/get-single`: Mengambil satu data matakuliah berdasarkan `kode`.
- `POST /matakuliah/post`: Menambahkan data matakuliah baru.
- `POST /matakuliah/update`: Memperbarui data matakuliah yang ada.
- `POST /matakuliah/delete`: Menghapus data matakuliah.

### 3. Kelas (`/kelas`)
Modul ini mengelola data kelas, yang merepresentasikan hubungan antara mahasiswa dan matakuliah. API yang tersedia meliputi:
- `GET /kelas/get-all`: Mengambil semua data kelas beserta detail mahasiswa dan matakuliah.
- `GET /kelas/get-single`: Mengambil satu data kelas berdasarkan `id_kelas`.
- `POST /kelas/post`: Menambahkan data kelas baru.
- `POST /kelas/update`: Memperbarui data kelas yang ada.
- `POST /kelas/delete`: Menghapus data kelas.

## Cara Menjalankan
1.  Pastikan database PostgreSQL sudah terpasang dan berjalan.
2.  Buat database (misalnya dengan nama `postgres` atau sesuaikan koneksi di file `repo.py`).
3.  Jalankan skrip `database_schema.sql` untuk membuat tabel dan mengisi data awal.
4.  Install semua dependensi Python yang dibutuhkan (seperti Flask dan psycopg2).
5.  Jalankan `main.py` untuk memulai server Flask.
