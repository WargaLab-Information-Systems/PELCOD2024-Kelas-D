nama_1 = "Ali"
nama_2 = "Dani"

print("bertemunya Ali dan Dani di tempat cukur")

print(f"{nama_1}:Hai! nama kamu siapa?")
print(f"{nama_2}:Halo nama aku Dani, kamu namamnya siapa?")
print(f"{nama_1}:Halo Dani, aku Ali,")
print(f"{nama_2}:Halo Ali, salam kenal")

model_rambut1 = "Mullet"
model_rambut2 = "botak"
harga = 10000

print(f"{nama_1}:kamu mau potong rambut model apa")
print(f"{nama_2}:aku pengen potongan model {model_rambut1}")
print(f"{nama_1}:waduh keren tuh potongan model {model_rambut1}")
print(f"{nama_2}:iya pengen aja, kalo kamu?")
print(f"{nama_1}:karna aku anak teknik, aku mau potong model {model_rambut2}")
print(f"{nama_2}:hah, {model_rambut2}, HAHAHAHAHA")
print(f"{nama_1}:jangan ketawa dong hehe,")
print(f"{nama_2}:kamu tau gak biasanya harganya berapa")
print(f"{nama_1}:potongan apapun biasanya di sini cuma {harga}")
print(f"{nama_2}:oh ok, jadi kalo {model_rambut1} juga {harga}?")
print(f"{nama_1}:iya {harga} juga")

respon = input(f"{nama_2}:menurutmu potongan model {model_rambut1} cocok ke aku?")

if respon=="iya cocok":
    print(f"{nama_2}:oh baik aku senang deh")
    print(f"{nama_1}:WADUHHH Uang ku ketinggalan di rumah!")
    print(f"{nama_2}:WAHH Parah terus gimana dong")
    print(f"{nama_1}:kamu ada uang gak?")
    print(f"{nama_2}:ada nih uang, kamu butuh berapa?")

    hargaa = int(input(f"{nama_1}:aku butuhnya cuma "))

    print(f"{nama_2}:santai,kebetulan aku bawa uang lebih nih")
    print(f"{nama_1}:bolehkah aku pinjem dulu")
    print(f"{nama_2}:iya boleh kok ini pake aja")
    print(f"{nama_1}:wah makasih banyak yaa,kamu sangat baik")
    print(f"{nama_2}:iya sama sama santai aja")
else:
    print(f"{nama_1}:kayanya kurang cocok bro hehe,yaudah ya bro aku gajadi potong rambut nih di telpon suruh pulang")
    print(f"{nama_2}:aduhhh, yaudah semoga bertemu lagi di lain tempat,hati hati bro")
    print(f"{nama_1}:iya bro, yaudah ya duluan")
    print(f"{nama_2}:ok broo")
print("CERITA PUN TAMAT")

