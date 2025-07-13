# 1
# print("Rafly Anggara Putra")

# 2
# name = "Rafly Anggara Putra"
# age = 20
# height = 5.6
# is_married = False
# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is Married?", is_married)

# 2
# name = input("Siapa Namamu? ")
# print("Selamat Datang, " + name + "!")

# 3
# x = 3
# y = 10
# print(x + y)
# print(y - x)
# print(x * y)
# print(y / x)
# print(y // x)
# print(y % x)
# print(y ** x)

# 4
# age = int(input("Berapa umur anda? "))
# if age >= 18:
#     print("Kamu sudah dewasa")
# elif age >= 13:
#     print("Kamu sudah remaja")
# else:
#     print("Kamu masih anak-anak")


# 5
# count = 0
# while count < 5:
#     print("Count is: ", count)
#     count += 1

# 6
# for count in range(5):
#     print("Count", count)

# 7
# test = ["Test 1", "Test 2", "Test 3"]
# for a in test:
#     print(a)
# print(test[0])
# test.append("Test 4")
# test[1] = "Test 5"
# print(test)

# 8
# def say_hello(nama_orang):
#     print("Hello, " + nama_orang + "!")
    
# say_hello("Rafly Anggara Putra")
# def perkalian(a,b):
#     return a * b

# hasil = perkalian(5,3)
# print("Result:", hasil)  # Output: 15

# 9
import random

secret_number = random.randint(1,10)
attempt = 3

print("Saya sedang memikirkan angka 1-10")

while attempt > 0:
    tebak = int(input("Tebak angka: "))
    if tebak == secret_number:
        print("Selamat tebakan anda benar!")
        break
    elif tebak < secret_number:
        print("Tebakan mu lebih kecil dibanding kan dengan angka yang saya pikirkan")
    else:
        print("Tebakan mu lebih besar dibandingkan dengan angka yang saya pikirkan")
    attempt -= 1