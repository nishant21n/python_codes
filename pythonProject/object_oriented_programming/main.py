import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen  # Here's Turtle which is in PascalCase i.e. Class
a = 100
status = True
chandre = Turtle()
print(chandre)
chandre.color("coral")  # for color
chandre.shape("turtle")  # for shape
# chandre.speed("slowest")
while status:
    chandre.forward(a)  # for move
    chandre.right(45)  # Turn right in Degree of 90
    a -= 1
    if a == 0:
        status = False
my_screen = Screen()  # It's used for creating a screen
print(my_screen.canvheight)
my_screen.exitonclick()  # It  allows program to continue running until we click screen

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtla", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
