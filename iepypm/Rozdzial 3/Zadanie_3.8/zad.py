from math import *

def liczba_pierwsza(n):
    pom = int(sqrt(n)) + 1
    for i in range(2, pom):
        if n % i == 0:
            return False
    return True

def przepisz():
    dane = open("liczby.txt", "r")
    wyniki = open("zad_5.txt", "w")
    for k in dane:
        k = int(k)
        if k == int(sqrt(k)) * int(sqrt(k)):
            if liczba_pierwsza(int(sqrt(k))): 
                wyniki.write(str(k) + '\n')
    dane.close()
    wyniki.close()

przepisz()

 
