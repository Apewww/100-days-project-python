# Introduction

# class Animal:
#     def make_sound(self):
#         print("The animal makes a sound")
        
# class Dog(Animal):
#     def make_sound(self):
#         print("The dog barks")
        
# class Cat(Animal):
#     def make_sound(self):
#         print("The cat meows")
        
# # Polymorphism in action
# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.make_sound()

# class Shape:
#     def area(self):
#         print("Calculating area...")
        
# class Circle(Shape):
#     def area(self):
#         print("Area of a Circle: pi*r*r")
#         # return 3.14 * self.radius * self.radius

# class Square(Shape):
#     def area(self):
#         print("Area of a Square: side*side")
        
# # Polymorphissm in action
# shapes = [Circle(), Square()]
# for shape in shapes:
#     shape.area()

# class Bird:
#     def make_sound(self):
#         print("Bird chirps!")
        
# class Duck:
#     def make_sound(self):
#         print("Duck quacks!")
        
# def animal_sounds(animal):
#     animal.make_sound()
    
# # Polymorphism in function argument
# bird = Bird()
# duck = Duck()

# animal_sounds(bird)
# animal_sounds(duck)