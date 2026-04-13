# normal way to create list
number=[]
for i in range(5):
    number.append(i)
print(number)

# list comprehension

number = [i for i in range(5)]
print(number)

# [expression for item in iterable]

squares = [x*x for x in range(5)]
print(squares)

# 2. filtering with list comprehension

# [express for item in iterable if condition]
even_number = [x for x in range(10) if x%2==0]
print(even_number)


# using conditional statements..
# [expression_if_true if condition else expression_if_false for item in iterable]
result = ["even" if x %2==0 else "odd" for x in range(5)]
print(result)
