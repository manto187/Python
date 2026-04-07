def distance(km):
    meters = km*1000
    miles = km*0.621371
    return meters, miles

km = float(input("enter distance in km: "))
m,mi = distance(km)

print("meters: ", m)
print("miles: ", mi)