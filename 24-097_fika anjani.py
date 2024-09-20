nama1 = "fika"
nama2 = "fara"
buku1 = "novel"
buku2 = "majalah"
alamat1 = "jl telang indah gang 3"
alamat2 = "jl telang indah gang 2"

print("suatu hari di sebuah toko buku")
print("fika : permisi apa boleh minta bantuannya?")
print("fara : oh iya tentu")

print("fika : letaknya" , buku1 , "dimana ya?")
print("fara : letaknya di rak bagian paling selatan")
print("fika : oh disana terimakasih ya")

print("fika : kalo boleh tanya siapa namamu?") 
print("fara : namaku" , nama2)
print("fika : kenalin nama aku" , nama1 , "salam kenal ya")

print("fara : iya btw kosmu dimana?")
print("fika : aku di" , alamat1 , "kamu dimana?")
print("fara : aku di" , alamat2 , "berhubung kita satu jalan boleh pulang bareng?")
jawab = input("masukkan jawaban")

if jawab == "boleh" :
    print("fika : ok kita pulang bareng")
else :
    print("maaf tidak bisa")
print("fika : tunggu sebentar aku mau bayar ke kasir dulu")
print("fara : ok")
print("mereka pun pulang bersama sambil berbincang bincang")