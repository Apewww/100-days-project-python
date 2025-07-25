# Introduction
# with open("Week 3/sample_data/journal.txt", "w") as file:
#    file.write("Day 1: Today i learned about writing files in Python. \n")

# with open("Week 3/sample_data/journal.txt", "a") as file:
#     file.write("Day 2: I built a journal logger . \n")

# try:
#     with open("Week 3/restricted/journal.txt", "w") as file:
#         file.write("Test Entry")
# except PermissionError:
#     print("You do not have permission to write to this file.")


# Daily Journal Logger

# Step 1: Define the journal file
journal_file = "daily_journal.txt"

# Step 2: Add a new entry
def add_entry():
    entry = input("Tuliskan jurnalmu: ")
    with open(journal_file, "a") as file:
        file.write(entry + '\n')
    print("Entry berhasil ditambahkan")
    
# Step 3: View all entries
def view_entries():
    try:
        with open(journal_file, "r") as file:
            content = file.read()
            if content:
                print("------ Jurnal Entries Mu ------") 
                print(content)
            else:
                print("Jurnal masih kosong")
    except FileNotFoundError:
        print("Jurnal belum dibuat")
        
# Step 4: Search entries by keyword
def search_entries():
    keyword = input("Masukan keyword: ").lower()
    try:
        with open(journal_file, "r") as file:
            content = file.readlines()
            found = False
            print("\n---- Hasil pencarian ----")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("Tidak ada hasil yang ditemukan")
    except FileNotFoundError:
        print("Jurnal belum dibuat")
        
# Step 5: Display Menu
def main_menu():
    print("----- Daily Journal Logger -----")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Exit")

# Step 6: Main Program Loop
while True:
    main_menu()
    choice = input("Pilih Menu (1-4): ").strip()
    
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        search_entries()
    elif choice == '4':
        print("Program ended.")
        break
    else:
        print("Pilihan tidak valid. Pilih menu yang tersedia.")