import math

principle = int(input("enter the principle value="))

rate = int(input("enter the rate value="))

time = int(input("enter the time value="))

compoundInterest = principle * math.pow(1 + rate/100, time)

print("compound interest of =",compoundInterest);
