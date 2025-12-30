num = [0,0,0]
for i in range(0,3):
    num[i] = int(input("enter number: "))
greatest = num[0]
for i in range(0,3):
    if (num[i]>greatest):
        greatest = num[i]
print("Greatest number is:",greatest)