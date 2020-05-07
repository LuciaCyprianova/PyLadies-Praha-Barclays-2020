from turtle import shape, speed, forward, left, right, penup, pendown, exitonclick
from math import sqrt
shape("turtle")
speed(1)

n = int(input("Zadaj počet vrcholov pravidelného n-uholníka: "))

if n >= 3:
    l = 330 / n
    for i in range (n):
        forward(l)
        left(180 - (180 * (1 - (2/n))))
    exitonclick()

else:
    print("Taký n-uholník neexistuje.")