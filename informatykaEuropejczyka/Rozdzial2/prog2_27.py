#obliczanie pola ograniczonego wykresem funkcji, osia 0x i prostymi p, q - metoda prostokatow

from math import *

def F (x):
    return x**2-x-3

def oblicz (p, q, n):
    dl=(q-p)/n
    s=0
    for i in range(n):
        s+=fabs(F(p+dl*i+dl/2))
    return dl*s

#print(oblicz(-2,5,30))
