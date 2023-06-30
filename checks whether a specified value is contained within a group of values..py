# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


l = int(input("Enter the number to check whether it is present in the group of values or not: "))
a = [1, 5, 8, 3]
print(l in a)
