students = {}

while True:
    print("1. add student")
    print("2. update marks")
    print("3. show students")
    print("4. find topper")
    print("5. exit")

    choice = input("enter choice: ")

    if choice == "1":
        name = input("enter name: ")
        marks = int(input("enter marks: "))
        students[name] = marks

    elif choice == "2":
        name = input("enter name: ")
        if name in students:
            marks = int(input("enter new marks: "))
            students[name] = marks
        else:
            print("student not found")

    elif choice == "3":
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "4":
        if len(students) > 0:
            topper = max(students, key=students.get)
            print("topper:", topper, "with marks", students[topper])
        else:
            print("no data")

    elif choice == "5":
        break

    else:
        print("invalid choice")