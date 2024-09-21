nama1 = "Tina" #tipedata string
nama2 = "Sikin" #tipedata string
nama3 = "Mbak Kasir" #tipedata string
semester = 5 #tipedata integer
tahun = 2.5 #tipedata float
teman = True #tipedata boolean

print(f"{nama1} dan {nama2} mereka adalah mahasiswa semester {semester} yang berarti {tahun} tahun lagi mereka akan lulus. Suatu hari mereka keluar ruangan karena telah menyelesaiakan mata kuliah hari ini ")
print("apakah mereka berteman?", teman)
print(f"{nama1} : Halo, Sikin tugas hari ini banyak ya.")
print(f"{nama2} : Iya benar Tina, rasanya aku ingin meledak.")
print(f"{nama1} : Bagaimana kalau kita mengerjakan tugas bersama-sama?")
print(f"{nama2} : Boleh-boleh, bagaimana jika sekarang kita pergi ke cafe saja?")
print(f"{nama1} : Ayoo, gas.")       
print("mereka berdua berjalan menuju cafe yang paling dekat dengan kampus mereka.")
print(f"{nama2} : Tina kita pesen makan sama minum dulu yaa?")
print(f"{nama1} : Iya pesan saja.")

#operasi aritmatika 
matcha_sikin = int(input(f"{nama2} : aku mau matcha "))
matcha_tina = int(input(f"{nama1} : aku sama kayak kamu deh mau matcha  "))

total_minuman = matcha_sikin + matcha_tina

print(f"{nama2} : jadi, kami pesan {total_minuman} matcha ya.")
print(f"{nama1} : iya benar, aku mau pesan makan juga lapar cuy.")

cireng_tina = int(input(f"{nama1} : aku mau cireng "))
cireng_sikin = int(input(f"{nama2} : kelihatannya cireng enak mau deh  "))

total_makanan = cireng_tina + cireng_sikin

print(f"{nama3} : Jadi untuk pesanannya ada {total_minuman} matcha lalu untuk makanannya ada {total_makanan} cireng ya kak?.")
print(f"{nama1} : Iya kak, sudah benar.")
print(f"{nama3} : Baik kak mohon ditunggu.")

print(f"setelah itu {nama1} dan {nama2} mencari tempat duduk.")
print(f"{nama1} : Eh Sikin tadi sama dosennya diberi berapa soal tugasnya?")
print(f"{nama2} : Gatau lupa ya berapa.")
print(f"{nama1} : Bentar ya aku liat dulu.")
print(f"{nama2} : Okey.")

#operasi logika 
tugas_total = int(input(f"{nama1} : Tina tugasnya ada "))

if tugas_total % 2 == 0: 
    tugas_Tina = tugas_total // 2
    tugas_Sikin = tugas_total // 2
else: 
    tugas_Tina = tugas_total // 2
    tugas_Sikin = tugas_total - tugas_Tina

print(f"{nama1} : Kalau gitu, kamau ngerjain {tugas_Sikin} soal, aku ngerjain {tugas_Tina} soal.")
print(f"{nama2} : sipp setuju, oke kita kerjain sekarang.")
