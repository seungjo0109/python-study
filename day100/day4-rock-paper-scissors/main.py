import random

# random_integer = random.randint(1, 10)
# random_float = random.random()
# print(random_integer)
# print(random_float)

# # example 1
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# # example 2
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")

# random_integer = random.randint(0, len(names)-1)
# print(f"{names[random_integer]} is going to buy the meal today!")
# # print(random.choice(names))

# example 3
row1 = ["🟦", "🟦", "🟦"]
row2 = ["🟦", "🟦", "🟦"]
row3 = ["🟦", "🟦", "🟦"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure?")
map[int(position[1]) -1][int(position[0])-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")