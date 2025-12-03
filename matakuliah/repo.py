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


class RepoMatakuliah:
    def getAll():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT kode_mk, nama_mk, sks FROM matakuliah ORDER BY kode_mk DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [dict(row) for row in rows]

    def getSingle(kode):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT  kode_mk, nama_mk, sks FROM matakuliah WHERE kode_mk = %s", (kode,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return dict(row) if row else None

    def insert(nama, sks):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO matakuliah (nama_mk, sks) VALUES (%s, %s) RETURNING kode_mk", (nama, sks))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return new_id

    def update(kode, nama, sks):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE matakuliah SET nama_mk=%s, sks=%s WHERE kode_mk=%s",
                    (nama, sks, kode))
        conn.commit()
        cur.close()
        conn.close()

    def delete(kode):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM matakuliah WHERE kode_mk=%s", (kode,))
        conn.commit()
        cur.close()
        conn.close()
