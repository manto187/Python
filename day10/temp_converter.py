def c_tof(c):
    return (c*9/5)+32
def f_to_c(f):
    return (f-32)*5/9

temp = float(input("enter temprature: "))
unit = input("enter unit(centigrade for C/fahrenheit for F): ")

if unit == "C":
    print("fahrenheit: ", c_to_f(temp))

elif unit == "F":
    print("celsius: ", f_to_c(temp))

else:
    print("invalid input")