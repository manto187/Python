# reading csv file
import csv 
file = open("student.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(row)

file.close()

# writing csv files 

import csv 
file = open("student.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["name", "marks", "grade"])
writer.writerow(["ali", 85, "A"])
writer.writerow(["sara", 90, "A+"])

file.close()

# using csc module 

import csv 

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

        