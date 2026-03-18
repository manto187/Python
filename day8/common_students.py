classA = {"Ali", "Ahmad", "Sara"}
classB = {"Sara", "Zain", "Ali"}

common = classA & classB

print("common students: ", common)



onlyA = classA - classB
onlyB = classB - classA

print("Only in Class A:", onlyA)
print("Only in Class B:", onlyB)