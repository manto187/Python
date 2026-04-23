import json 
import os 

FILE = "project.json"

# load tasks 
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as file:
        return json.load(file)
    
# save tasks 
def save_tasks(tasks):
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# add task
def add_task():
    task = input("enter task:")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("task added successfully")

# view tasks 
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("no tasks found")
        return 
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("enter task number to delete:"))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("task deleted successfully")
    except:
        print("invalid input")

# main menu

while True:
    print("1.add task")
    print("2.view tasks")
    print("3.delete task")
    print("4.exit")

    choice = input("enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":        
        delete_task()
    elif choice == "4":
        break
    else:
        print("invalid choice")