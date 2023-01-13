from turtle import Turtle, Screen
import random


def shape_shifter(num_of_sides):
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(360 / num_of_sides)


tim = Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed(0)
colours = ["red", "black", "blue", "green", "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
           "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown",
           "black", "gray"]

# for num_of_sides in range(3, 11):
#     tim.pencolor(random.choice(colours))
#     shape_shifter(num_of_sides)
# for movement in range(100000):
#     tim.color(random.choice(colours))
#     direction = random.randint(0,1)
#     if direction:
#         tim.left(90)
#         tim.forward(20)
#     else:
#         tim.right(90)
#         tim.forward(20)

directions = [0, 90, 180, 270]
for _ in range(300):
    tim.pencolor(random.choice(colours))
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = Screen()
screen.exitonclick()
