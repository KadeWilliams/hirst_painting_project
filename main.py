import random
import turtle as t
from turtle import Turtle, Screen

# Get the list of top colors
# import colorgram as c
# top_colors = c.extract('dot.jpg', 30)
# colors = []
# for color in range(len(top_colors)):
#     rgb = top_colors[color].rgb
#     colors.append((rgb.r, rgb.g, rgb.b))

t.colormode(255)
circle = Turtle()

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
              (46, 73, 62), (47, 66, 82)]


def straight_line_of_dots():
    circle.speed(20)
    circle.hideturtle()
    number_of_dots = 101
    circle.penup()
    x = -225
    y = -225
    circle.setx(x)
    circle.sety(y)
    for dot_count in range(1, number_of_dots):
        circle.dot(20, random.choice(color_list))
        circle.forward(50)
        y = circle.ycor()
        if dot_count % 10 == 0:
            circle.goto(x, y + 50)


straight_line_of_dots()

my_screen = Screen()
my_screen.exitonclick()
