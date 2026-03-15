# adding an element to a list and printing the list

numbers=[1,2,3,4,5]
numbers.append(6)
for num in numbers:
    print(num)

names = ["alice", "bob", "charlie"]
names.remove("bob")
for name in names:
    print(name)

# created list of numbers and check from that list which is the largest number  
numbers = [5, 3, 8, 1, 4]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("largest number is", largest)
