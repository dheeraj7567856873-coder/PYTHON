day=int(input("enter the month number=")) 

match day:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")
    case _:
        print("invalid month")