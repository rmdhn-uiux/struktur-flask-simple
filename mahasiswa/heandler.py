from .usecase import Usecase
from flask import jsonify, request

class HandlerMahasiswa():

    # GET ALL
    def getAll():
        return Usecase.getAll()

    # GET SINGLE (pakai query param)
    def getSingle(request):
        kode = request.args.get('kode')
        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        return Usecase.getSingle(kode)

    # POST / Tambah Data
    def post(request):
        data = request.json
        nama = data.get("nama")
        nim = data.get("nim")
        ket = data.get("ket")
        jurusan = data.get("jurusan")

        if not nama:
            return jsonify({"code": 400, "message": "Nama tidak boleh kosong"}), 400
        if not nim:
            return jsonify({"code": 400, "message": "NIM tidak boleh kosong"}), 400
        if not jurusan:
            return jsonify({"code": 400, "message": "Jurusan tidak boleh kosong"}), 400

        return Usecase.post(nama, nim, ket, jurusan)

    # UPDATE / Ubah Data
    def update(request):
        data = request.json
        kode = data.get("kode")
        nama = data.get("nama")
        nim = data.get("nim")
        ket = data.get("ket")
        jurusan = data.get("jurusan")

        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        if not nama:
            return jsonify({"code": 400, "message": "Nama tidak boleh kosong"}), 400
        if not nim:
            return jsonify({"code": 400, "message": "NIM tidak boleh kosong"}), 400
        if not jurusan:
            return jsonify({"code": 400, "message": "Jurusan tidak boleh kosong"}), 400

        return Usecase.update(kode, nama, nim, ket, jurusan)

    # DELETE
    def delete(request):
        data = request.json
        kode = data.get("kode")

        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400

        return Usecase.delete(kode)
