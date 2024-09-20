# Tugas Coding dengan Variabel dan Tipe Data

# Variabel
hari = "Senin pagi"
cuaca = "cerah"
lokasi = "kantin"
makanan_raja = "mie ayam"
harga_makanan_raja = 10000
makanan_ratu = "bakso"
harga_makanan_ratu = 15000
selisih_harga = harga_makanan_ratu - harga_makanan_raja
waktu_tersisa = 5 # dalam menit
raja_haus = True
raja_punya_uang = True
raja_beli_air = raja_haus and raja_punya_uang



# Output percakapan string
print(f"{hari} yang {cuaca}, Raja & Ratu sedang menikmati makanan {makanan_ratu} dan {makanan_raja} di {lokasi} sambil berbincang.")

print(f"Raja: Berapa harga {makanan_ratu}mu?")
print(f"Ratu: {harga_makanan_ratu}, dan {makanan_raja}mu?")
print(f"Raja: Mahal sekali, {makanan_raja}ku aja cuma {harga_makanan_raja}")
input(f"Ratu: berarti selisih berapa makanan kita?")
print(f"Raja: 5000, by the way aku mau beli air dulu, aku haus")
print(f"Ratu: oke,aku tunggu disini")

selisih = input ("berapakah selisih harga makanan raja dan ratu?")

print(f"apa raja membeli air? {raja_beli_air} ")





 