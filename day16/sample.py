import json 
with open('data.json') as file:
    data = json.load(file)

print(data)
print(data["name"])


# writing to json file 

import json 
data = {
    "name": "asad",
    "age": 25,
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


# modifying json data 

import json

with open("data.json", "r") as file:
    data = json.load(file)

# Modify
data["age"] = 22
data["city"] = "Lahore"

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
