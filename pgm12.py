# leap year
year = 2000
if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# using input()
yr = int(input("Enter the year:"))
if (yr % 4) == 0:
    if(yr % 100) == 0:
        if(yr % 400) == 0:
            print("{0} is a leap year".format(yr))
        else:
            print("{0} is not a leap year".format(yr))
    else:
        print("{0} is a leap year".format(yr))
else:
    print("{0} is not a leap year".format(yr))




