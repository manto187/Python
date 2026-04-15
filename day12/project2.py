import random

def generate_otp():
    otp = ""
    for _ in range(6):
        otp +=str(random.randint(0,9))
    return otp

otp = generate_otp()
print("your otp is: ", otp)

user_input = input("enter otp: ")

if user_input == otp:
    print("access granted")

else:
    print("invalid otp")
     