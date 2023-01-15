import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(0)


for _ in range(10000):
    tim.pencolor(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = t.Screen()
screen.exitonclick()
