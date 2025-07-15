# 1
# angka = -20
# if angka > 10:
#     print("Angka lebih besar dari 10")
# elif angka == 10:
#     print("Angka sama dengan 10")
# else:
#     print("Angka kurang dari 10")

# 2
a = 10
b = 20
# if a > 11 and b < 25:
if a > 11 or b < 25:
    print("Kedua kondisi bernilai True")
else:
    print("Setidaknya salah satu atau keduanya bernilai False")
    
# 3
# angka = -20
# if angka > 10:
#     print("Angka lebih besar dari 10")
# elif angka == 10:
#     print("Angka sama dengan 10")
# elif angka == 5:
#     print("Angka sama dengan 5")
# else:
#     print("Angka kurang dari 10")


# 4
# Number Comparison Tool

# Step 1: Get user input for two number
num1 = int(input("Masukan Angka pertama: "))
num2 = int(input("Masukan Angka kedua: "))

# Step 2: Compare the numbers and print the result
if num1 == num2:
    print(f"{num1} sama dengan {num2}")
elif num1 > num2:
    print(f"{num1} lebih besar dari {num2}")
else:
    print(f"{num2} lebih besar dari {num1}")
    
# Step 3: Check if any number is zero
if num1 == 0 or num2 == 0:
    print("Setidaknya salah satu dari kedua angka adalah 0")
else:
    print("Keduanya tidak bernilai 0")