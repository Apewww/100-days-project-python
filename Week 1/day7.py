# Introduction
# shopping_list = ['Milk', 'Egg', 'Bread']
# shopping_list.append('Butter')
# shopping_list.insert(0,'Juice')
# print(shopping_list)

# shopping_list.sort()
# shopping_list.reverse()
# shopping_list.clear()
# print(shopping_list)

# shopping_list.remove('Milk')
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)

# for i in shopping_list:
#     print(f"- {i}")

# for index,item in enumerate(shopping_list):
#     print(f"[{index + 1}] {item}")

# Shopping List App
# Step 1: Initialize an empty Shopping List
shopping_list = []

# Step 2: Define the main menu
def main_menu():
    print("\n------ Shopping List Menu ------")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear List")
    print("5. Exit")
    print("----------------------------------")
    
# Step 3: Main Program Loop
while True:
    main_menu()
    choose = int(input("Choose the menu: "))
    if choose == 1:
        if not shopping_list:
            print("The shopping list is empty.")
        else:
            for index,item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
    elif choose == 2:
        add = input("Enter the item to add: ")
        shopping_list.append(add)
    elif choose == 3:
        remove = input("Enter the item to remove: ")
        shopping_list.remove(remove)
    elif choose == 4:
        shopping_list.clear()
        print("Item has been clear")
    elif choose == 5:
        break
    else:
        print("Invalid Option!")