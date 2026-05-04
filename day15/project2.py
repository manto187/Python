import csv 

with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "status"])

    for i in range(3):
        name = input("enter name: ")
        status = input("present/absent: ")
        writer.writerow([name, status])