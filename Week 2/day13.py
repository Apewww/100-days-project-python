# Introduction
# squares = [x**2 for x in range(10)]
# print(squares)

# numbers = [1, 2, 3, 4, 5]
# doubled_nunbers = [x*2 for x in numbers]
# print(doubled_nunbers)

# numbers = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
# even_numbers = [even for even in numbers if even % 2 == 0]
# print(even_numbers)

# names = ['Rafly', 'aaaaaaa', 'Raf', 'aaaaaaa']
# # uppercase_name = [name.upper() for name in names]
# short_name = [name for name in names if len(name) < 5]
# print(short_name)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ['Even' if number % 2 == 0 else 'Odds' for number in numbers]
print(labels)