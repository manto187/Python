students = ["ali", "ahmed", "usman", "sara", "ayesha"]
marks = [85, 42, 73, 90, 38]

data = list(zip(students, marks))

passed = [name for name, mark in data if mark>=50]

failed = [name for name, mark in data if  mark<50]

grades = [
    ("A" if mark>=80 else "B" if mark>=60 else "C" if mark>=50 else "F")
for name, mark in data
]

print("all students: ", data)
print("passed: ", passed)
print("failed: ", failed)
print("grades: ", grades)