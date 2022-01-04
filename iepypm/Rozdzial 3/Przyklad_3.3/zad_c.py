def zad_c(n):
    for s in range(4, 33):
        k = n - s
        suma = k % 10 + (k // 10) % 10 + (k // 100) % 10 + (k // 1000) % 10     
        if suma == s: return k
    return 0

wynik = zad_c(28)
if wynik != 0: print(wynik)
else: print("NIE")






