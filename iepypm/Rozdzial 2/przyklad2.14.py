# algorytm Newtona-Raphsona wyznaczający wartość pierwiastka kwadratowego
# z liczby nieujemnej

from math import *

def pierwiastek(p, E, L):
    a = p
    i = 0;
    while fabs(a - p / a) > E and i < L:
        a = (a + p / a) / 2
        i += 1
    return a

print(pierwiastek(10, 0.00001, 50))



