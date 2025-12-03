import psycopg2
import psycopg2.extras

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='08080808',
        port='5432'
    )
    return conn


class RepoData:

    # GET ALL
    def getAllData():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT kode, nama, nim, ket, jurusan FROM mahasiswa ORDER BY nama DESC;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [dict(row) for row in rows]
        return payload

    # GET SINGLE
    def getSingle(kode):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT kode, nama, nim, ket, jurusan FROM mahasiswa WHERE kode = %s", (kode,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is None:
            return {"message": "Data tidak ditemukan"}

        return dict(row)

    # INSERT (POST)
    def insertData(nama, nim, ket, jurusan):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO mahasiswa (nama, nim, ket, jurusan) VALUES (%s, %s, %s, %s) RETURNING kode;",
            (nama, nim, ket, jurusan)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return {"message": "Data berhasil ditambahkan", "kode": new_id}

    # UPDATE (PUT)
    def updateData(kode, nama, nim, ket, jurusan):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE mahasiswa SET nama=%s, nim=%s, ket=%s, jurusan=%s WHERE kode=%s;",
            (nama, nim, ket, jurusan, kode)
        )
        conn.commit()
        cur.close()
        conn.close()

        return {"message": "Data berhasil diperbarui"}

    # DELETE
    def deleteData(kode):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM mahasiswa WHERE kode=%s;", (kode,))
        conn.commit()
        cur.close()
        conn.close()

        return {"message": "Data berhasil dihapus"}
