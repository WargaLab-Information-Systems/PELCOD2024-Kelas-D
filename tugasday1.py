print ("Di suatu pagi yang cerah, berjalan-jalanlah seorang anak kecil sambil membawa sekeranjang apel.")
print ("Ia bersenandung riang, berlari kecil dengan sedikit melompat-lompat.")
print ("Hingga tanpa sengaja ia tersandung dan tidak bisa dihindari sekeranjang apelnya pun tumpah ruah di tanah. ")

#Menggunakan Variable
a = "Hansel"
print('"Kak', a, 'kakak tidak apa-apa, kan?"')

print ("Ternyata seorang gadis kecil mengikutinya dari belakang dengan membawa sekeranjang apel juga.")
print ("Ia tampak kewalahan dengan keranjang besar di tangannya.")

b = "Gretel"
print('"Aduhh, tidak apa-apa,', b,'. Hanya sedikit sakit, tapi..."')

print ("Ia menatap sedih apelnya.")
print ("Nasib, beberapa apel tenyata telah terinjak oleh kereta kuda yang baru saja lewat.")

print("\n")

#Menggunakan Tipe Data
print ("Apakah Hansel adalah kakak Gretel?")
boolean = 10 > 7
print (boolean)

#Menggunakan Operasi Logika 
umur_Hansel = True
umur_Gretel = not umur_Hansel
print ('Hansel adalah ayah Gretel,', umur_Gretel)
print ('Gretel adalah adik Hansel,', umur_Hansel)
print("\n")

nama = 'Hansel' 
print('"Bagaimana ini, Kak', nama, '. Apelnya beberapa ada yang rusak.",')

nama = 'Gretel'
apel=str(input('Apakah menurutmu apelnya banyak yang rusak?'))

#Menggunakan Operasi Logika (If Statement)
if apel=="ya" :
    print('"Kalau begitu kita kumpulkan dulu apel yang masih bagus."')
else :
    print('"Syukurlah, jadi tidak banyak apel yang terbuang. Kita kumpulkan saja dulu apel yang masih bagus"')

print("Mereka pun bersama-sama mengumpulkan apel yang masih bagus dan menaruhnya lagi di keranjang.")

nama = 'Gretel'
format_str = f'"Ada berapa apel di keranjangmu, {nama}?" ucap Hansel'
print(format_str)

#Menerima Input Pengguna
apel_gretel = int(input("Ada berapa apel di dalam keranjang Gretel?"))
print(f'"Masih lengkap seperti tadi, Kak. Ada {apel_gretel} apel. Apel di keranjang kakak ada berapa?"')
apel_hansel = int(input("Ada berapa apel di dalam keranjang Hansel?"))
print(f'"Syukurnya masih tersisa {apel_hansel} apel, Gretel."')

print('"Kalau dijumlahkan semua berarti punya kita ada berapa, Kak?"')

#menggunakan operasi aritmatika
jumlah = apel_gretel + apel_hansel
print(f'"Kalau dijumlahkan semua artinya ada {jumlah} apel, Gretel."')
print('"Kalau apel punya kakak dan Gretel dikalikan berarti ada berapa, Kak?"')
jumlah = apel_gretel * apel_hansel
print(f'"Nah, kalau dikalikan hasilnya ternyata {jumlah}, Gretel."')

print('"Ohh begitu ya, Kak. Ya sudah, Kak. Sekarang ayo kita pulang, Gretel ingin makan kue!" Gretel berseru semangat.')
print('Hansel hanya tertawa menanggapi dan menuruti adiknya untuk pulang.')
print('Mereka pun berjalan beriringan sambil menyanyi ringan dengan tak lupa membawa keranjang apel mereka.')
print('THE END~~')