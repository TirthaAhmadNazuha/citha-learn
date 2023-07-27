# menyambung string 

nama_pertama = 'Citha'
nama_tengah = 'Ahmad'
nama_akhir = 'Pauzi'

nama_lengkap = nama_pertama + ' ' + nama_tengah + ' ' + nama_akhir
print(nama_lengkap) 

# menghitung panjang string

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + ' = ' + str(panjang))

# mengecek komponen char/string di string

y = 'Cit'
status = y in nama_lengkap
print(y + ' ada di ' + nama_lengkap + ' = ' + str(status))

Y = 'cit'
status = Y not in nama_lengkap
print(Y + ' tidak ada di ' + nama_lengkap + ' = ' + str(status)) 

# mengulang string
print('ha ha'*10)

# indexing
print('index ke-0 : ' + nama_lengkap[1])
print('index ke-(-5) : ' + nama_lengkap[-5])
# cara mengambil str dr index 3 sampai 7
print('index ke-[3:7] : ' + nama_lengkap[3:7])
# harus menggunakan :2 (karna loncat 2)
print('index ke-[2,4,6,8,10] : ' + nama_lengkap[2:10:2])
