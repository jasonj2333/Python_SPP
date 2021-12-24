def zad_b(n):
    wynik = 1
    while n > 1:
        if n % 2 == 0: n //= 4
        else: n = 3 * n + 1
        wynik += 1
    return wynik
 
print(zad_b(31))
