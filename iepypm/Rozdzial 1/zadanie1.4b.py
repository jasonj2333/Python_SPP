from math import *

def zad_b(x):
    if x < 7:
        return x ** 3 + 1
    elif x == 7:
        return x - 1
    elif x == 9:
        return sqrt(3 * x)
    else:
        return -8 * x
    
print(zad_b(3))
