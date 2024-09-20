#Mendefenisikan sebuah karakter/nama orang
nama1="Yubi"
nama2="siska"

#Dialog pertama
print(f"{nama1} : Halo {nama2}, kamu apa kabar?")
print(f"{nama2} : Halo juga {nama1}, emm kabarku baik")

print(f"{nama1} :Eh, kemarin kamu datang ga ke pelatihan kemarin? (iya/ga) : ")
Jawaban=input(f"{nama2} : ")

if Jawaban.lower() == "iya" :
    print(f"{nama2} : Iya, aku datang ke pelatihan kemarin")
else:
    print(f"{nama2} : Ga, aku ga datang kemarin") 

print(f"{nama1} : Kalau aku, kemarin datang")
print(f"{nama1} : Eh btw berat badan kamu berapa ya?")

#input untuk mendapatkan data berat badam
berat_Yubi=int(input(f"{nama1} : Berat aku sekarang itu (Masukkan angka saja) : "))
berat_siska=int(input(f"{nama2} : Kalau berat aku sekarang (Masukkan saja angka) : "))
 
#Menghitung jumlah perbedaan berat badan
perbedaan_berat=abs(berat_Yubi- berat_siska)

#Penyeleksian kondisi operasi logika untuk perbedaan berat badan
if berat_Yubi>berat_siska:
    print(F"{nama1} : emm ternyata aku lebih berat {perbedaan_berat} dari kamu")
elif berat_Yubi<berat_siska:
    print(f"{nama1} : emm ternyata aku lebih ringan {perbedaan_berat} dari kamu")
else:
    print(f"{nama1} : Ehh ternyata berat kita sama {perbedaan_berat} ya")

# Operasi aritmatika lain
Total_berat=berat_Yubi+berat_siska
print(f"{nama2} : Berapa yah kalau berat badan kita berdua ditambahkan?")
print(f"{nama1} : Mmm sebentar aku mikir dulu!")
print(f"{nama1} : Beratku itu {berat_Yubi} + berat kamu {berat_siska} jadi... totalnya adalah")
print(f"{nama1} : {Total_berat}, jenius")

print(f"{nama2} : Hahaha kamu emang jenius")
print(f"{nama1} : Hahaha ga juga")
print(f"{nama1} : Itukan penjumlahan yang sangat mudah")
print(f"{nama2} : Bagi kamu mudah bagi aku susah")
print(f"{nama2} : Soalnya aku ga pinter matwmatikaya")