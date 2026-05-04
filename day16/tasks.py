# task 1 stored student data in json file
import json 

student = {
    "name": "asad", 
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file)


# task 2 read and display data 

import json 

with open("student.json", "r") as file:
    data = json.load(file)

print("name:", data["name"])
print("marks:", data["marks"])


# task 3 adding new field

import json 

with open("student.json", "r") as file:
    data = json.load(file)

data["grade"] = "A"
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)