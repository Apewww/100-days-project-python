# Introduction
# def function_name():
#     print("Halo")    
# function_name()

# def sapa():
#     print("Halo, selamat datang di python")
# sapa()

# 3
# def sapa(nama):
#     print(f"Halo {nama}, selamat datang di python")
# sapa('Rafly')

# 4
# def tambah(a,b):
#     print(f"Pertambahan dari {a} dan {b} adalah {a+b}")    
# tambah(5,1)

# 5
# def perkalian(a,b):
#     return a * b
# hasil = perkalian(5,2)
# print(f"Hasil Perkalian adalah {hasil}")


# Basic Math Quiz Game
import random
# Step 1: Define the math question function
def generate_question():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return f"{num1} {operator} {num2}", answer
# Step 2: Main Quiz Game Function
def quiz_game():
    score = 0
    round = 5
    
    print("\n----- Selamat datang di Quiz Matematika -----")
    print("----- Anda harus menjawab pertanyaan dengan benar -----")
    
    for i in range(round):
        pertanyaan, jawaban = generate_question()
        print(f"\nPertanyaan ke {i+1} : {pertanyaan}")
        jawaban_peserta = int(input("Jawabanmu: "))
        
        if jawaban_peserta == jawaban:
            print("Jawban benar!")
            score += 1
        else:
            print(f"Jawaban salah! jawaban yang benar adalah {jawaban}") 
            
    print("\n---- Game Berakhir ----")
    if score == round:
        print("Selamat, kamu telah menjawab semua pertanyaan dengan benar")
    elif score >= round // 2:
        print("Kerja bagus, kamu melakukannya dengan baik")
    else:
        print("Tetap belajar, dan coba lagi lain kali!")
        
# Step 3: Run the Game
quiz_game()