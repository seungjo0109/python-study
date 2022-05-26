# example 1
print("Hello"[4])
print(123_456_789)

# example2
str = input("Type a two digit number: ")
num = int(str[0]) + int(str[1])
print(num)

# example 3
weight = float(input("enter your weight in kg = "))
height = float(input("enter your height in m = "))
bmi = int(weight/height**2)
print(bmi)

# example 4
age = int(input("What is your current age?"))
remain_months = (90-age)*12
remain_weeks = (90-age)*52
remain_days = (90-age)*365

print(f"You have {remain_days} days, {remain_weeks} weeks and {remain_months} months left.")