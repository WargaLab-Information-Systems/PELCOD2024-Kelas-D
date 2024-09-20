# Definisikan karakter
nama1 = "Adel"
nama2 = "Jesica"

# fungsi untuk dialog
print("Hallo, perkenalkan nama aku Adel, asalku dari mojokerto yang kotanya sangat indah itu")
print("Hallo,kalau nama aku Jesica, aku berasal dari Surabaya yang kotanya tidak kalah indah itu")
print(f"{nama2}: sekarang kamu tinggal dimana kok jauh banget kamu main sampai surabaya")
print(f"{nama1}: aku ngekos dimadura,karena kebetulan aku kuliah disitu")
print(f"{nama2}: {nama1} kalau boleh tau berapa umur kamu sekarang?")
umur_Adel = int(input(f"{nama1}: umurku sekarang berapa?"))
print(f"{nama2}: oh, jadi umurmu {umur_Adel} tahun.aku sekarang {umur_Adel + 2} tahun!")
print(f"{nama1}: wah, jadi kita selisih umur {2} tahun ya?")
selisih_umur = abs (umur_Adel - (umur_Adel + 2))
print(f"{nama2}: betul sekali! selisih umur kita adalah {selisih_umur} tahun.")
print(f"{nama1}: bagaimana kalau kita menghitung total umur kita?")
total_umur = umur_Adel + (umur_Adel + 2)
print(f"{nama2}: total umur kita adalah {total_umur} tahun.")

# cek jika total umur lebih dari 30
if total_umur > 30:
    print(f"{nama1}: wow, total umur kita lebih dari 30 tahun!")
else:
    print(f"{nama2}: kita masih muda, total umur kita kurang dari atau sama dengan 30 tahun.")

# fungsi untuk dialog
int = input(f"{nama2}: sekarang {nama1} lagi sibuk apa kesehariannya?")
kegiatan = input("kesibukanmu")
print(f"{nama2}: semangat ya {kegiatan}nya semoga berhasil")
print(f"{nama2}: kalau aku sibuknya kerja aja sih")
print(f"{nama1}: emang {nama2} kerja dimana?")
print(f"{nama2}: kerja di salah satu perusahaan di Surabaya dekat alun-alun itu loh")
print(f"{nama1}: oalah iya {nama2}")
print(f"{nama1}: oke deh kalau gitu aku mau balik dulu ya, see you!!")
print(f"{nama2}: see you {nama1} semoga berjumpa kembali")

# jalankan dialog