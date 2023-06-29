print("'.......................calculator............................... "
       "to find area perimeter\n,"
      "(t) =area of triangle\n "
      "(c) =area of circle\n"
      "(s) =area of sqaure\n"
      "(r) =area of rectangle\n "'')

print("--------------------------------------------------")
INPUT=input()
if INPUT=="t":
    print("area of triangle")+
    b=eval(input("enter a bredth:-"))
    h=eval(input("enter a height:-"))
    print("area of triangle is:-",0.5*b*h)

elif INPUT=="c":
    print("area of circle")
    pi=3.14
    r=eval(input("enter the radius:-"))
    print("area of circle is:-",pi*r)

elif INPUT=="s":
    print("area of sqaure")
    a=eval(input("enter the area:-"))
    print("area of sqaure is:-",a*a)

elif INPUT=="r":
    print("area of radius")
    l=eval(input("enter the length:-"))
    w=eval(input("enter the weidth:-"))
    print("area of rectangle is:-",l*w)

else:
    print("enter the correct area of perimeter shortcurt*")
