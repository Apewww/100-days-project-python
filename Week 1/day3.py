# 1
# nama = input("Siapa namamu? ")
# print(f"Halo {nama}!")

# 2
# angka = input("Masukan Angka: ")
# # angka = int(input("Masukan Angka: "))
# angka = int(angka)
# print(f"{angka} x 2 adalah {angka * 2}")
# angka = float(angka)
# print(f"{angka} x 2 adalah {angka * 2}")
# angka = str(angka)
# print(f"{angka} x 2 adalah {angka * 2}")

# 3
# angka1 = int(input("Masukan Angka-1: "))
# angka2 = int(input("Masukan Angka-2: "))
# pejumlahan = angka1 + angka2
# hasil = print(f"Penjumlahan dari {angka1} dan {angka2} adalah {pejumlahan}")

# 4
# a = 10
# b = 5
# print(f"Penjumlahan {a + b}")
# print(f"Pengurangan {a - b}")
# print(f"Perkalian {a * b}")
# print(f"Pembagian {a / b}")
# print(f"// {a // b}")
# print(f"Sisa Bagi {a % b}")
# print(f"** {a ** b}")


# Simple Calculator
 
# Step 1: Get user input for two numbeers
angka1 = float(input("Masukan Angka ke-1: "))
angka2 = float(input("Masukan Angka ke-2: "))

# Step 2: Perform arithmetic operation
penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2 if angka2 != 0 else "Tidak bisa dibagi dengan 0!"

# Step 3: Display Result
print(f"------ Kalkulator Sederhana------")
print(f"Penjumlahan {angka1} dan {angka2} adalah {penjumlahan}")
print(f"Pengurangan {angka1} dan {angka2} adalah {penjumlahan}")
print(f"Perkalian {angka1} dan {angka2} adalah {perkalian}")
if angka2 != 0:
    print(f"Pembagian {angka1} dan {angka2} adalah {pembagian}")
else:
    print(f"{pembagian}")