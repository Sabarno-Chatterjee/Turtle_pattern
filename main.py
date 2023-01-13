from turtle import Turtle, Screen
import random


def shape_shifter(num_of_sides):
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(360 / num_of_sides)


tim = Turtle()
tim.shape("turtle")
colours = ["red", "black", "blue", "green", "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
           "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown",
           "black", "gray"]

for num_of_sides in range(3, 11):
    tim.pencolor(random.choice(colours))
    shape_shifter(num_of_sides)

screen = Screen()
screen.exitonclick()
