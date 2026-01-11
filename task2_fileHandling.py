import os
def main():
    filename = "sample.txt"

    if os.path.exists(filename):

        with open(filename, 'r') as file:
            content = file.read()
            print("file content:\n")
            print(content)
    else:
            print("file does not exists")
if __name__ == "__main__":
     main()            