nama_1 ="Tian"
nama_2 ="Alex"
jam ="2 jam "
kota_1 ="Bristol"
kota_2 ="London"
waktu = "06.00"

print(f"Liburan telah tiba inilah waktu untuk bersantai setelah bekerja siang dan malam tanpa jeda waktu, karena itu {nama_1} ingin mengajak {nama_2} untuk pergi berlibur agar tidak jenuh.")
print()

print(f"{nama_1}: \"kamu ada rencana liburan atau tidak? {nama_2} \"")
print(f"{nama_2}: \"tidak ada, aku bingung harus pergi kemana ada rekomendasi?\"")
print(f"{nama_1}: \"aku ada rekomendasi nih ke {kota_1}, tapi kamu mau ikut ngga hehe?\" ")
print(f"{nama_2}: \"wah ke {kota_1}? mau banget {nama_1} aku sudah lama tidak kesana.\"")
print()

print(f"{nama_1}: \"oya berapa jam untuk perjalanan ke {kota_1}, aku baru pertama kali.\"")
print(f"{nama_2}: \"hanya memakan waktu {jam} untuk kesana dari {kota_2} {nama_1}.\"")
print(f"{nama_1}: \"dengan waktu {jam} termasuk cepat juga ya.\"")
print(f"{nama_2}: \"iya, mau kapan kesana?\"")
print(f"{nama_1}: \"lusa bagaimana {nama_2} untuk sekarang kita persiapan.\"")
print(f"{nama_1}: \"dan juga lusa jam {waktu} ya! okeh sampai jumpa.\"" )
print(f"{nama_2}: \"sampai jumpa!\"")
print()

print(f"akhirnya {nama_1} dan {nama_2} pulang mempersiapkan barang-barang untuk pergi beribur lusa nanti.")
print(f"pertanyaan berapa jam jika dari {kota_1} ke {kota_2} pulang pergi?")

#ARITMATIKA

a = float(input("masukkan nilai 1 :"))
tanda = input("masukkan operasi matematika(+,-,*,/):")
b = float(input("masukkan nilai 2 :"))

if tanda == "+":
    print(f"{a} + {b} =", a + b)
elif tanda == "-":
    print(f"{a} - {b} =", a - b)
elif tanda == "*":
    print(f"{a} * {b} =", a * b) 
elif tanda == "/":
    print(f"{a} / {b} =", a / b)
else:
    print("input yang anda masukkan salah")
    
print(f"jadi jika {nama_1} dan {nama_2} pulang pergi maka mereka menempuh waktu 4 jam")
    