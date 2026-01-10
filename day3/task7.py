price = float(input("enter price: "))
quantity = int(input("enter quantity: "))
amount = price * quantity
if(amount>200):
    if(amount>1000):
        print("amount is greater than 1000")
    else:
        if(amount>800):
            print("amount is between 800 and 1000")
        elif(amount>600):
            print("amount is between 600 and 1000")
        else:
            print("amount is between 200 and 1000")
elif(amount==200):
    print("amount is 200")
else:
    print("amount is less than 200")