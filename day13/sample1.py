# basic syntax
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# better way

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)