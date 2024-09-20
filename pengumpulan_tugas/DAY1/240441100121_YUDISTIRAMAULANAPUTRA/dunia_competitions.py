import datetime

# karakter logika
class Character:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def ask_question(self, question, correct_answer):
        print(f"{self.name}: {question}")
        user_answer = input("Jawaban Elu: ")
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Bener bro! Skor lu sekarang bertambah 1.")
        else:
            print("Salah. Jawaban yang benar itu:", correct_answer)

# Main body function
def main():
    print("=== Kompetisi Pengetahuan Dunia ===")
    print("Hari ini, dua peserta akan bertanding.")
    
    # inisial karakter percakapan
    character1 = Character("Sakera")
    character2 = Character("Marlena")

    # pendefinisian daftar pertanyaan
    questions = [
        ("Sebutkan ibukota Indonesia?", "Jakarta"),
        ("Berapa hasil dari 5 + 4?", "9"),
        ("Siapa pencipta linux?", "Linus Torvalds"),
        ("Berapa hasil dari 20 / 2?", "10"),
    ]

    # prompt pertanyaan dan jawaban karakter
    for question, answer in questions:
        character1.ask_question(question, answer)
        character2.ask_question(question, answer)

    # print pada saat program berakhir
    print("\n=== Hasil Akhir ===")
    print(f"{character1.name} dapet skor: {character1.score}")
    print(f"{character2.name} dapet skor: {character2.score}")

    # segmen menentukan pemenang antar karakter
    if character1.score > character2.score:
        print(f"Selamat, {character1.name} telah memenangkan kompetisi!")
    elif character1.score < character2.score:
        print(f"Selamat, {character2.name} telah memenangkan kompetisi!")
    else:
        print("Kompetisi berakhir imbang!")

    # Tambahan untuk menampilkan tanggal dan waktu kompetisi berakhir
    end_time = datetime.datetime.now()
    print(f"Kompetisi berakhir pada: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()