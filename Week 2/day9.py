# Introduction
# my_tupple = (1, 2, 3)

# fruits = ("apple", "banana", "cherry")
# print(fruits[0])

# print(fruits[-1])

coordinates = (10, 20, 30)
x, y, z = coordinates

# print(x)
# print(y)
# print(z)

# fruits = ("pisang", "apel", "durian")
# print(len(fruits))

# print(fruits + ("nanas",))

# my_set = {1, 2, 3}

# ingredients = {"sugar", "butter", "flour"}
# print(ingredients)

# ingredients.add("eggs")
# ingredients.remove("flour")
# print(ingredients)

# set_a = {"sugar", "butter", "flour"}
# set_b = {"sugar", "eggs"}

# print(set_a | set_b) # Gabungan
# print(set_a & set_b) # Irisan
# print(set_a - set_b) # Perbedaan


# Ingredient Checker
# Step 1: Define the recipe ingredients
recipe_ingredients = {"eggs", "milk", "flour", "butter", "sugar"}

# Step 2: Get user input for available ingredients
user_input = input("Masukan bahan yang kamu punya (pisahkan dengan ,): ")
user_ingredients = set(user_input.split(", "))

# Step 3: Compare the ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# Step 4: Display Result
print("\n------ Hasil Pengecekan Bahan ------")
if missing_ingredients:
    print(f"Bahan yang tidak ada: {','. join(missing_ingredients)}")
else:
    print("Kamu mempunyai semua bahan yang dibutuhkan")

if extra_ingredients:
    print(f"Kamu mempunyai barang lebih yang tidak dibutuhkan: {', '.join(extra_ingredients)}")