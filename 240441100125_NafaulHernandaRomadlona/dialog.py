# Program dialog antara dua karakter: Parjo dan Paijan

# Menyapa pengguna
print("Selamat datang di program dialog antara Parjo dan Paijan!")
print("Parjo: Halo jan, Hari ini kita akan belajar berhitung dengan matematika.")
print("Paijan: Hai Parjo Aku paling semangat kalo soal matematika!")
print("Parjo: yaudah lansung aku mulai yaa")
print("Paijan: okee")

# Mengambil input dari pengguna untuk angka
try:
    angka1 = int(input("Parjo: pilihlah angka dengan bijak : "))
    angka2 = int(input("Parjo: jangan yang selain angka yaaa!!!: "))
except ValueError:
    print("ANGKA WOII.")
    exit()


# Melakukan operasi aritmatika
jumlah = angka1 + angka2
selisih = angka1 - angka2
produk = angka1 * angka2

if angka2 != 0:
    pembagian = angka1 / angka2
else:
    pembagian = None

# Menampilkan hasil operasi aritmatika
print("\nParjo: Hasilnya gini cuy")
print(f"Parjo: Jumlah dari {angka1} dan {angka2} adalah {jumlah}.")
print(f"Parjo: Selisih antara {angka1} dan {angka2} adalah {selisih}.")
print(f"Parjo: Produk dari {angka1} dan {angka2} adalah {produk}.")

if pembagian is not None:
    print(f"Parjo: Pembagian dari {angka1} oleh {angka2} adalah {pembagian}.")
else:
    print("Parjo: bagi tuh gabisa pake 0.")
# Operasi logika
if angka1 > angka2:
    print(f"\nParjo: {angka1} lebih besar dari {angka2}.")
elif angka1 < angka2:
    print(f"Parjo: {angka1} lebih kecil dari {angka2}.")
else:
    print(f"Parjo: {angka1} sama dengan {angka2}.")

# Mengakhiri dialog
print("\nPaijan: Makasih cuy,membantu banget sih")
print("Parjo: Amannn sanz ae,gas mabar yok!")
print("Paijan:gasss")