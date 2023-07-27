from connction import conn

def readAll():
    cursor = conn.cursor()
    cursor.execute("SELECT nim, nama FROM mahasiswa")
    rows = cursor.fetchall()
    columns = ["nim", "nama"]
    result = [dict(zip(columns, row)) for row in rows]
    return result

def readById(id):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM mahasiswa WHERE nim = {id}')
    row = cursor.fetchone()
    columns = ["nim", "nama", "noTelp", 'alamat']
    result = dict(zip(columns, row))
    return result