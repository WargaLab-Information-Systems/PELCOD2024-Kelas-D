orang_1 = "Adib"
orang_2 = "Akbar"
orang_3 = "mba kasir"

harga_bakmie_komplit_jumbo = 29000
harga_mie_yamin_komplit = 27000
uang_akbar = 100000


print( f"{orang_2}: Haloo Adib, kamu ada rekomendasi menu di kedai bakmie saudagar ini tidak?")
print( f"{orang_1}: Hii Abar! Ada nihh, karna kamu yang mau traktir hari ini, jadi yang pilih menunya aku aja.")
print( f"{orang_2}: Jadi apa menu pilihanmu dib?")
print( f"{orang_1}: Aku yang Bakmie Komplit Jumbo dan kau Mie Yamin Komplit")
print( f"{orang_2}: Untuk seporsi bakmie juga mie yamin nya berapa harganya Mba?")
print( f"{orang_3}: Harga Bakmie Komplit Jumbonya Rp.{harga_bakmie_komplit_jumbo} juga Harga Mie Yamin Rp.{harga_mie_yamin_komplit}")

total_harga_makanan = harga_bakmie_komplit_jumbo + harga_mie_yamin_komplit
sisa_uang_akbar = uang_akbar - total_harga_makanan

print( f"{orang_3}: Mau pembayaran cash atau debit kak?")
print( f"{orang_2}: Cash mba.")
print( f"{orang_3}: Baik, uangnya Rp.{uang_akbar} ya kak.")
print( f"{orang_3}: Totalnya jadi Rp.{total_harga_makanan} ini untuk kembaliannya Rp.{sisa_uang_akbar},Terima kasih.")