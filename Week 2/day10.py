# Introduction
# file = open("./sample_data/filename.txt", "r+")
# file.close()

# with open("sample_data/notes.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("sample_data/notes.txt", "w") as file:
#     file.write("This is a new line of text.")
    
# with open("sample_data/notes.txt", "a") as file:
#     file.write("\nLine Baru.\n")


# Note-Taking App
# Step 1: Define File Name
file_name = "./sample_data/MyNotes.txt"

# Step 2: Display menu options
def main_menu():
    print("\n ------ Note-Taking App ------ ")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

# Step 3: Add a new note function
def add_notes():
    note = input("Enter your note: ")
    with open(file_name, "a") as file:
        file.write(note + "\n")
    print("Note berhasil ditambahkan!")

# Step 4: View all notes
def view_notes():
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if content:
                print("----- Your Notes -----")
                print(content)
            else:
                print("Notes kosong!")
    except FileNotFoundError:
        print("File note tidak ditemukan!")

# Step 4: Delete all notes
def delete_notes():
    confirm = input("Apakah kamu yakin ingin menghapusnya? (Y/N): ")
    if confirm.lower() == "y":
        with open(file_name, "w") as file:
            # file.write("")
            pass
            print("Notes berhasil dihapus!")
    else:
        print("Notes tidak jadi dihapus!")

# Step 5: Main Program
while True:
    main_menu()
    choice = int(input("Pilih Menu: "))
    if choice == 1:
        add_notes()
    elif choice == 2:
        view_notes()
    elif choice == 3:
        delete_notes()
    elif choice == 4:
        print("Program berhenti.")
        break
    else:
        print("Pilihan Menu tidak valid, pilih menu (1-4)")