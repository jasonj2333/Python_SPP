def silnia_iter(n):
    wynik = 1
    
    if n > 0:
        for i in range(2, n+1):
            wynik *= i
    return wynik

def silnia_rek(n):
    if n == 0:
        return 1
    else:
        return n * silnia_rek(n-1)

n = 5

print(silnia_iter(n))
print(silnia_rek(n))