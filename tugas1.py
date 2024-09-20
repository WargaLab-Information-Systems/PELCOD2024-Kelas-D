karakter = ["Adit", "Denis", "Jarwo"]
uang = 10000

print("Di sore hari yang cerah, Adit, Denis, dan Jarwo ingin bermain bersama-sama.")
print("Mereka kebingungan untuk menentukan lokasi bermain yang cocok dan nyaman.")
print("Apakah ada rekomendasi tempat bermain yang bagus disore hari?.")

lokasi = input("Masukkan lokasi cerita: ")

print(f"{karakter[0]}: Hai {karakter[1]} dan {karakter[2]}! Cuacanya cerah banget nih, ayo kita main di {lokasi}.")
print(f"{karakter[1]}: Wah, ide bagus tuh! Ngomong-ngomong, aku ada uang {uang} rupiah nih. Enaknya buat beli apa ya?")
print(f"{karakter[2]}: Hmm, gimana kalau kita beli es teh? Panas-panas gini pasti enak minum yang segar-segar.")
print(f"{karakter[0]}: Boleh tuh, tapi aku lagi ga bawa duit nih hehe")
print(f"{karakter[1]}: Santai kawan, aku yang traktir kalian")
print(f"{karakter[0]}: Wihh mantap tuh, terimakasih ya {karakter[1]}")
print(f"{karakter[2]}: wihh baik sekali. Terimakasih ya {karakter[1]}")

beli = int(input(f"{karakter[1]}: Masukkan jumlah es teh yang akan dibeli!!"))
harga = 2000
total = beli * harga
sisa = uang - total

print(f"{karakter[1]}: Oke, jadi kita beli {beli} es teh yaa. Harga satunya {harga} rupiah.")
print(f"{karakter[2]}: Berarti total belanjaan kita {total} rupiah.")
print(f"{karakter[0]}: Iya nih. Eh tapi tunggu, berarti sisa uang {karakter[1]} tinggal {sisa} rupiah dong?")
print(f"{karakter[1]}: Betul sekali! Tapi gapapa, yang penting kita bisa menikmati es teh di {lokasi}.")
print(f"{karakter[0]}: Bener banget! Yuk, kita berangkat ke {lokasi} sekarang.")
print(f"{karakter[1]}, {karakter[2]}: Gasss...")

print(f"Akhirnya mereka bertiga pergi ke {lokasi} untuk bermain bersama dan menikmati es teh mereka")