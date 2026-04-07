def salary(monthly):
    yearly = monthly*12
    return monthly, yearly
m=float(input("enter monthly salary: "))
month, year = salary(m)

print("monthly: ", month)
print("yearly: ", year)