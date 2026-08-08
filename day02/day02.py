# Tip_Calculator
print("Welcome to the tip calculator.")
# ask for the tip percentage
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# ask for the bill
bill = float(input("What was the total bill? $"))
# ask for the number of people
people = int(input("How many people to split the bill? "))
# calculate total with tip
total = bill * (1 + tip / 100)
bill_per_person = total / people
# print the result
print("Each person should pay: $" + str(round(bill_per_person, 2)))
