from read import readAll
from update import update_data
from delete import delete_data
from create import creates
def getInput():
    nama = input("Nama: ")
    noTelfn = input("No Telfon: ")
    alamat = input("Alamat: ")
    return nama, noTelfn, alamat

print(creates(*getInput()))

# print(readAll())