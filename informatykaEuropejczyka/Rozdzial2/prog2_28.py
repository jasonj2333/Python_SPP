#obliczanie pola obszaru ograniczonego wykresem funkcji, osia 0x i prostymi p, q - metoda trapezow

from math import *

def F (x):
    return -x**3-x**2+1

def oblicz (p, q, n):
    dl=(q-p)/n
    s=0
    for i in range(n):
        s+=fabs(F(p+i*dl))
    return dl/2*(fabs(F(p))+fabs(F(q))+2*s)

#print(oblicz(-2,5,30))

