# counting total students 
import csv 
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    count = 0
    next(reader) 

    for row in reader:
        count += 1
print("total students: ", count)

# finding highest marks 
import csv 
with open("students.cvs", "r") as file:
    reader = csv.reader(file)
    next(reader)

    max_marks = 0
    topper = ""

    for row in reader:
        marks = int(row[1])
        if marks > max_marks:
            max_marks = marks 
            topper = row[0]
print("topper: ", topper)
print("marks: ", max_marks)