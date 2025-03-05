from turtle import *
import random

def koch0(bok):
    fd(bok)
    
def koch1(bok):
    koch0(bok/3)
    lt(60)
    koch0(bok/3)
    rt(120)
    koch0(bok/3)
    lt(60)
    koch0(bok/3)
    
def koch2(bok):
    koch1(bok/3)
    lt(60)
    koch1(bok/3)
    rt(120)
    koch1(bok/3)
    lt(60)
    koch1(bok/3)
    
def koch3(bok):
    koch2(bok/3)
    lt(60)
    koch2(bok/3)
    rt(120)
    koch2(bok/3)
    lt(60)
    koch2(bok/3)
    
def koch4(bok):
    koch3(bok/3)
    lt(60)
    koch3(bok/3)
    rt(120)
    koch3(bok/3)
    lt(60)
    koch3(bok/3)
    
def koch(bok, n):
    if n == 0:
        #colormode(255)
        #r = random.randint(0,255)
        #g = random.randint(0,255)
        #b = random.randint(0,255)
        #pencolor(colors[random.randint(0,2)])
        #pencolor((r,g,b))
        fd(bok)
        return
    
    koch(bok/3, n-1)
    lt(60)
    koch(bok/3, n-1)
    rt(120)
    koch(bok/3, n-1)
    lt(60)
    koch(bok/3, n-1)

def skok(x, y):
    pu()
    goto(x, y)
    pd()
    
def platek():
    for i in range(3):
        koch(500, 4)
        rt(120)

colors = ["red", "green", "blue"]
#screensize(1800, 600, "yellow")
speed(0)
skok(-300, 250)
platek()
ht()
    
    