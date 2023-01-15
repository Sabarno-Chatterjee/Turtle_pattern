import turtle

import colorgram
from turtle import Turtle as t
import random


turtle.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_shade = (r, g, b)
#     rgb_colors.append(new_shade)
design_shades = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# def colour_generator():

tim = t()
my_screen = tim.getscreen()
tim.hideturtle()
tim.penup()
tim.speed(0)

# def design_pattern():
#     for _ in range(100):
#         color = random.choice(design_shades)
#         tim.color(color)
#         tim.dot(20)
#         tim.forward(50)


# design_pattern()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    color = random.choice(design_shades)
    tim.dot(20,color)
    tim.forward(50)
for _ in range(9):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    for _ in range(10):
        color = random.choice(design_shades)
        tim.dot(20,color)
        tim.forward(50)

turtle.exitonclick()