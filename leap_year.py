year = int(input("Enter year:"))
if year % 4 == 0:
    if year %100 == 0:
        if year % 400 == 0:
             print("leap year",year)
        else:
            print("this is not leap year",year)
    else:
            print("a leap year",year)
else:
    print("not a leap year",year)