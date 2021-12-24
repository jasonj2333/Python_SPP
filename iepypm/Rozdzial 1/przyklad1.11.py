def zad_a(n):
    if n == 1:
        return 3
    return zad_a(n - 1) + 3 

def zad_b(n):
    if n == 1:
        return -2
    return zad_b(n - 1) * -2

def zad_c(n):
    if n == 1:
        return 8
    return zad_c(n - 1) / -2 

def zad_d(n):
    if n == 1: return 2
    if n == 2: return 6
    return zad_d(n - 2) + 1 

def zad_e(n):
    if n == 1: return -1
    if n == 2: return 4
    if n == 3: return -4
    return zad_e(n - 2) * zad_e(n - 1)

def zad_f(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return -4
    return zad_f(n - 3) + zad_f(n - 1) 

print(zad_a(5))
print(zad_b(6))
print(zad_c(6))
print(zad_d(7))
print(zad_e(6))
print(zad_f(6))
