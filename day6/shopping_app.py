shopping_list = []
while True:
    print("**********************************")
    print("         Shopping list app        ")
    print("**********************************")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

    option = input("select an option: ")
    if option == "1":
        item = input("enter item name: ")
        shopping_list.append(item)
        print("item added successfully")
    elif option == "2":
        if len(shopping_list) == 0:
            print("your shopping list is empty")
        else:
            print("your shopping list is: ")
            for i in range(len(shopping_list)):
                print(i+1, ".", shopping_list[i])
    elif option == "3":
            if len(shopping_list) == 0:
              print("your shopping list is empty")
            else:
             print("your shopping list is: ")
            for i in range(len(shopping_list)):
                print(i+1, ".", shopping_list[i])
                item_number = int(input("enter item number to remove: "))

                if item_number >=1 and item_number <= len(shopping_list):
                    removed_item = shopping_list.pop(item_number - 1)
                    print("item removed successfully:", removed_item)
                else:
                    print("invalid item number")
    elif option == "4":
        print("thank you for using the shopping list app")
        break
    else:        print("invalid option, please try again")