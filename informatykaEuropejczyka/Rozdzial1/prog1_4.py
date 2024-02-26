#algorytm "delty" rozwiazujacy rownanie kwadratowe

from math import *

def rownanie_kwadratowe (a, b, c):
    if a==0:
        print("to nie jest rownanie kwadratowe")
    else: 
        delta=b*b-4*a*c
        if delta<0:
            print("rownanie nie ma pierwiastkow")
        elif delta==0:
            x1=-b/(2*a)
            print("x = ",x1)
        else:    
            x1=(-b-sqrt(delta))/(2*a)
            x2=(-b+sqrt(delta))/(2*a)
            print("x1 = ",x1,"\tx2 = ",x2)

#rownanie_kwadratowe(-2,2,4)
