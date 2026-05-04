# reading from files
file = open("file.txt", "r")
data = file.read()
file.close()

# writing to files
file = open("notes.txt", "w")
file.write("Hello World")
file.close()


# appending to files
file = open("notes.txt", "a")
file.write("\nNew Note")
file.close()