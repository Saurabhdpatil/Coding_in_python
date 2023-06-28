# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

#code 1st you can take input from user..........
day=input("enter a day::")
month=input("enter a month")
year=input("enter a year:")
print("your date is:",day,"/",month,"/",year)
          
                #.........................................both gives you same output...........................................#

#code 2nd...........
exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date
print("The examination will start from: {}/{}/{}".format(day, month, year))
