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

# class Counter:
#     count = 0
    
#     @classmethod
#     def increment(cls):
#         # cls.count += 1
#         cls.count += 10
        
# Counter.increment()
# print(Counter.count)

# Inventory Management System

class Inventory:
    total_items = 0
    
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity
        
    # Instance Method: Show Product Detail
    def show_product_details(self):
        print("\n----- Product Details -----") 
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        
    # Instance Method: Sell Product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"You have sold {amount} units of {self.product_name}")
        else:
            print(f"Not enough {self.product_name} in stock to sell {amount} units.")
            
    # Static Method: Calculate Discount
    @staticmethod
    def calculate_discount(price, discount_precentage):
        return price * (1 - discount_precentage / 100)
    
    # Class Method: Total Items Report
    @classmethod
    def total_items_report(cls):
        print(f"\nTotal Items: {cls.total_items}")
        
# Main Program
products = []

# Add Product to Inventory
def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    product = Inventory(product_name, price, quantity)
    products.append(product)
    print(f"{quantity} {product_name}(s) added to inventory.")
    
# Display All Products
def view_products():
    print("\n----- Inventory -----")
    if not products:
        print("No products in inventory.")
    else:
        for product in products:
            product.show_product_details()
            
# Sell Product
def sell_product():
    product_name = input("Enter product name: ")
    for product in products:
        if product.product_name == product_name:
            amount = int(input("Enter amount to sell: "))
            product.sell_product(amount)
            break
    else:
        print("Product not found in inventory.")
        
# Calculate Discount
def discount_price():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: "))
    discount_price = Inventory.calculate_discount(price, discount_percentage)
    print(f"Discounted Price: {discount_price}")
    
# Main Menu
while True:
    print("\n----- Inventory Management System -----")
    print("1. Add Product to Inventory")
    print("2. View All Products")
    print("3. Sell Product")
    print("4. Calculate Discount Price")
    print("5. Total Items")
    print("6. Exit")
    
    choice = input("Enter your choice(1-6): ")
    
    if choice == '1':
        add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        sell_product()
    elif choice == '4':
        discount_price()
    elif choice == '5':
        Inventory.total_items_report()
    elif choice == '6':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")