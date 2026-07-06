students = {}

def calculate_grade(avg):
    if avg >= 90:
        return "a+"
    elif avg >= 80:
        return "a"
    elif avg >= 70:
        return "b"
    elif avg >= 60:
        return "c"
    elif avg >= 50:
        return "d"
    else:
        return "f"

def add_student():
    roll = input("enter roll number: ")
    if roll in students:
        print("student already exists.")
        return

    name = input("enter student name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"enter marks of subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
    }
    print("student record added successfully!")

def search_student():
    roll = input("enter roll number to search: ")
    if roll in students:
        s = students[roll]
        print("\nstudent detail")
        print("________")
        print("roll number:", roll)
        print("name :", s["name"])
        print("marks :", s["marks"])
        print("total :", s["total"])
        print("average :", round(s["average"], 2))
        print("grade :", s["grade"])
    else:
        print("student not found!")

def display_students():
    if not students:
        print("no student records found")
        return

    print("\nall student records")
    print("_" * 60)
    for roll, s in students.items():
        print("roll number:", roll)
        print("name :", s["name"])
        print("marks :", s["marks"])
        print("total :", s["total"])
        print("average :", round(s["average"], 2))
        print("grade :", s["grade"])
        print("_" * 60)

while True:
    print("\n===== student record management system =====")
    print("1. add student record")
    print("2. search student record")
    print("3. display all student records")
    print("4. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        display_students()
    elif choice == "4":
        print("thank you!")
        break
    else:
        print("invalid choice please try again.")
