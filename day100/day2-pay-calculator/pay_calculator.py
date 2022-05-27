# Greeting
print("Welcome to the pay calculator")

# Input bill
bill = float(input("What was the total bill? $"))

# Input tip percent
tip_percent = float(input("What percentage tip would you like to give? "))

# Input number of people
people_num = int(input("How many people to split the bill? "))

# Calculate each pay
pay = round(bill * (100+tip_percent)/100 / people_num, 2)

print(f"Each person shoule pay: ${pay}")