import datetime
now = datetime.datetime.now()
presentyr=now.year  #to get present year
presentmon=now.month    #to get present month
presentday=now.day  #to get present day
day,mon,year=input("Enter your date of birth, ex:27-07-2000: ").split("-")  #input is splitted by using seperator "-"
totalyr=presentyr-int(year)
totalmon=presentmon-int(mon)
totalday=presentday-int(day)

if(day=="27" and mon=="07" and year=="2000"):
    print("hey!, we born on the same day")

if(totalmon < 0):
    print("your age is ",-totalmon,"months",totalday," day(s) lesser to",totalyr,"years")
else:
    print("your age is ",totalyr,"years,",totalmon,"months and ",totalday,"days")
