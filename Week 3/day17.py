# Introduction
# import csv

# with open("Week 3/sample_data/students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import csv

# with open("Week 3/sample_data/students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# import csv

# with open("Week 3/sample_data/students.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name','Math','Science','English'])
#     writer.writerow(['Daisy',88,92,85])

# import csv

# with open("Week 3/sample_data/students.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['Name','Math','Science','English'])
#     writer.writeheader()
#     writer.writerow({'Name': 'Eve', 'Math': 91, 'Science': 87, 'English': 97})



# Student Report Generator