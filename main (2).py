#find a year is leap year or not
Year=2016
if(Year%4==0 and Year%100!=0)or Year%400==0:
    print("{} is a leap year".format(Year))
else:
    print("{} is not a leap year".format(Year))
    
    

