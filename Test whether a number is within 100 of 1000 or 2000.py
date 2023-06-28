# Write a Python program to test whether a number is within 100 of 1000 or 2000.



a=int(input("enter the no that you want test  either it is 1000,100or 2000:-"))
if a>=1000:
    print("your no is under 2k ")
elif a<=100:
    print("your no is under the 100")
elif a<=1000:
    print("your no is under the 1000")
else:
    print("enter the valid no")
