# a simple program to calculate the sum of a list of numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
sum=0
for num in numbers:
    sum +=num
print("the sum of the numbers is", sum)

# counting even numbers in a list
numbers = [2,5,6,7,8,14]
count=0
for num in numbers:
    if num % 2 == 0:
        count +=1
print("the count of even numbers is", count)    

# finding second largest number in the list

numbers = [5, 3, 8, 1, 4]
numbers.sort()
second_largest = numbers[-2]
print("the second largest number is", second_largest)