# Introduction
# try:
#     num = int(input("Masukan sebuah angka: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Pembagian tidak boleh dengan angka 0")
# except ValueError:
#     print("Error: Invalid input. Dimohon memasukan angka yang valid.")

# try:
#     # Code that might raise an exception
# except ExceptionType:
#     # Code to handle exception
# else:
#     # Execute if no exception occurs
# finally:
#     # Always execute, even if an exeception occurs


# Finally Exception
# try:
#     num = int(input("Masukan sebuah angka: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Pembagian tidak boleh dengan angka 0")
# except ValueError:
#     print("Error: Invalid input. Dimohon memasukan angka yang valid.")
# finally:
#     print("Finally section dieksekusi, Program berhenti")


# Multiple Exception
# try:
#     num = int(input("Masukan sebuah angka: "))
#     result = 10 / num
#     print("Result:", result)
# except (ZeroDivisionError, ValueError):
#     print("Error: Pembagian tidak boleh dengan angka 0 atau Input tidak valid")

# Custom Exception
# def withdraw(amount):
#     if amount < 0:
#         raise ValueError("Invalid withdrwal amount - Amount cannot be negative")
#     print(f"you haven withdraw ${amount}")
    
    
# try:
#     withdraw(-50)
# except ValueError as event:
#     print(f"Error: {event}")


# Safe Calculator
# Step 1: Define Calculator Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a,b ):
    if b == 0:
        raise ZeroDivisionError("Cannot divied by zero")
    return a / b

# Step 2: Display Menu
def main_menu():
    print("Menu Operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
# Step 3: Get user input
while True:
    main_menu()
    choice = int(input("Select Operation (1-5): "))

    if choice == 5:
        print("Exiting Calculator, Goodbye!")
        break

    try:
        a = int(input("A: "))
        b = int(input("B: "))
        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        else:
            print("Invalid Choice, please select valid option.")
    except ValueError:
        print("Error: Invalid Input. Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error occured: {e}")
    finally:
        print("Thank you for using the safe calculator")