def zad_a(n):
    if n == 1:
        return 4
    return zad_a(n - 1) + 3

def zad_b(n):
    if n == 1:
        return 2
    return zad_b(n - 1) * 2
 
def zad_c(n):
    if n == 1:
        return 2
    return zad_c(n - 1) * -3

def zad_d(n):
    if n == 1:
        return -10
    return zad_d(n - 1) / -2

def zad_e(n):
    if n == 1: return 3
    if n == 2: return 5
    return zad_e(n - 2) + 1

def zad_f(n):
    if n == 1: return 1.5
    if n == 2: return 1
    return zad_f(n - 2) + zad_f(n - 1) - 2
 
def zad_g(n):
    if n == 1: return -3
    if n == 2: return 1
    return zad_g(n - 2) * zad_g(n - 1) - 1
 
def zad_h(n):
    if n == 1: return -2
    if n == 2: return 2.5
    if n == 3: return 3
    return zad_h(n - 3) - zad_h(n - 1)
 
def zad_i(n):
    if n == 1: return -1
    if n == 2: return 0
    if n == 3: return 0.5
    return zad_i(n - 1) - zad_i(n - 3)
 
def zad_j(n):
    if n == 1: return 0
    if n == 2: return 1
    if n == 3: return -1
    return zad_j(n - 3) + zad_j(n - 2) - zad_j(n - 1)

print(zad_a(6))
print(zad_b(5))
print(zad_c(6))
print(zad_d(5))
print(zad_e(4))
print(zad_f(5))
print(zad_g(6))
print(zad_h(5))
print(zad_i(4))
print(zad_j(5))


