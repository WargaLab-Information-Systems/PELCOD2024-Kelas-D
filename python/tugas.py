user = input("masukkan nama anda: ")

print("===================================")

teman = "Ujang"
penjual = "Pak Dudung"
Beras = 22000
UangUjang = 20000

print(f"Disaat {user} membeli roti di toko, ia bertemu {teman}")
kegiatan = input(f"{teman}: Halo {user}!, lagi beli apa? ")
print(f"{user}: Aku lagi {kegiatan}")
print(f"{teman}: Owalaah, lagi {kegiatan}, Eh {user}! Kamu ada uang lebih nggak?")
print(f"{user}: Ada, kenapa emangnya?")
print(f"Ini harga berasnya {Beras}, sementara uangku {UangUjang}")
print(f"{user}: Oke, boleh boleh")

kegiatan =  int(4000)
Total = int(kegiatan + Beras)

print(f"{user}: Jadi totalnya roti sama beras berapa pak")
print(f"{penjual}: Total semuanya jadi {Total} ribu")
sapa = input(f"{teman}: {user}, makasih ya ")
print(f"{user}: {sapa}") 

Hutang = (Beras - UangUjang)

print(f"{teman}: Berarti aku pinjam uangmu {Hutang} ribu ya, aku ganti besok")
tugas = input(f"{teman}: Eh {user}, tugas besok kamu sudah selesai? ")

if tugas=="sudah":
  print(f"{teman}: Wow sudah selesai ternyata, besok boleh pinjam ga?")
  print(f"{user}: Waduh.. gimana kalo aku bantuin aja nanti, daripada nyontek wkwk")
  print(f"{teman}: Okela boleh boleh")
  print(f"{user}: okee ntar malem aku kerumahmu")
  
else:
   print(f"{teman}: Waduh belum ternyata, kukira kamu sudah selesai..")
   print(f"{user}: Iya wkwk gimana nanti kita kerjain bareng bareng?")
   print(f"{teman}: Hmm boleh, gimana nanti kerjain di rumahku?")
   print(f"{user}: Ide bagus.. berarti aku nanti kerumah mu ya")
  
print(f"{teman}: Okee sampe ketemu nanti")
print("BERSAMBUNG")
print("===================================")

