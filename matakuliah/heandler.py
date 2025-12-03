from .usecase import UsecaseMatakuliah
from flask import jsonify, request

class HandlerMatakuliah:

    def getAll():
        return UsecaseMatakuliah.getAll()

    def getSingle(request):
        kode = request.args.get("kode")
        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        return UsecaseMatakuliah.getSingle(kode)

    def post(request):
        data = request.json
        nama = data.get("nama")
        sks = data.get("sks")
        if not nama:
            return jsonify({"code": 400, "message": "Nama tidak boleh kosong"}), 400
        if not sks:
            return jsonify({"code": 400, "message": "SKS tidak boleh kosong"}), 400
        return UsecaseMatakuliah.post(nama, sks)

    def update(request):
        data = request.json
        kode = data.get("kode")
        nama = data.get("nama")
        sks = data.get("sks")
        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        if not nama:
            return jsonify({"code": 400, "message": "Nama tidak boleh kosong"}), 400
        if not sks:
            return jsonify({"code": 400, "message": "SKS tidak boleh kosong"}), 400
        return UsecaseMatakuliah.update(kode, nama, sks)

    def delete(request):
        data = request.json
        kode = data.get("kode")
        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        return UsecaseMatakuliah.delete(kode)
