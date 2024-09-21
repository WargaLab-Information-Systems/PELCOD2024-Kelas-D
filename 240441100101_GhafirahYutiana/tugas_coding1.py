# Dialog percakapan peminjaman buku di perpustakaan

# Data peminjaman
max_peminjaman_hari = 14  # Maksimal hari peminjaman
denda_per_hari = 5000     # Denda per hari keterlambatan dalam rupiah

# Input pengguna
nama_peminjam = input("Masukkan nama peminjam: ")
judul_buku = input("Masukkan judul buku yang dipinjam: ")
jumlah_hari_dipinjam = int(input("Berapa hari buku akan dipinjam? "))

# Operasi logika untuk mengecek apakah peminjaman lebih dari maksimal hari
if jumlah_hari_dipinjam > max_peminjaman_hari:
    hari_keterlambatan = jumlah_hari_dipinjam - max_peminjaman_hari
    total_denda = hari_keterlambatan * denda_per_hari
    print(f"\nPeminjaman melebihi batas maksimal {max_peminjaman_hari} hari.")
    print(f"Anda terlambat {hari_keterlambatan} hari dan harus membayar denda sebesar Rp{total_denda}.")
else:
    print(f"\nPeminjaman sah selama {jumlah_hari_dipinjam} hari. Tidak ada denda.")

# Percakapan antara petugas dan peminjam
print("\n===== Dialog Percakapan =====")
print(f"Petugas: 'Selamat siang, {nama_peminjam}. Buku yang ingin Anda pinjam adalah \"{judul_buku}\"?'")
print(f"{nama_peminjam}: 'Betul, saya ingin meminjam buku itu selama {jumlah_hari_dipinjam} hari.'")

# Operasi logika untuk memastikan apakah peminjaman diperbolehkan
if jumlah_hari_dipinjam <= max_peminjaman_hari:
    print(f"Petugas: 'Baik, buku \"{judul_buku}\" dapat dipinjam selama {jumlah_hari_dipinjam} hari. Jangan lupa untuk mengembalikannya tepat waktu.'")
else:
    print(f"Petugas: 'Maaf, Anda hanya dapat meminjam buku maksimal {max_peminjaman_hari} hari. Jika Anda ingin meminjam lebih lama, akan ada denda.'")
    print(f"{nama_peminjam}: 'Oh, baiklah. Saya akan memperhitungkannya.'")