def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 35:
        return "D"
    else:
        return "F (Fail)"

def student_grade_calculator():
    try:
        name = input("Enter student's name: ")
        subjects = int(input("Enter number of subjects: "))
        total_marks = 0

        for i in range(1, subjects + 1):
            mark = float(input(f"Enter mark for subject {i}: "))
            if mark < 0 or mark > 100:
                print("❌ Marks should be between 0 and 100.")
                return
            total_marks += mark

        percentage = total_marks / subjects
        grade = calculate_grade(percentage)

        print("\n🎓 Result")
        print("---------")
        print(f"Student Name   : {name}")
        print(f"Total Marks    : {total_marks}/{subjects * 100}")
        print(f"Percentage     : {percentage:.2f}%")
        print(f"Grade          : {grade}")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only!")

# Run the program
student_grade_calculator()

"""
🔹 Example Output 1:
Enter student's name: Aysha
Enter number of subjects: 3
Enter mark for subject 1: 85
Enter mark for subject 2: 90
Enter mark for subject 3: 80

🎓 Result
---------
Student Name   : Aysha
Total Marks    : 255.0/300
Percentage     : 85.00%
Grade          : A

🔹 Example Output 2:
Enter student's name: Sara
Enter number of subjects: 4
Enter mark for subject 1: 70
Enter mark for subject 2: 65
Enter mark for subject 3: 75
Enter mark for subject 4: 60

🎓 Result
---------
Student Name   : Sara
Total Marks    : 270.0/400
Percentage     : 67.50%
Grade          : B
"""

