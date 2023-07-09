# Write a program that checks if a given number is positive, negative, or zero.
user=int(input("enter no that check given no is postive , negative or zero:-"))
if user <0:
    print("your no is negative:-",user)
elif user==0:
    print("your no is zero:-",user)
elif user>=0:
    print("your no is positive:-",user)
else:
    print("enter the valid no")
