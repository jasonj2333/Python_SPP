from turtle import *

def wielokat(liczbaBokow, dlugosc):
    for i in range(liczbaBokow):
        forward(dlugosc)
        left(360 / liczbaBokow)

penup()
backward(200)
left(90)
forward(100)
pendown()
wielokat(9, 50)
penup()
goto(100, 200)
pendown()
color("red")
pensize(5)
wielokat(4, 100)
done()