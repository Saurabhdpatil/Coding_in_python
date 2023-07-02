# Write a Python program to add two objects if both objects are integers.

a = input("Enter the first integer: ")
b = input("Enter the second integer: ")

if a.isdigit() and b.isdigit():
    c = int(a) + int(b)
    print("The sum of the two integers is:", c)
else:
    print("Please enter valid integer values.")
