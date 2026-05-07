year=int(input("enter the year="));

if(year%400==0 and (year%4==0 or year!=0)):
    print("leap year");
else:
    print("not leap year");