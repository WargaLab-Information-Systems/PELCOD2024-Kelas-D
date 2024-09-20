nama1 = "fauzul"
nama2 = "aby"

print("bertemu fauzul di kantin kampus")

print(f"{nama1}:Halo zul")
print(f"{nama2}:hai by")
print(f"{nama1}:sedang beli apa kamu by")
print(f"{nama2}:beli nasi zul")

nasi = "kuning"
harga = 15000
minum = "es teh"
harga = 5000
berat = 1.5

print(f"{nama1}:nasi apa?")
print(f"{nama2}:ini aku lagi beli nasi {nasi}")
print(f"{nama1}:kamu mau beli nasi juga kah by")
print(f"{nama2}:iya ini sama mau beli nasi {nasi} juga")
print(f"{nama1}:minumnya apa kamu by?")
print(f"{nama2}:aku si biasanya minum {minum}")
print(f"{nama1}:berapa harganya?")
print(f"{nama2}:harganya cuman {harga} zul")
print(f"{nama1}:oalah okedeh zul aku mau beli juga")
print(f"{nama2}: eh zul, btw boleh nanya ga")
print(f"{nama1}: ya, mau nanya apa by?")

print(f"{nama2}: disini toko yang jual beras {berat} liter murah dimana ya?")
print(f"{nama1}: itu di depan toko abel by ada, murah disana")
print(f"{nama2}: oke makasih zul infonya")
print(f"{nama1}: sama sama by")

uang1 = 20000
uang2 = 20000
total_uang = uang1 + uang2

print(f"{nama1}: eh by sini uangmu satuin aja sekalian sama uangku")
print(f"{nama2}: berapa totalnya semua emg zul")
print(f"{nama1}: {total_uang},semua totalnya sama uangku")
print(f"{nama2}: oke zul")

aby_suka_kulineran = True
fauzul_suka_nyore = True
budget_cukup = True
cuaca_cerah = False

if aby_suka_kulineran and fauzul_suka_nyore:
    print(f"{nama2}: eh zul kita kulineran yuk kayanya di depan kampus enak enak makanannya, baru kita nyore nanti")
    print(f"{nama1}: ide bagus tu by, tapi kita cari yang murah murah dulu")

    if cuaca_cerah and budget_cukup:
        print(f"{nama2}: cuacanya sekarang cerah zul dan uang kita cukup, ayo gas kita kulineran dulu")
        print(f"{nama1}: gasken, setelah itu kita bisa nyore")

    else:
        print(f"{nama2}: kayanya kita tunda dulu rencana kita zul")
        print(f"{nama1}: iya by, lebih baik kita tabung dulu untuk keperluan yang lain")

print("CERITA SELESAI")