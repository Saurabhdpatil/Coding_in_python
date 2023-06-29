# sum of three given numbers, if the values are equal then return thrice of their sum

num1=int(input("enter the no 1:-"))
num2=int(input("enter the no 2:-"))
num3=int(input("enter the no 3:-"))

if num1 == num2 == num3:
    print((num1+num2+num3)*3)
else:
    print(num1+num2+num3)
