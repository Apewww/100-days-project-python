# Introduction

# Parent class
# class Animal:
#     def sound(self):
#         print("The animal makes a sound")
        
# # Child class
# class Dog(Animal):
#     def sound(self):
#         print("The dog barks")
        
# # Child class
# class Cat(Animal):
#     def meow(self):
#         print("The cat meows")
        
# cat = Cat()
# cat.sound()

# class Parent:
#     def display(self):
#         print("Parent class")

# class Child(Parent):
#     pass

# child = Child()
# child.display()

# class A:
#     def method_a(self):
#         print("Inside method_a of class A")
        
# class B:
#     def method_b(self):
#         print("Inside method_b of class B")
        
# class C(A,B):
#     pass
        
# obj = C()
# obj.method_a()
# obj.method_b()

# class GrandParent:
#     def display(self):
#         print("GrandParent class")
        
# class Parent(GrandParent):
#     pass

# class Child(Parent):
#     pass

# child = Child()
# child.display()

# class Animal:
#     def __init__(self):
#         print("Animal Created")
        
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Dog Created")
        
# dog = Dog()

# class Vehicle:
#     def fuel_type(self):
#         print("Fuel type: Petrol/Diesel")
        
# class ElectricCar(Vehicle):
#     def fuel_type(self):
#         print("Fuel type: Electric")
        
# car = ElectricCar()
# car.fuel_type()

# Employee Management System

# Base Class: Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary
        
    def display_info(self):
        print("\n----- Employee Details -----")
        print(f"Name: {self.name}") 
        print(f"Employee ID: {self.id}") 
        print(f"Salary: {self.salary}")
        
    def calculate_bonus(self):
        return self.salary * 0.1
    
# Derived Class Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f"Departemen: {self.department}")
        
    def calculate_bonus(self):
        return self.salary * 0.2
    
# Derived Class Developer
class Developer(Employee):
    def __init__(self, name, emp_id, salary, progamming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = progamming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        
    def calculate_bonus(self):
        return self.salary * 0.5
    
# Main Program
employees = []

def add_employee():
    print("\n----- Choose Employee Type -----")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer") 
    choice = int(input("Enter your choice: ").strip())
    
    name = input("Enter Employee Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Salary: ").strip())
    
    if choice == 1:
        employees.append(Employee(name, emp_id, salary))
    elif choice == 2:
        department = input("Enter Department: ").strip()
        employees.append(Manager(name, emp_id, salary, department))
    elif choice == 3:
        programming_language = input("Enter Programming Language: ").strip()
        employees.append(Developer(name, emp_id, salary, programming_language))
    else:
        print("Invalid choice")
        
def display_all_employees():
    print("\n----- All Employees -----")
    for employe in employees:
        employe.display_info()
        print(f"Bonus: {employe.calculate_bonus()}")
        
# Menu
while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")
    choice = int(input("Enter your choice: ").strip())
    
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employees()
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid Choice")