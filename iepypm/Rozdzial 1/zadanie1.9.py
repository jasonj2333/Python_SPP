def zad_a(n):
    s=0
    k=2
    for i in range(1, n + 1):
        if i % 2: s -= k
        else: s += k
        k += 3
    return s  

def zad_b(n):
    s = 1
    k = 4
    for i in range(1, n + 1):
        if i % 2: s *= k
        else: s *= -k
        k += 4
    return s

def zad_c(n):
    s = 0
    k = 1
    for i in range(1, n + 1):
        k *= i
        s += k
    return s

def zad_d(n):
    s1 = 0
    s2 = 1
    k2 = 2
    for i in range(1, n + 1):
        s1 += i
        s2 *= k2
        k2 += 4
    return s1 / s2

def zad_e(n):
    s1 = 1
    k1 = 2
    s2 = 1
    k2 = -3
    for i in range(1, n + 1):
        s1 *= k1
        k1 += 0.5
        s2 *= k2
        k2 *= 0.1
    return s1 / s2

def zad_f(n):
    s1 = 0
    k1 = 1
    s2 = 0
    k2 = -0.2
    for i in range(1, n + 1):
        k1 *= i
        if i % 2: s1 += k1
        else: s1 -= k1
        s2 += k2
        k2 += 0.3
    return s1 / s2

def zad_g(n):
    s1 = 0
    k1 = 2
    s2 = 1
    k2 = 3
    for i in range(1, n + 1):
        if i % 2:
            s1 -= k1
            s2 *= k2
        else:
            s1 += k1
            s2 *= -k2
        k1 += 5
        k2 += 4
    return s1 / s2

def zad_h(n):
    s1 = 1
    k1 = 1
    s2 = 0
    for i in range(1, n + 1):
        k1 *= i
        if i % 2: s1 *= n ** 2 / k1
        else: s1 *= -n ** 2 / k1
        s2 += 1 / 3
    return s1 / s2

print(zad_a(4))
print(zad_b(3))
print(zad_c(3))
print(zad_d(4))
print(zad_e(2))
print(zad_f(3))
print(zad_g(3))
print(zad_h(2))


