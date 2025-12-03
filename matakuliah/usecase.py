from .repo import RepoMatakuliah

class UsecaseMatakuliah:

    def getAll():
        data = RepoMatakuliah.getAll()
        return {"code": 200, "message": "Berhasil", "data": data}

    def getSingle(kode):
        data = RepoMatakuliah.getSingle(kode)
        return {"code": 200, "message": "Berhasil", "data": data}

    def post(nama, sks):
        new_id = RepoMatakuliah.insert(nama, sks)
        return {"code": 200, "message": "Berhasil", "id": new_id}

    def update(kode, nama, sks):
        RepoMatakuliah.update(kode, nama, sks)
        return {"code": 200, "message": "Berhasil update"}

    def delete(kode):
        RepoMatakuliah.delete(kode)
        return {"code": 200, "message": "Berhasil hapus"}
