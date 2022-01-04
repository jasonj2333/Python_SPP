# badanie, czy liczba jest pierwsza

from math import *

def liczba_pierwsza1(n):
    pom = int(sqrt(n))
    for i in range(2, pom + 1):
        if n % i == 0:
            return False
    return True

def liczba_pierwsza2(n):
    pom = int(sqrt(n))
    i = 2
    while i <= pom:
        if n % i == 0:
            return False
        i += 1
    return True
                    
print(liczba_pierwsza1(61))
print(liczba_pierwsza2(105)) 

