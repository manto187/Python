import csv 
with open("contact.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "phone"])

    for i in range(3):
        name = input("enter name: ")
        phone = input("enter phone: ")
        writer.writerow([name, phone])