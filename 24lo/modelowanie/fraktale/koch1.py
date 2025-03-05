from turtle import *

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
    
def koch(bok, n):
    if n == 0:
        fd(bok)
        return
    koch(bok/3, n-1)
    lt(60)
    koch(bok/3, n-1)
    rt(120)
    koch(bok/3, n-1)
    lt(60)
    koch(bok/3, n-1)
ht()
speed(0)
koch(400, 4)