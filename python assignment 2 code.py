Python Code:- Student Record and Academic         Management System
students = {}
departments = {"Computer", "IT", "Mechanical"}

def add_student():
    roll = input("Enter roll number: ")
    if roll in students:
        print("Record already exists!")
        return

    name = input("Enter name: ")
    dept = input("Enter department: ")
    marks = list(map(int, input("Enter marks (3 subjects): ").split()))
    attendance = float(input("Enter attendance percentage: "))

    students[roll] = {
        "name": name,
        "department": dept,
        "marks": marks,
        "attendance": attendance
    }
    print("Student added successfully!")

def display_students():
    for roll, data in students.items():
        print(roll, data)

def search_student():
    roll = input("Enter roll number: ")
    print(students.get(roll, "Student not found"))

def update_student():
    roll = input("Enter roll number: ")
    if roll in students:
        students[roll]["name"] = input("Enter new name: ")
        print("Record updated!")
    else:
        print("Student not found")

def delete_student():
    roll = input("Enter roll number: ")
    if roll in students:
        del students[roll]
        print("Record deleted!")
    else:
        print("Student not found")

def average_marks():
    for roll, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        print(roll, data["name"], "Average:", avg)

while True:
    print("\n1.Add  2.Display  3.Search")
    print("4.Update  5.Delete  6.Average  7.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        average_marks()
    elif choice == "7":
        break
    else:
        print("Invalid choice!")
