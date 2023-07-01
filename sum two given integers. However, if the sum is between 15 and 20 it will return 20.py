# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.\

a=int(input("enter the first integer:-"))
b=int(input("enter the secound integer:-"))
c=a+b

if c>=15 and c<= 20:   you can also use this codition 15=< c >=20:
print("Your answer is:", 20)
else:
    print("Your answer is:", c)
