# add items to the end of the list

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)


# add items to a specific position in the list

numbers = [1,2,4,5]
numbers.insert(1,3)
print(numbers)

# remove items from the list
number= [1,2,3,4]
number.remove(3)
print(number)

# remove items from the list by index using pop() function

colors = ["red", "black", "brown"]
colors.pop(1)
print(colors)

# sorting lists

characters = ["zebra", "monkey", "rat", "cat", "bat"]
characters.sort()
print(characters)

# reversing lists
numbers = [5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)


# looping through lists

fruits = ["apples", "bananas", "cherries"]
for fruit in fruits:
    print(fruit)

languages = ["python", "java", "c++"]
for lang in languages:
    print("im learning", lang)


numbers = [2,4,6,8]
for num in numbers:
    print(num * 2)