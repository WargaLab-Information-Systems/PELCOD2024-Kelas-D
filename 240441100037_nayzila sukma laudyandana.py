print("SELAMAT DATANG DI PROGRAM SAYA")
# Karakter pertama: Rafi
nama_rafi = "Rafi"
umur_rafi = 25

# Karakter kedua: Yuli
nama_yuli = "Yuli"
umur_yuli = 23

# Dialog dimulai
print(f"{nama_rafi}: Hai {nama_yuli}, bagaimana kabarmu hari ini?")
jawaban_yuli = input(f"{nama_yuli}: ")

print(f"{nama_rafi}: Senang mendengarnya! Ngomong-ngomong, umurmu sekarang berapa, {nama_yuli}?")
umur_yuli_input = int(input(f"{nama_yuli}: Aku sekarang berumur {umur_yuli}, kamu berapa, Rafi? "))

# Menghitung apakah Rafi lebih tua atau lebih muda
if umur_rafi > umur_yuli:
    print(f"{nama_rafi}: Aku lebih tua darimu, selisih umur kita {umur_rafi - umur_yuli} tahun!")
else:
    print(f"{nama_rafi}: Ternyata aku lebih muda darimu, selisih umur kita {umur_yuli - umur_rafi} tahun!")

# Menghitung rata-rata umur
rata_rata_umur = (umur_rafi + umur_yuli)
print(f"{nama_rafi}: Jika kita gabungkan umur kita, rata-rata umur kita adalah {rata_rata_umur:.1f} tahun!")

# Rafi ingin membeli pensil dan penghapus
print(f"{nama_rafi}: Aku ingin membeli 2 pensil dan 1 penghapus. Harga pensil Rp5.000 dan harga penghapus Rp3.000. Berapa total yang harus kubayar?")
harga_pensil = 5000
harga_penghapus = 3000
jumlah_pensil = 2
jumlah_penghapus = 1

# Menghitung total harga
total_harga_pensil = harga_pensil * jumlah_pensil
total_harga_penghapus = harga_penghapus * jumlah_penghapus
total_harga_semua = total_harga_pensil + total_harga_penghapus

print(f"{nama_yuli}: Totalnya adalah Rp{total_harga_semua}. Apakah uangmu cukup, Rafi?")
uang_rafi = int(input(f"{nama_rafi}: Aku punya uang Rp "))

# Memeriksa apakah uang Rafi cukup menggunakan logika berbeda
if uang_rafi > total_harga_semua:
    sisa_uang = uang_rafi - total_harga_semua
    print(f"{nama_yuli}: Uangmu lebih dari cukup, sisa uangmu adalah Rp{sisa_uang}.")
elif uang_rafi == total_harga_semua:
    print(f"{nama_yuli}: Uangmu pas, kamu tidak akan punya sisa setelah membeli barang-barang ini.")
else:
    kekurangan = total_harga_semua - uang_rafi
    print(f"{nama_yuli}: Uangmu kurang Rp{kekurangan}. Kamu perlu mencari uang tambahan!")

# Cerita berakhir
print(f"{nama_rafi}: Terima kasih sudah menemani, Yuli! Sampai jumpa di lain waktu.")
print(f"{nama_yuli}: Sama-sama, Rafi! Sampai jumpa.")

print("TERIMAKASIH DAN SAMPAI JUMPA")