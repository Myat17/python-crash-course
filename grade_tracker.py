# Dictionaries and if statements
# Student Grade Tracker
# Manage student names and their scores then determine if they passed
student_grades = {}

while True:
    name = input("Enter a student name or enter 'q' to quit: ")


    if name.lower() == "q":
        break

    score = input("Enter the student's score or enter 'q' to quit: ")

    if score.lower() == 'q':
        break

    student_grades[name] = int(score)

print("\n--- Student Grade Report ---")

for student_name, student_score in student_grades.items():
    if student_score >= 80:
        print(f"{student_name.title()} scored {student_score} and passed with distinction!")
    elif student_score >= 60:
        print(f"{student_name.title()} scored {student_score} and passed!")
    else:
        print(f"{student_name.title()} scored {student_score} and  failed!")
