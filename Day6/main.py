print("Enter a Number")
number = int(input())
number_entered = number

fac = 1

if number == 0:
    result = 0
else:
    while number>=1:
        fac = fac*number
        number = number-1
    result = fac

print(f"Factorial of {number_entered} is {result}")
