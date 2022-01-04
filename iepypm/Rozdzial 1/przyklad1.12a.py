def zad_a(T):
    n = len(T)
    s = 0
    for i in range(n):
        s += T[i]
    return s    

def zad_b(T):
    n = len(T)
    s = 1
    for i in range(n):
        if T[i] < 6:
            s *= T[i]
    return s    

def zad_c(T):
    n = len(T)
    s = 0
    for i in range(n):
        if i % 5 != 0:
            s += 1
    return s

def zad_d(T):
    for i in range(3, 8, 2):
        T[i] = 0
    return T  

print("zad_a (lista) = ", zad_a([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_b (lista) = ", zad_b([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_c (lista) = ", zad_c([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_d (lista) = ", zad_d([3, 4, 5, 5, 7, 9, 4, 2, 1]))

print("zad_a (krotka) = ", zad_a((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_b (krotka) = ", zad_b((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_c (krotka) = ", zad_c((3, 4, 5, 5, 7, 9, 4, 2, 1)))

