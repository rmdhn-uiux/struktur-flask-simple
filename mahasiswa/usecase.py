from .repo import RepoData

class Usecase():

    # GET ALL
    def getAll():
        data = RepoData.getAllData()
        return {
            "code": 200,
            "message": "Berhasil mengambil semua data",
            "data": data
        }

    # GET SINGLE
    def getSingle(kode):
        data = RepoData.getSingle(kode)
        return {
            "code": 200,
            "message": "Berhasil mengambil data",
            "data": data
        }

    # INSERT (POST)
    def post(nama, nim, ket, jurusan):
        result = RepoData.insertData(nama, nim, ket, jurusan)
        return {
            "code": 200,
            "message": "Berhasil menambahkan data",
            "data": result
        }

    # UPDATE
    def update(kode, nama, nim, ket, jurusan):
        result = RepoData.updateData(kode, nama, nim, ket, jurusan)
        return {
            "code": 200,
            "message": "Berhasil memperbarui data",
            "data": result
        }

    # DELETE
    def delete(kode):
        result = RepoData.deleteData(kode)
        return {
            "code": 200,
            "message": "Berhasil menghapus data",
            "data": result
        }
