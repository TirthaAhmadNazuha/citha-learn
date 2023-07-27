from flask import Flask, render_template, request, redirect
from read import readAll, readById
from create import creates
from update import update_data
app = Flask(__name__)

@app.route('/mahasiswa', methods=['GET'])
def route_mahasiswa_all():
    return { 'mahasiswa': readAll() }


@app.route('/mahasiswa/<string:id>', methods=['GET'])
def route_mahasiswa_by_id(id):
    return { 'mahasiswa': readById(id) }

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    nama = request.form.get('nama')
    noTelp = request.form.get('noTelp')
    alamat = request.form.get('alamat')
    print(nama, noTelp, alamat)
    creates(nama, noTelp, alamat)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    nim = request.form.get('nim')
    nama = request.form.get('nama')
    noTelp = request.form.get('noTelp')
    alamat = request.form.get('alamat')
    update_data(nim, nama, noTelp, alamat)
    return redirect('/')


if __name__ == '__main__':
    app.run('localhost', 8080, True)