def zad_a(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return 2 * n / s  

def zad_b(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

def zad_c(n):
    s = 1
    for i in range(1, n + 1):
        s *= (i + 3) / n
    return s

def zad_d(n):
    s = 0
    k = 3
    for i in range(1, n + 1):
        s += 2 * k / i
        k *= 2
    return s

print(zad_a(4))
print(zad_b(3))
print(zad_c(3))
print(zad_d(4))

