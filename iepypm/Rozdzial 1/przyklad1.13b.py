def zad_a(T):
    for k in T:
        if k != 2:
            return True
    return False    

def zad_b(T):
    for k in T:
        if k < 0:
            return False
    return True

def zad_c(T):
    for k in T:
        if k < 5 or k > 8:
            return True
    return False 

def zad_d(T):
    for k in T:
        if k <= 11:
            return False
    return True 

def zad_e (T, k):
    if k in T:
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
