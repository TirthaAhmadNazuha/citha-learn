# operator dalam bentuk metods

# merubah case dari string

# merubah ke upper case/lower case 

hello = 'brooKKss!'
print('ini tidak ada perubahan : ' + hello)
hello = hello.upper()
print('ini upper : ' + hello)
hello = hello.lower()
print('ini lower : ' + hello) 

# pengecekan dengan is methods 
# isalpha() --> mengecek semua huruf 
# isalnum() --> huruf dan angka 
# isdecimal() --> angka saja 
# isspace() --> spasi, tab, new line/ \n
# istitle() --> semua kata di mulai dengan huruf besar 


hello = 'WHATSAP BROK!!'
lower = hello.islower() #hasilnya bool jadi hrs mnggunakan str 
print(hello + ' apakah lower ? ' + str(lower))

hello = 'WHATSAP BROK!!'
lower = hello.isupper() #hasilnya bool jadi hrs mnggunakan str 
print(hello + ' apakah upper ? ' + str(lower))

## cek komponen startswith() dan endswith

cek_start = "Cek Toko Sebelah".startswith('Cek')
print("start : " + str(cek_start))

cek_end = "Cek Toko Sebrang".endswith("Sebrang")
print("end : " + str(cek_end))

#penggabuan komponen join() split()

pisah = ['aku', 'keberatan', 'dengan', 'putusan', 'kamu']
gabung = ' '.join(pisah)
print(gabung)

gabung = ['saya dengan berat hati menyampaikan ini bahwa kamu tidak lolos']
pisah = gabung[0].split(' ')
print(pisah)

gabung = "kamuakulucukamusukaaku"
print(gabung.split('aku'))