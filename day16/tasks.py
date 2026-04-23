# task 1 stored student data in json file
import json 

student = {
    "name": "asad", 
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file)