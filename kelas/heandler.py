from .usecase import UsecaseKelas
from flask import jsonify, request

class HandlerKelas:

    def getAll():
        return UsecaseKelas.getAll()

    def getSingle(request):
        kode = request.args.get("kode")
        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        return UsecaseKelas.getSingle(kode)

    def post(request):
        data = request.json
        kode_mahasiswa = data.get("kode_mahasiswa")
        kode_mk = data.get("kode_mk")
        tahun = data.get("tahun")
        semester = data.get("semester")

        if not kode_mahasiswa:
            return jsonify({"code": 400, "message": "Kode mahasiswa tidak boleh kosong"}), 400
        if not kode_mk:
            return jsonify({"code": 400, "message": "Kode matakuliah tidak boleh kosong"}), 400
        if not tahun:
            return jsonify({"code": 400, "message": "Tahun tidak boleh kosong"}), 400
        if not semester:
            return jsonify({"code": 400, "message": "Semester tidak boleh kosong"}), 400

        return UsecaseKelas.post(kode_mahasiswa, kode_mk, tahun, semester)

    def update(request):
        data = request.json
        id_kelas = data.get("kode")
        kode_mahasiswa = data.get("kode_mahasiswa")
        kode_mk = data.get("kode_mk")
        tahun = data.get("tahun")
        semester = data.get("semester")

        if not id_kelas:
            return jsonify({"code": 400, "message": "Kode kelas tidak boleh kosong"}), 400
        if not kode_mahasiswa:
            return jsonify({"code": 400, "message": "Kode mahasiswa tidak boleh kosong"}), 400
        if not kode_mk:
            return jsonify({"code": 400, "message": "Kode matakuliah tidak boleh kosong"}), 400
        if not tahun:
            return jsonify({"code": 400, "message": "Tahun tidak boleh kosong"}), 400
        if not semester:
            return jsonify({"code": 400, "message": "Semester tidak boleh kosong"}), 400
            
        return UsecaseKelas.update(id_kelas, kode_mahasiswa, kode_mk, tahun, semester)

    def delete(request):
        data = request.json
        kode = data.get("kode")
        if not kode:
            return jsonify({"code": 400, "message": "Kode tidak boleh kosong"}), 400
        return UsecaseKelas.delete(kode)
