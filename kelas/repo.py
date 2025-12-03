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


class RepoKelas:

    # GET ALL
    def getAll():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT 
                k.id_kelas,
                m.kode AS kode_mahasiswa,
                m.nama AS nama_mahasiswa,
                mk.kode_mk,
                mk.nama_mk,
                k.tahun,
                k.semester
            FROM kelas k
            JOIN mahasiswa m ON k.kode_mahasiswa = m.kode
            JOIN matakuliah mk ON k.kode_mk = mk.kode_mk
            ORDER BY k.id_kelas DESC
        """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [dict(row) for row in rows]

    # GET SINGLE
    def getSingle(id_kelas):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT 
                k.id_kelas,
                m.kode AS kode_mahasiswa,
                m.nama AS nama_mahasiswa,
                mk.kode_mk,
                mk.nama_mk,
                k.tahun,
                k.semester
            FROM kelas k
            JOIN mahasiswa m ON k.kode_mahasiswa = m.kode
            JOIN matakuliah mk ON k.kode_mk = mk.kode_mk
            WHERE k.id_kelas = %s
        """, (id_kelas,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return dict(row) if row else None

    # INSERT
    def insert(kode_mahasiswa, kode_mk, tahun, semester):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO kelas (kode_mahasiswa, kode_mk, tahun, semester)
            VALUES (%s, %s, %s, %s)
            RETURNING id_kelas
        """, (kode_mahasiswa, kode_mk, tahun, semester))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return new_id

    # UPDATE
    def update(id_kelas, kode_mahasiswa, kode_mk, tahun, semester):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE kelas 
            SET kode_mahasiswa=%s, kode_mk=%s, tahun=%s, semester=%s 
            WHERE id_kelas=%s
        """, (kode_mahasiswa, kode_mk, tahun, semester, id_kelas))
        conn.commit()
        cur.close()
        conn.close()

    # DELETE
    def delete(id_kelas):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM kelas WHERE id_kelas=%s", (id_kelas,))
        conn.commit()
        cur.close()
        conn.close()
