#importowanie z biblioteki math funkcji floor(zaokrąglanie w dół) oraz sqrt(pierwiastek kwadratowy)
from math import floor, sqrt

def jest_pierwsza(n):
    m = floor( sqrt(n) ) #pierwiastek z n zaokrąglony w dół
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True

stop = int( input("Podaj górną granicę przedziału: ") )
print(f"Liczby pierwsze z przedziału od 2 do {stop}")

for i in range(2, stop+1):
    if( jest_pierwsza(i) ):
        print(i, end=", ")
        
#można to zrobić lepiej - patrz Sito Erastotenesa