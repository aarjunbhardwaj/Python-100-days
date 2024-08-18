print("Welcome to the tip calculator!")
bill = float(input("What is total bill amount?\n$:"))
tip = int(input("How Much tip do you want to give?\nPercentage:"))
split = int(input("How many people to the split the bill?\nPeople:"))

total_amount = round(bill + (bill * tip / 100), 2)
print("Each person pays: $", total_amount / split)