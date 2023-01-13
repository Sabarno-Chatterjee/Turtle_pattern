from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
colours = ["red", "black", "blue", "green"]

for _ in range(3, 11):
    tim.color(random.choice(colours))
    for loop in range(_):
        tim.forward(100)
        tim.right(360/_)

for _ in range(3, 11):
    tim.color(random.choice(colours))
    for loop in range(_):
        tim.forward(100)
        tim.left(360/_)

tim.forward(200)
for _ in range(3, 11):
    tim.color(random.choice(colours))
    for loop in range(_):
        tim.forward(100)
        tim.left(360/_)
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.43)
#
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# for _ in range(5):
#     tim.forward(100)
#     tim.left(72)
#
# for _ in range(6):
#     tim.forward(100)
#     tim.left(60)
#
# for _ in range(7):
#     tim.forward(100)
#     tim.left(51.43)
#
# for _ in range(8):
#     tim.forward(100)
#     tim.left(45)
#
# for _ in range(9):
#     tim.forward(100)
#     tim.left(40)
#
# for _ in range(10):
#     tim.forward(100)
#     tim.left(36)
# num_of_sides = ["4","5","6","7","8","9","10"]
# for num in num_of_sides:
#     angle = 360 / int(num_of_sides[int(num)])
#     color = random.choice(colours)
#     tim.color(color)
#     tim.forward(100)
#     tim.right(angle)



screen = Screen()
screen.exitonclick()




