from .repo import RepoKelas

class UsecaseKelas:

    def getAll():
        data = RepoKelas.getAll()
        return {"code": 200, "message": "Berhasil", "data": data}

    def getSingle(kode):
        data = RepoKelas.getSingle(kode)
        return {"code": 200, "message": "Berhasil", "data": data}

    def post(kode_mahasiswa, kode_mk, tahun, semester):
        new_id = RepoKelas.insert(kode_mahasiswa, kode_mk, tahun, semester)
        return {"code": 200, "message": "Berhasil tambah", "id": new_id}

    def update(id_kelas, kode_mahasiswa, kode_mk, tahun, semester):
        RepoKelas.update(id_kelas, kode_mahasiswa, kode_mk, tahun, semester)
        return {"code": 200, "message": "Berhasil update"}

    def delete(kode):
        RepoKelas.delete(kode)
        return {"code": 200, "message": "Berhasil hapus"}
