from turtle import *

def trojkat_sierpinskiego(bok, n):
    if n == 0:
        for i in range(3):
            fd(bok)
            lt(120)
    else:
        trojkat_sierpinskiego(bok/2, n-1)
        fd(bok/2)
        trojkat_sierpinskiego(bok/2, n-1)
        bk(bok/2)
        lt(60)
        fd(bok/2)
        rt(60)
        trojkat_sierpinskiego(bok/2, n-1)
        lt(60)
        bk(bok/2)
        rt(60)

speed(0)            
trojkat_sierpinskiego(400, 3)