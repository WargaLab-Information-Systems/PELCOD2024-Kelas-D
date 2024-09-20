# Karakter
print("Hai, Siapa namamu??")
karakter1 = (input(f"namaku.."))
karakter2 = "Fahri ngemplak"

# Fungsi untuk memulai dialog
def dialog():
    print(f"{karakter1}: Hai {karakter2}, berapa banyak permen yang kamu punya?")
    permen_k1 = 10
    permen_k2 = int(input(f"{karakter2}: Aku punya berapa ya? Coba hitung... (masukkan jumlah permen): "))

    print(f"{karakter1}: Hmm, aku punya {permen_k1} permen.")
    total_permen = permen_k2 + permen_k1

    print(f"{karakter1}: Jadi, kalau kita gabungkan, kita punya {total_permen} permen!")
    
    # Memeriksa apakah mereka punya cukup permen untuk dibagikan
    if total_permen > 15:
        print(f"{karakter2}: Wah, kita bisa bagi-bagi permen kepada teman-teman kita!")
    else:
        print(f"{karakter2}: Hmm, sepertinya jumlahnya kurang untuk dibagikan.")

    # Menanyakan apakah mereka mau berbagi
    mau_bagi = input(f"{karakter1}: Apakah kamu mau berbagi permen dengan teman-teman kita? (ya/tidak): ").lower()
    
    if mau_bagi == "ya":
        print(f"{karakter2}: Bagus! Mari kita bagi {total_permen} permen ini!")
        permen_per_orang = total_permen // 5  # Misalnya 5 teman
        print(f"Setiap orang akan mendapatkan {permen_per_orang} permen.")
    else:
        print(f"{karakter2}: Baiklah, kita nikmati sendiri saja permen ini!")

# Memulai cerita
dialog()
