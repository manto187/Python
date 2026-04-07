# understand return values in functions.
def add(a,b):
    return a+b
result = add(2,3)
print(result)


# without return function give nothing..
def add(a,b):
    return a+b
result = add(2,3)
print(x)

# function used to perform calculations
# square of a number
def square(num):
    return num*num
print(square(4))

# average of a number
def average(a,b):
    return (a+b)/2
print(average(10,20))

# returning multiple values
def calc(a,b):
    sum=a+b
    diff=a-b
    return sum, diff
x,y = calc(10,5)
print(x)
print(y)