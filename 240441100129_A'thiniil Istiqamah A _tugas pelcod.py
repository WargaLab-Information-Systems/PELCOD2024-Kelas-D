nama1 ="Taehyung"
nama2 ="Jimin"
nama3 ="Jungkook"

print(f"{nama2}: Hai,{nama1} dan {nama3} apa kabar kalian semua")
print(f"{nama2}: Apakah pertemuan ini kita tidak akan membeli sesuatu?")
print(f"{nama3}: Boleh, bagaimana kita patungan saja untuk uangnya")
print(f"{nama1}: bagaimana kita beli baju samaan saja?")
print(f"{nama2}: boleh aku punya rekomendasi toko baju, dan harganya sekitar 200 ribu untuk tiga baju")
print(f"{nama3}: kita kumpulkan uangnya ")
print(f"{nama1}: uangku 70")
print(f"{nama2}: uangku juga 70")
print(f"{nama3}: uangku 75")

print(f"{nama2}: 70 + 75 + 70")
jawaban = int(input(f"{nama3}:"))
hasil = 70 + 75 + 70

if jawaban == hasil:
    print(f"{nama2} jawabanmu benar")
else: 
    print(f"{nama2} jawabanmu salah yang benar adalah {hasil}")

print(f"{nama3}: uang kita cukup untuk membeli baju kembar 3")
print(f"{nama2}: langsung saja kita kesana, menggunakan mobil {nama1}")
print(f"{nama1}: lets go!!")