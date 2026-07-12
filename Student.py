students = {}

while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        students[roll] = {"Name": name, "Marks": marks}
        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            for roll, data in students.items():
                print(f"Roll No: {roll}")
                print(f"Name: {data['Name']}")
                print(f"Marks: {data['Marks']}")
                print("---------------------")
        else:
            print("No Records Found.")

    elif choice == "3":
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(students[roll])
        else:
            print("Student Not Found.")

    elif choice == "4":
        roll = input("Enter Roll Number: ")
        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
