# risky code
try:
    num = int(input("enter a number: "))
# runs if error occurs
except:
    print("invalid input")
# runs if no error occurs
else:
    print("you entered: ", num)
# runs always
finally:
    print("program ended")