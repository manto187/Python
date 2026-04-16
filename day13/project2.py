def login():
    username = input("username: ")
    password = input("password: ")

    try:
        with open("users.txt", "r") as f:
            for line in f:
                user, pwd = line.strip().split(":")

                if user == username and pwd == password:
                    print("login successful")
                    return
        print("invalid credentials")

    except FileNotFoundError:
        print("user file not found")

#main
login()