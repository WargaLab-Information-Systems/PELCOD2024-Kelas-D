nama1 = "Rei"
nama2 = "Hyke"

print(f"Disuatu sekolah, dimana beberapa hari lagi akan ada ujian fisika.")
print(f"Ada dua orang sahabat yang merencanakan belajar bersama, yaitu : {nama1} dan {nama2}.")

nilai1 = 28
nilai2 = 20

print(f"{nama1}: Oy broo, bentar lagi ujian fisika nih, gw gak mau lagi kayak ujian fisika sebelumnya yang cuma dapet {nilai1} wkwkwk.")
print(f"{nama2}: iya nih gw lebih rendah dari lu cuy dapet {nilai2},")
respon = input("ayo kerumah buat belajar bareng nggak? ")

alamat = 'Jl. sudirman'
jarak = 2.5
uang1 = 300000

if respon=="ayo":
    print(f"{nama2}: okela, nanti malam kerumah gw!")
    print(f"{nama1}: hmmm, atau ke kafe di {alamat}, kafenya enak banget cuy tapi, jauh banget sekitar {jarak}km.")
    print(f"{nama2}: waduhnh jauh banget broo kerumah gw aja, {nama1}")
    print(f"{nama1}: siappp, lu mau gw beliin sesuatu nggk? uang gw lagi berlimpah nih, {uang1}")
    uang2 = int(input(f"{nama2}: Uang gua ada "))
    print(f"{nama1}: Owh, uang lu {uang2}, gabungin sama uang gw aja {nama2}, jadinya nanti {uang2 + uang1}.")
    print(f"{nama2}: lumayan lah itu, buat beli-beli biar energi kita terisi dan fokus belajarnya kita...")
    print(f"{nama1}: iya kalo belajar, kalo nggak...")
    print(f"{nama2}: makan-makan aja hehehe:)")

else:
    print(f"{nama2}: wah, yaudah deh...")
    print(f"{nama1}: lain kali aja bro, gw ada urusan...")
    print(f"{nama2}: okelaa broo..")
print("CERITA SELESAI")   
