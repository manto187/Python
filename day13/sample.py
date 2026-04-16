# handling file reading errors
# method 1 by using try-except

try:
    with open("sample.txt", "r") as f:
        print(f.read())
except fileNotFoundError:
    print("file not found")


# method 2 using multiple errors

try:
    with open("sample.txt", "r") as f:
        print(f.read())
except fileNotFoundError:
    print("file missing")
except Exception as e:
    print("error", e)