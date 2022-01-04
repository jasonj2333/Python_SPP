# sito Eratostenesa - generowanie liczb pierwszych

def generuj(n):    
    T = [0]
    for i in range(1, n + 1):
        T += [1]
    i = 2
    while i <= n:
        if T[i] == 0:
            i = i + 1
        m = 2 * i
        while m <= n:
           T[m] = 0
           m = m + i
        i = i + 1
    for indeks, wartosc in enumerate(T):
        if wartosc == 1 and indeks > 1:
            print(indeks)

generuj(40)
