# import colorgram
import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 42)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

turtle_module.colormode(255)
rio = turtle_module.Turtle()
rio.speed(0)
rio.penup()
rio.hideturtle()

color_list = [(2, 13, 31), (52, 25, 17), (219, 127, 106), (10, 105, 159), (241, 213, 69), (149, 83, 39), (214, 87, 64),
 (164, 162, 32), (157, 7, 24), (156, 63, 102),(11, 63, 32), (97, 6, 19), (206, 74, 104), (11, 96, 57), (172, 135, 162),
 (1, 63, 145), (8, 173, 216), (156, 34, 24),(5, 212, 207), (8, 139, 86), (146, 227, 216), (122, 193, 148),
 (101, 219, 229), (221, 178, 216), (253, 196, 0),(80, 135, 179), (121, 168, 189), (30, 84, 92), (228, 175, 166),
 (182, 191, 205), (68, 72, 42)]


rio.setheading(225)
rio.forward(300)
rio.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    rio.dot(20, random.choice(color_list))
    rio.forward(50)

    if dot_count % 10 == 0:
        rio.setheading(90)
        rio.forward(50)
        rio.setheading(180)
        rio.forward(500)
        rio.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()