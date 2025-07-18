# Introduction
# list_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }

# contact = {
#     "name": "Rafly",
#     "phone": "123-456-7890",
#     "email": "apewinaja@gmail.com"
# }

# print(contact['name'])
# print(contact.get('email'))
# contact["phone"] = "634-423-7457"
# print(contact)
# contact["address"] = "Indonesia"
# print(contact)
# del contact['email']
# print(contact)

# for head,value in contact.items():
#     print(f"{head} => {value}")
    
# if 'email' in contact:
#     print("Email found!")
# else:
#     print("Email not found")


# Contact
# Step 1: Inisiasi variable Dictionaries
contact = {}

# Step 2: Definisikan Main Menu
def main_menu():
    print("\n----- Contanct Book Menu -----")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Edit Contanct")
    print("5. Delete Contact")
    print("6. Exit") 
    
# Step 3: Pembuatan Fitur
def add_contact():
    name = input("Masukan nama Contact: " )
    phone = input("Masukan nomer Contact: ")
    email = input("Masukan email Contact: ")
    contact[name] = {"phone": phone, "email": email}
    print(f"{name} berhasil ditambahkan kedalam contact")
    
def view_contact():
    if not contact:
        print("Contact kosong")
    else:
        for name, details in contact.items():
            print(f"Nama: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            
def search_contact():
    nama = input("Masukan nama Contact yang akan dicari: ")
    if nama in contact:
        for name, details in contact.items():
            print(f"Nama: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("Contact tidak ditemukan")
        
def edit_contact():
    nama = input("Masukan nama Contact yang ingin dirubah: ")
    if nama in contact:
        new_phone = input("Masukan nomor Contact baru: ")
        new_email = input("Masukan email Contact baaru: ")
        contact[nama] = {"phone": new_phone, "email": new_email}
        print(f"data contact {nama} berhasil dirubah")
    else:
        print("Contact tidak ditemukan")
        
def delete_contact():
    nama = input("Masukan nama Contact yang ingin dihapus: ")
    if nama in contact:
        del contact[nama]
        print(f"{nama} berhasil dihapus dari contact")
    else:
        print("Contact tidak ditemukan")
        
# Step 4: Main Program
while True:
    main_menu()
    choice = int(input("Pilih Menu: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        edit_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("Exit!")
        break
    else:
        print("Pilihan tidak valid!")