def marks(a,b,c):
    total = a+b+c
    percentage = total/3
    return total, percentage
a=int(input("enter marks 1: "))
b=int(input("enter marks 2: "))
c=int(input("enter marks 3: "))

t,p = marks(a,b,c)
print("total: ", t)
print("percentage: ", p)