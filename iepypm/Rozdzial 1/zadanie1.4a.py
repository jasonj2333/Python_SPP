from math import *

def zad_a(x):
    if x < 1:
        return 2 * x
    elif x == 1:
        return -10
    elif x == 3:
        return x ** 4
    elif x == 6:
        return sqrt(x - 4)
    else:
        return 0
    
print(zad_a(6))
