#algorytm sprawdzajacy, czy punkt P lezy na prostej 3x+4y-4 = 0

from math import *
       
def szukaj (x0, y0):
    d=fabs(3*x0+4*y0-4)/sqrt(3.0**2+4.0**2)
    if d==0:
        return True
    return False

#print(szukaj(2.5,3))

