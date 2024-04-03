from turtle import *

# for i in range(12):
#     forward(50) #fd(100)
#     left(360/12) #lt(90)

def wielokat(dlugosc=50, boki=4):
    for i in range(boki):
        fd(dlugosc)
        lt(360/boki)

speed(20)
color('red')
for i in range(36):
    wielokat(100,6)
    left(360/36)