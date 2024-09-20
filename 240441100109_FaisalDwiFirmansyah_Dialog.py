nama1=input("Masukkan nama anda: ")
nama2=input("Masukkan nama anda: ")

print("\nPada suatu hari terdapat dua orang sahabat yang berkumpul di kantin kampus")
print(f"{nama1}: Eh, kamu sekarang ngekos dimana, {nama2}?")
print(f"{nama2}: Aku ngekos di daerah timur kampus, jaraknya sekitar 7km kalau dari sini, kalau jarak kosmu dari sini berapa, {nama1}?")
print(f"{nama1}: Jauh juga ya, kalau kosku lumayan dekat. Dari sini jaraknya cuma 4km")
print(f"{nama2}: Wah,beneran dekat itumah. Berarti selisih jarak antara kos kita berapa ya?")

jarak_kos1 = 7
jarak_kos2 = 4
selisih_jarak = jarak_kos1 - jarak_kos2

print(f"{nama1}: jadi cara menghitung selisih jarak antara kos kita adalah dengan cara {jarak_kos1} - {jarak_kos2}")
jawaban_nama2 = int(input(f"{nama2}: menurutku hasilnya adalah : "))

if jawaban_nama2 == selisih_jarak:
    print(f"{nama1}: wah, jawabanmu benar")
else:
    print(f"{nama1}: sayang sekali jawabanmu kurang tepat, harusnya {selisih_jarak}")

print(f"{nama2}: baiklah kalau begitu, bentar lagi masuk nih ayo balik ke kelas")
print(f"{nama1}: wokeeee")


