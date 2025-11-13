from flask import Flask

# Membuat instance Flask
app = Flask(__name__)

# Routing utama (halaman depan)
@app.route('/halo-world/')
def hello_world():
    return 'Hello, World!'

@app.route('/halo-dunia/')
def hello_dunia():
    return 'Hello, Dunia!'

@app.route('/get/')
def get():
    return 'ini get!'

@app.route('/get-single/')
def get_single():
    return 'Ini get single!'

@app.route('/post/')
def post():
    return 'Ini post!'

@app.route('/delete/')
def delete():
    return 'Ini delete!'

@app.route('/put/')
def put():
    return 'Ini put!'
    
# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
