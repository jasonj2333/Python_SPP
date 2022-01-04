def silnia(n):
    if n == 0:
        return 1
    return silnia(n - 1) * n

def zad (n, k):
    if k >= 0 and k <= n:
        return silnia(n) / (silnia(k) * silnia(n - k))
    else: return "błędne dane"
 
print(zad(6, 4))
print(zad(5, 6))

