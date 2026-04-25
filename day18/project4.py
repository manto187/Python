from datetime import datetime 

y = int(input("year: "))
m = int(input("month: "))
d = int(input("day: "))

birth = datetime(y, m, d)
now = datetime.now()

years = now.year - birth.year
months = now.month - birth.month
days = now.day - birth.day

if days<0:
    months -=1 
    days+=30

if months<0:
    years -=1
    months+=12

print(f"age: {years} years, {months} months, {days} days")
