students = {
    "Alice": [85, 90, 88],
    "Bob": [70, 75, 72],
    "Charlie": [95, 92, 96],
    "David": [60, 65, 58],
    "Emma": [78, 82, 80]
}


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


for student, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print("Student:", student)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("--------------------")