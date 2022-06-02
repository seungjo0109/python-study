# example 1
number = int(input("Which number do you want to check? "))
if number%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# example 2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = (weight/height**2)

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are normal weight")
elif bmi < 30: 
    print("you are overweight")
elif bmi < 35:
    print("you are obese")
else:
    print("you are clinically obese")

# example 3
year = int(input("Which year to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is leap year")
        else:
            print("This it not leap year")
    else:
        print("This is leap year")
else:
    print("This is not leap year")

# example 4
print("Welcom to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
name1 += name2

true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
percent = 10*(true%10) + love

if percent < 10 and percent > 90:
    print(f"Your love percent is {percent}, you go together coke and metos.")
elif percent > 40 and percent <50: 
    print(f"Your love percent is {percent}, you are alright together.")
else:
    print(f"Your love percent is {percent}")
