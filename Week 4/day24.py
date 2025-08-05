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