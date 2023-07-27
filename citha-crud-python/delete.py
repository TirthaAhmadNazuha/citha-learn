from connction import conn

def delete_data(nim):
    try: 
        query = f"DELETE FROM mahasiswa WHERE nim = {nim}"
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return { 'OK': True ,'message': 'Success'}
    except Exception as e:
        conn.rollback()
        print(e)
        return { 'ok': False, 'data': None, 'message': e.__str__() }
    

