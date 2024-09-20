# Program Simulasi Transaksi Jual Beli

# Menyapa pembeli
print("Penjual: Selamat datang di Trunojoyo Mart !!")
print("Pembeli: Terima kasih, saya ingin membeli beberapa barang.")

# Input barang dan harga
nama_barang = input("Penjual: Barang apa yang ingin Anda beli? ")
harga_barang = float(input(f"Penjual: Harga satuan dari {nama_barang} adalah Rp "))
jumlah_barang = int(input(f"Pembeli: Saya ingin membeli {nama_barang} sejumlah "))

# Menghitung total harga
total_harga = harga_barang * jumlah_barang

# Logika: Menentukan apakah pembeli mendapat diskon atau tidak
diskon = 0
if jumlah_barang > 5:
    diskon = (10/100) * total_harga  # Diskon 10% jika membeli lebih dari 5 barang
    print("Penjual: Anda mendapatkan diskon 10% karena membeli lebih dari 5 barang.")
else:
    print("Penjual: Anda tidak mendapatkan diskon.")

# Menghitung total akhir setelah diskon
total_setelah_diskon = total_harga - diskon

# Menampilkan total harga
print(f"Penjual: Total harga sebelum diskon adalah Rp {total_harga:.2f}")
print(f"Penjual: Total yang harus Anda bayar setelah diskon adalah Rp {total_setelah_diskon:.2f}")

# Input pembayaran
pembayaran = float(input("Pembeli: Saya akan membayar sebesar Rp "))

# Logika: Mengecek apakah pembayaran cukup
if pembayaran >= total_setelah_diskon:
    kembalian = pembayaran - total_setelah_diskon
    print(f"Penjual: Terima kasih! Berikut kembalian Anda sebesar Rp {kembalian:.2f}")
else:
    kekurangan = total_setelah_diskon - pembayaran
    print(f"Penjual: Maaf, uang Anda kurang sebesar Rp {kekurangan:.2f} , Silahkan Menyiapkan Uang anda Yang Kurang.")