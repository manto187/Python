list1 = {"milk", "bread", "eggs"}
list2 = {"bread", "butter", "eggs"}

common = list1 & list2
print("common items:", common)

only1 = list1-list2
only2 = list2-list1

print("only in list1:", only1)
print("only in list2:", only2)