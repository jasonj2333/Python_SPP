def zad_a(T):
    n = len(T)
    for i in range(n):
        if T[i] != 2:
            return True
    return False    

def zad_b(T):
    n = len(T)
    for i in range(n):
        if T[i] < 0:
            return False
    return True

def zad_c(T):
    n = len(T)
    for i in range(n):
        if T[i] < 5 or T[i] > 8:
            return True
    return False 

def zad_d(T):
    n = len(T)
    for i in range(n):
        if T[i] <= 11:
            return False
    return True 

def zad_e(T, k):
    n = len(T)
    for i in range(n):
        if T[i] == k:
            return True
    return False

print("zad_a = (lista) ", zad_a([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_b = (lista) ", zad_b([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_c = (lista) ", zad_c([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_d = (lista) ", zad_d([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_e = (lista) ", zad_e([3, 4, 5, 5, 7, 9, 4, 2, 1], 7))

print("zad_a = (krotka) ", zad_a((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_b = (krotka) ", zad_b((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_c = (krotka) ", zad_c((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_d = (krotka) ", zad_d((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_e = (krotka) ", zad_e((3, 4, 5, 5, 7, 9, 4, 2, 1), 7))
