available = {"egg", "milk", "flour", "sugar"}
required = {"egg", "milk", "butter", "sugar"}

have = available & required
missing = required - available

print("you have: ", have)
print("you are missing:", missing)

if missing: 
    print("you cannot make the recipe")
else:
    print("you can make the recipe")