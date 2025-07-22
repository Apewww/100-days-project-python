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

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# labels = ['Even' if number % 2 == 0 else 'Odds' for number in numbers]
# print(labels)

# Student Grade Manager

# Step 1: Get student Scoress
student_scores = input("Masukan nilai dengan bagian (,): ")
scores = [int(score) for score in student_scores.split(',')]

# Step 2: Assign Grades using List Comprehension
grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

# Step 3: Filter Passing and failing students
passing_student = ([grade for grade in grades if grade != "F"], [score for score in scores if score >= 60])
failing_student = ([grade for grade in grades if grade == "F"], [score for score in scores if score < 60])

# Step 4: Print Result
print("------ Student Grade Manager ------")
for i,(score,grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score} and Grade = {grade}") 

print("------ Passing and failing Students ------")
print("Passing students: ")
for score,grade in zip(passing_student[0], passing_student[1]):
    print(f"Score: {score} | Grade: {grade}") 
print("Failing students:")
for score,grade in zip(failing_student[0], failing_student[1]):
    print(f"Score: {score} | Grade: {grade}")
    
    
    
# Bonus Solusi Lebih Efektif dan Aman
# grades = ["A", "B", "F", "C", "F"]
# scores = [85, 55, 70, 40, 90]

# # Gabungkan dulu (score, grade)
# students = list(zip(scores, grades))

# # Filter hanya yang lulus: score >= 60 dan grade != "F"
# passing_students = [(s, g) for s, g in students if s >= 60 and g != "F"]

# # Tampilkan hasil
# for score, grade in passing_students:
#     print(f"Passing students:\nScore: {score} | Grade: {grade}")
