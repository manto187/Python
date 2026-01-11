num = [0,0,0]
for i in range(0,3):
    num[i] = int(input("enter number:"))
largest  = num[0]
for i in range(0,3):
    if(num[i]>largest):
        largest = num[i]
print("largest is: ", largest)