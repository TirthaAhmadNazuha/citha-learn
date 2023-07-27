from connction import conn
def update_data(nim, nama=None, noTelp=None, alamat=None):
    try:
        cursor = conn.cursor()
        query = 'UPDATE mahasiswa SET '
        where = f' WHERE `nim` = "{nim}"'
        if nama != None:
            query += f'`nama` = "{nama}" ,'
        if noTelp != None:
            query += f'`noTelp` = {noTelp} ,'
        if alamat!= None:
            query += f'`alamat` = "{alamat}" ,'
        sql = query[:-2] + where
        print('sql', sql)
        cursor.execute(sql)
        conn.commit()
        return { 'ok': True, 'data': None, 'message': 'Success' }
    except Exception as e:
        conn.rollback()
        print(e)
        return { 'ok': False, 'data': None, 'message': e.__str__() }

    

