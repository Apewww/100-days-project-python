# Introduction
# def function_name():
#     # Line Code
#     return value

# def add(a,b):
#     return a + b
# result = add(10, 20)
# print(result)

# def luas(tinggi, lebar):
#     return tinggi * lebar
# result = luas(20,30)
# print(result)

# def operasi_matematik(a, b):
#     pertambahan = a + b
#     pengurangan = a - b
#     perkalian = a * b
#     pembagian = a / b
#     return pertambahan, pengurangan, perkalian, pembagian

# result = operasi_matematik(10, 5)
# print(result)
# pertambahan,pengurangan, perkalian, pembagian = operasi_matematik(10,2)
# print(f"Pertambahan: {pertambahan}")
# print(f"Pengurangan: {pengurangan}")
# print(f"Perkalian: {perkalian}")
# print(f"Pembagian: {pembagian}")


# Simple Temperature Converter
# Step 1: Define the converter
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Step 2: Show the menu
def main_menu():
    print("\n------ Converter Temperature Menu ------") 
    print("1. Celcius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celcius & Kelvin")
    print("3. Kelvin to Celcius & Fahrenheit")
    print("4. Exit")
    
    
# Step 3: Main Program
while True:
    main_menu()
    
    try:
        choice = int(input("Pilih menu: "))
        if choice == 1:
            celcius = float(input("Masukkan suhu celcius: "))
            print(f"Celcius to fahrenheit: {celcius_to_fahrenheit(celcius):.2f}")
            print(f"Celcius to kelvin: {celcius_to_kelvin(celcius):.2f}")
        elif choice == 2:
            fahrenheit = float(input("Masukan suhu fahrenheit: "))
            print(f"Fahrenheit to celcius: {fahrenheit_to_celcius(fahrenheit):.2f}")
            print(f"Fahrenheit to Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}")
        elif choice == 3:
            kelvin = float(input("Masukan suhu kelvin: "))
            print(f"Kelvin to celcius: {kelvin_to_celcius(kelvin):.2f}")
            print(f"Kelvin to fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")
        elif choice == 4:
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Menu tidak valid, pilih menu (1-4)")
    except ValueError:
        print("Input tidak valid, pilih menu (1-4), atau suhu harus berupa angka")
        