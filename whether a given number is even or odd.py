# Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.

number=int(input("enter no that check either no is even or odd:-"))

if number % 2== 0:       #number  % 2 == 0 this condition that shows either no is even or not.....
    print("your given no is even:-",number)

else:
    print("your given no is odd:-",number)
