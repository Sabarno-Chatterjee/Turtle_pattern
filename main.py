import turtle
import colorgram
from turtle import Turtle as t
import random

turtle.colormode(255)

design_shades = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
                 (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                 (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                 (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                 (176, 192, 208), (168, 99, 102)]

tim = t()
my_screen = tim.getscreen()
tim.hideturtle()
tim.penup()
tim.speed(0)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for count_dots in range(1, number_of_dots + 1):
    color = random.choice(design_shades)
    tim.dot(10, color)
    tim.forward(50)
    if count_dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

turtle.exitonclick()
