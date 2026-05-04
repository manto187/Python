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

# handling mutiple exceptions........
try:
    a=int(input("enter a number: "))
    b=int(input("enter second number: "))
    print(a/b)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
except:
    print("something went wrong")   

# you can create your own exceptions using raise keyword...
age = int(input("enter your age: "))

if age < 18:
    raise Exception("you are not allowed")