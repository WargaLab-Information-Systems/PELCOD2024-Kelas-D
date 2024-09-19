#Mendefinisikan sebuah karakter/nama orang
Karakter1="Arga"
Karakter2="Nia"

#Percakapan pertama
print(f"{Karakter1} : Hai, {Karakter2} Apa kabar nihh?")
print(f"{Karakter2} : Haii {Karakter1} alhamdulillah baik,kamu sendiri gimana kabarnya?")

print(f"{Karakter1} : Alhamdulillah untuk saat ini aku masih sehat!")
print(f"{Karakter1} : oh iya {Karakter2} sejauh ini gimana kuliahnya? (Baik/tidak) : ")
Jawaban=input(f"{Karakter2} : ")

if Jawaban.lower() == "Baik" :
    print(f"{Karakter2} : Sebenernya sedikit merasa salah jurusan sihh, tapi ya jalanin aja")
else:
    print(f"{Karakter2} : Tapi yaa begitulah, agak pusing karena ga bisa coding")

    print(f"{Karakter1} : Lah sama dong wkwkwk")
    print(f"{Karakter1} : Eh btw kemarin nilai ujianmu dapat berapa?")

#input untuk mendapatkan data nilai ujian
Nilai_Arga=int(input(f"{Karakter1} : Nilai aku kemarin ( )"))
Nilai_Nia=int(input(f"{Karakter2} : Kalau nilai aku kemarin ( )"))

#Menghitung jumlah perbedaan nilai
Perbedaan_Nilai =abs(Nilai_Nia - Nilai_Arga)

#Penyeleksian kondisi operasi logika untuk perbandingan nilai
if Nilai_Nia>Nilai_Arga:
    print(f"{Karakter1} : Ehh ternyata nilaiku lebih banyak {Perbedaan_Nilai} point dari kamu")
elif Nilai_Nia<Nilai_Arga:
    print(f"{Karakter1} : Ehh  nilaiku lebih banyak {Perbedaan_Nilai} point dari kamu")
else:
    print(f"{Karakter1} : Lah berarti nilai kita sama dong sama-sama {Nilai_Nia} point")

#Lanjut dengan operasi aritmatika lain
Total_Nilai = Nilai_Nia + Nilai_Arga
print(f"{Karakter2} : Kira-kira nilai kita berdua kalau ditambahkan jadi berapa ya?")
print(f"{Karakter1} : Bentar dulu loading nihh aku wkwkwk")
print(f"{Karakter1} : Nilaiku kan {Nilai_Arga} point + Nilai kamu {Nilai_Nia} point jadi totalnya")
print(f"{Karakter1} : {Total_Nilai} point dong")

print(f"{Karakter2} : Wahh pintar juga ternyata temenku satu ini wkwkwk")
print(f"{Karakter1} : orang aku hitung pakai kalkulator")
print(f"{Karakter2} : Wahahahahahaa pantes cepet, dahh deh aku pulang dulu yaa")
print(f"{Karakter1} : Iya deh, hati-hati yaa")

