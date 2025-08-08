# Introduction

# class Calculator:
#     base_value = 100
    
#     @staticmethod
#     def add(value1, value2):
#         return value1 + value2
    
#     @classmethod
#     def multiply_base(cls, multiplier):
#         return cls.base_value * multiplier
    
# # Using Static Method
# print(Calculator.add(1,2))
# # Using Class Method
# print(Calculator.multiply_base(5))

# class Utility:
#     @staticmethod
#     def greet_user(name):
#         print(f"Hello, {name}")
        
# Utility.greet_user("Rafly")

class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        # cls.count += 1
        cls.count += 10
        
Counter.increment()
print(Counter.count)