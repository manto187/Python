# writing to the file

with open("note.txt", "w") as file:
    file.write("this is a fresh start\n")
    file.write("this is old content that is gone")

# reading from file

with open("note.txt", "r") as file:
    print(file.read())

# appending to file

with open("note.txt", "a") as file:
    file.write("\n this line was added later")

# file handling errors

try:
    with open("protected_file.txt", "w") as file:
        file.write("hello world")
except PermissionError:
    print("error: you dont have permission to write to this file")

except Exception as e:
    print(f"an unexpected error occured:{e}")