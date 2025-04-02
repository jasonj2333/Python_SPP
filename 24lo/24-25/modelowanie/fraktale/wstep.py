from turtle import *

# for i in range(12):
#     lt(360/12)
#     fd(100)

def wielokat(dlugosc=50, boki=4):
    for i in range(boki):
        fd(dlugosc)
        lt(360/boki)

speed(100)
for i in range(36):
    wielokat(100,4)
    lt(360/36)