from connction import conn
from utils.generate_id import generate_id

def creates(nama, noTelp, alamat):
    try:
        nim = generate_id()
        cursor = conn.cursor()
        sql = "INSERT INTO mahasiswa VALUES (" + nim + ", %s, %s, %s)"
        data = (nama, noTelp, alamat)
        cursor.execute(sql, data)
        conn.commit()
        return { 'ok': True ,'message': 'Berhasil menambahkan data'}
    except Exception as e:
        conn.rollback()
        print(e)
        return { 'ok': False, 'data': None, 'message': e.__str__() }
    
    
