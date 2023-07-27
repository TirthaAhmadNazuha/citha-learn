# # format string 

# # string 
# nama = "ASTA"
# format_str = f"Hello {nama}"
# print(format_str)
# # angka
# umur = 20.5 
# format_str = f"umur kamu : {umur}"
# print(format_str)
# # bolean
# boolean = True
# format_str = f"boolean {boolean}"
# print(format_str)
# # bilangan bulat (:d)
# angka = 23 
# format_str = f"bilangan bulat {angka:d}"
# print(format_str)
# # bilangan ribuan sd jutaan 
# angka = 1000000
# format_str = f"jutaan {angka:,}"
# print(format_str)
# # bilanga desimal ditambah (.angka dibelakng koma sama f/float)
# angka = 2023.919012
# format_str = f"desimal {angka:.4f}"
# print(format_str)
# # menampilkan landing zero
# angka = 2023.919012
# format_str = f"desimal {angka:011.4f}"
# print(format_str)
# # menampilkan tanda + dan - 
# minus = -10
# plus = +62.8551864437
# format_minus = f"minus = {minus:+d}"
# format_plus = f"plus = {plus:+.2f}"
# print(format_minus) 
# print(format_plus) 
# # memformat persen 
# persentase = 0.0880
# format_persen = f"persentase = {persentase:.2%}"
# print(format_persen)
# # melakukan operasi aritmatika di dalam placeholder/kurung kurawal/tempalete literal
# sales = 15650122
# adt = 329
# averageTransaction = f"AT = {sales/adt:,.0f}"
# print("sales = ", sales)
# print("adt = ", adt)
# print(averageTransaction)
# # format angka binary, octal, hexadesimal 
# angka = 2023
# format_binary = f"binary {bin(angka)}\n"
# format_octal = f"octal {oct(angka)}\n"
# format_hex = f"hex {hex(angka)}\n" 
# print(format_binary, format_octal, format_hex)

# string width dan multiline

nama = "Mugiwara Asta"
umur = 23
tinggi = 170.3 
beratBadan = 70

# string standart 
data_str = f"Nama = {nama}, Umur = {umur}, Tinggi = {tinggi} Berat Badan = {beratBadan} KG"
print(5*"="+"DATA STRING"+5*"=")
print(data_str)
# string multiline dengan menggunakan \n
data_str = f"Nama = {nama}, \nUmur = {umur}, \nTinggi = {tinggi} \nBerat Badan = {beratBadan} KG"
print(5*"="+"DATA STRING"+5*"=")
print(data_str)
# string multiline (""" kutip triple)
data_str = f"""
Nama = {nama}
Umur = {umur}
Tinggi = {tinggi}
Berat Badan = {beratBadan}
"""
print(5*"="+"DATA STRING"+5*"=")
print(data_str)
# merubah lebar
data_str = f"""
Nama        = {nama:>5}
Umur        = {umur:>5}
Tinggi      = {tinggi:>5}
Berat Badan = {beratBadan:>5}
"""
print(5*"="+"DATA STRING"+5*"=")
print(data_str)

