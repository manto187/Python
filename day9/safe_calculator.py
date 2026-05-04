while True:
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    option = input("enter you choice: ")
    if option == "5":
        break
    try:
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        if option == "1":
            result = a+b
        elif option == "2":
            result = a-b
        elif option == "3":
            result = a*b
        elif option == "4":
            result = a/b
    except ValueError:
        print("invalid input")
    except ZeroDivisionError:
        print("cannot divide by zero")
    else:
        print("result: ", result)
    finally:
        print("calculation completed")