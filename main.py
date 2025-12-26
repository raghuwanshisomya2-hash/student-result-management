
# Student Result Management System

def calculate_grade(percentage):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Division"
    elif percentage >= 45:
        return "Second Division"
    elif percentage >= 33:
        return "Pass"
    else:
        return "Fail"


def main():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i+1}")
        name = input("Name: ")
        roll = input("Roll Number: ")

        marks = []
        for j in range(5):
            mark = float(input(f"Enter marks for subject {j+1}: "))
            marks.append(mark)

        total = sum(marks)
        percentage = total / 5
        grade = calculate_grade(percentage)

        students.append({
            "name": name,
            "roll": roll,
            "total": total,
            "percentage": percentage,
            "grade": grade
        })

    print("\n--- Student Results ---")
    for s in students:
        print(f"""
Name       : {s['name']}
Roll No    : {s['roll']}
Total Marks: {s['total']}
Percentage : {s['percentage']}%
Grade      : {s['grade']}
---------------------------
""")


if __name__ == "__main__":
    main()
