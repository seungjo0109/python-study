# Turtle example
# from turtle import Turtle, Screen

# # Create object
# timmy = Turtle()
# my_screen = Screen()

# # Set object attribute
# timmy.speed = 6
# print(my_screen.canvheight)

# # Method
# timmy.color("coral")
# timmy.shape("turtle")
# timmy.forward(100)

# my_screen.exitonclick()

# Pretty table
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pockemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)



