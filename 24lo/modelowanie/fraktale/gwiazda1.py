from turtle import *
#import turtle as t

def fragment(bok):
    fd(bok/3); rt(60)
    fd(bok/3); lt(120)
    fd(bok/3); rt(60)
    fd(bok/3)
    
def gwiazda(bok):
    for i in range(4):
        fragment(bok)
        lt(90)
    
gwiazda(300)