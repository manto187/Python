while True:
    print("1. add notes")
    print("2. view notes")
    print("3. clear notes")
    print("4. exit")

    option = input("enter your choice: ")

    if option =="1":
        note = input("enter your note: ")
        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()
        print("note added successfully!")

    elif option =="2":
        try: 
            file = open("notes.txt", "r")
            print("\nyour notes: ")
            print(file.read())
            file.close()
        except:
            print("no notes found")
    elif option == "3":
        file = open("notes.txt", "w")
        file.write("")
        file.close()
        print("note cleared successfully")
    elif option =="4":
        break
    else:
        print("invalid choice")
    