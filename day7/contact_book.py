contacts = {}

while True:
    print("1. add contact")
    print("2. view contacts")
    print("3. search contacts")
    print("4. delete contacts")
    print("5. exit")

    option = input("enter your option: ")

    if option == "1":
        name = input("enter name: ")
        phone = input("enter phone number: ")
        contacts[name] = phone
        print("contact added successfully!")
    elif option == "2":
        if len(contacts) == 0:
            print("no contact found")
        else:
            for name, number in contacts.items():
                print(name, ":", number)
    elif option == "3":
        name = input("enter name to search: ")
        if name in contacts:
            print("number :", contacts[name])
        else:
            print("contact not found")
    
    elif option == "4":
        name = input("enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("contact deleted successfully!")
        else:
            print("contact not found")
    elif option == "5":
        print("goodbye....!")
        break
    else:
        print("invalid choice")