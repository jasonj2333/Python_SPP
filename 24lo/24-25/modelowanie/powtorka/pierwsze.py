# K01: g ← [sqr(p)] ; wyznaczamy granicę sprawdzania podzielności p
# K02: Dla i = 2, 3, …, g: ; przebiegamy przez przedział <2, [√p]>
#      wykonuj krok K03
# K03:   Jeśli p mod i = 0, ; jeśli liczba z przedziału <2, [√p]> dzieli p, 
#        to pisz NIE i zakończ ; to p nie jest pierwsze
# K04: Pisz TAK ; jeśli żadna liczba z <2, [√p]> nie dzieli p, p jest pierwsze
# K05: Zakończ
from math import sqrt

def pierwsza(liczba):
    g = int( sqrt(liczba) )
    for i in range(2, g+1):
        if liczba % i == 0:
            return False
    return True

print( pierwsza(16) )
print( pierwsza(83) )
            
            
    
    
    