# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

# Future Value = Principal Amount * (1 + Rate of Interest / 100) ^ Number of Years

a = eval(input("enter the principal amount:-"))
b = eval(input("enter the rate of interest:-"))
c = eval(input("enter the no of year:-"))

future_value = (a * (1 + b / 100) ** c)   #here this (^) operator is not work in python so use for power is **

print("future value is :-", future_value)
