                # addtion,subtraction,multiplication,divide calculator...........

print('''
+ ADD
- SUB
* MUL
/ DIV
'''
)

num1=eval(input("enter the first no:-"))
num2=eval(input("enter the second no:-"))
opr=input("enter the operators:-")

if opr=="+":
    print(num1+num2)

elif opr=="-":
    print(num1-num2)

elif opr=="*":
    print(num1*num2)

elif opr=="/":
    print(num1/num2)

else:
    print("invalid operator")
