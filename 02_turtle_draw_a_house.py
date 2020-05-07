from turtle import shape, speed, forward, left, right, penup, pendown, exitonclick
from math import sqrt
shape("turtle")
speed(1)

forward(60)
left(90)
forward(60)
left(90)
forward(60)

right(135)
forward((sqrt(2 * (60 ** 2))) / 2)
right(90)
forward((sqrt(2 * (60 ** 2))) / 2)

right(90)
forward(sqrt(2 * (60 ** 2)))
right(135)
forward(60)
right(135)
forward(sqrt(2 * (60 ** 2)))

exitonclick()