#algorytm sprawdzajacy, czy punkt P=(3;-2) nalezy do odcinka AB

from math import *
       
def szukaj (x1, y1, x2, y2):
    AB=sqrt((x2-x1)**2+(y2-y1)**2)
    AP=sqrt((3-x1)**2+(-2-y1)**2)
    PB=sqrt((x2-3)**2+(y2+2)**2)
    if AP+PB==AB:
        return True
    return False

#print(szukaj(2,-3,4,-1))

