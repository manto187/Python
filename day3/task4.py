import os.path
def main():
    if(os.path.exists("data.txt")):
        f=open("data.txt",'a')
        f.write("\nNew Line")
        f.close()
    else:
        print("File does not exist" )

if __name__ =="__main__":
    main()
