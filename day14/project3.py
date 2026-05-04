def todo_list():
    print("\n    to-do manager    ")
    task = input("enter a new task: ")
    with open("todo.txt", "a") as file:
        file.write(f"[ ] {task}\n")

    print("current tasks: ")
    with open("todo.txt", "r") as file:
        print(file.read())

todo_list()