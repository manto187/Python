# read mode

with open("sample.txt", "r") as sample:
    print(f.read())

# read binary mode

with open("image.jpg", "rb") as img:
    data = f.read()


# read + write mode

with open("file.txt", "r+") as f:
    print(f.read())
    f.write("\nNew line added")