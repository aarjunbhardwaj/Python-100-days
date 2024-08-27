'''
The rules for determining a leap year are:

1. If the year is divisible by 4, it is a leap year.
2. However, if the year is divisible by 100, it is not a leap year.
3. Unless the year is also divisible by 400, in which case it is a leap year.

'''
year = int(input("Which year do you want to check: "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 ==0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
        print("it's not a leap year")
    else:
        print("It's a leap year")
    print("it's a leap year")
else:
    print("it's not leap year")