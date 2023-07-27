from mysql.connector import connect

conn = connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='mahasiswa',
)