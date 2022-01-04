from math import *

def zad(a, b, c):
    p = (a + b + c) / 2
    pp = p * (p - a) * (p - b) * (p - c)
    if pp >= 0:
        return sqrt(pp)
    else:
        return "trójkąt nie istnieje"
    
print(zad(3, 5, 9))
print(zad(3, 4, 6))

