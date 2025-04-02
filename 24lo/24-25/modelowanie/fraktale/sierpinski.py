from turtle import *

def trojkat(bok, n):
    if n == 0:
        for i in range(3):
            fd(bok)
            lt(120)
    else:
        trojkat(bok/2, n-1)
        fd(bok/2)
        trojkat(bok/2, n-1)
        bk(bok/2)
        lt(60)
        fd(bok/2)
        rt(60)
        trojkat(bok/2, n-1)
        lt(60)
        bk(bok/2)
        rt(60)
        
def skok(x, y):
    pu()
    goto(x, y)
    pd()
        
speed(0)
skok(-200, -100)
trojkat(400, 5)