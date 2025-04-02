from turtle import *

def koch(bok, n):
    if n==0:
        fd(bok)
        return
    koch(bok/3, n-1)
    lt(60)
    koch(bok/3, n-1)
    rt(120)
    koch(bok/3, n-1)
    lt(60)
    koch(bok/3, n-1)
    
def skok(x,y):
    pu()
    goto(x,y)
    pd()
    
def platek():
    for i in range(3):
        koch(500,4)
        rt(120)
    
ht()
skok(-300, 250)
speed(0)
platek()