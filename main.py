from flask import Flask, request
from mahasiswa.heandler import HandlerMahasiswa
from kelas.heandler import HandlerKelas
from matakuliah.heandler import HandlerMatakuliah

app = Flask(__name__)

######################
# API MAHASISWAs
######################

@app.route('/mahasiswa/get-all', methods=['GET'])
def mahasiswa_getAll():
    return HandlerMahasiswa.getAll()

@app.route('/mahasiswa/get-single', methods=['GET'])
def mahasiswa_getSingle():
    return HandlerMahasiswa.getSingle(request)

@app.route('/mahasiswa/post', methods=['POST'])
def mahasiswa_post():
    return HandlerMahasiswa.post(request)

@app.route('/mahasiswa/update', methods=['POST'])
def mahasiswa_update():
    return HandlerMahasiswa.update(request)

@app.route('/mahasiswa/delete', methods=['POST'])
def mahasiswa_delete():
    return HandlerMahasiswa.delete(request)


######################
# API KELAS
######################

@app.route('/kelas/get-all', methods=['GET'])
def kelas_getAll():
    return HandlerKelas.getAll()

@app.route('/kelas/get-single', methods=['GET'])
def kelas_getSingle():
    return HandlerKelas.getSingle(request)

@app.route('/kelas/post', methods=['POST'])
def kelas_post():
    return HandlerKelas.post(request)

@app.route('/kelas/update', methods=['POST'])
def kelas_update():
    return HandlerKelas.update(request)

@app.route('/kelas/delete', methods=['POST'])
def kelas_delete():
    return HandlerKelas.delete(request)


######################
# API MATAKULIAH
######################

@app.route('/matakuliah/get-all', methods=['GET'])
def mk_getAll():
    return HandlerMatakuliah.getAll()

@app.route('/matakuliah/get-single', methods=['GET'])
def mk_getSingle():
    return HandlerMatakuliah.getSingle(request)

@app.route('/matakuliah/post', methods=['POST'])
def mk_post():
    return HandlerMatakuliah.post(request)

@app.route('/matakuliah/update', methods=['POST'])
def mk_update():
    return HandlerMatakuliah.update(request)

@app.route('/matakuliah/delete', methods=['POST'])
def mk_delete():
    return HandlerMatakuliah.delete(request)


if __name__ == '__main__':
    app.run(debug=True)
