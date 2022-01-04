from math import *

def liczba_pierwsza(n):
    pom = int(sqrt(n)) + 1
    for i in range(2, pom):
        if n % i == 0:
            return False
    return True

def sprawdz(N):
    i = 2;
    while i <= sqrt(N):   
        if liczba_pierwsza(i):
            if N % i == 0:
                if liczba_pierwsza(N // i):
                    # print(N,' ',i,' ',N // i)
                    return True
        i += 1        
        while (not liczba_pierwsza(i)): 
            i += 1
    return False

def przepisz():
    dane = open("liczby.txt", "r")
    wyniki = open("zadanie5.txt", "w")
    for k in dane:
        if sprawdz(int(k)):
            wyniki.write(str(k))
    dane.close()
    wyniki.close()

przepisz()

 
