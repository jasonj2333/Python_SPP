def zad_a(T):
    print(T)

def zad_b(T):
    n = len(T)
    s = 0
    for i in range(n):
        if i % 5:
            s += 1
    return s

def zad_c(T):
    n = len(T)
    for i in range(n):
        if i % 2 and i >= 3 and i <= 8:
            T[i] += 2
    print(T)

def zad_d(T):
    for k in T:
        if k < 0:
            return False
    return True 

def zad_e(T):
    s = 1
    for k in T:
        if k == 5:
            s *= k
    return s

def zad_f(T):
    for k in T:
        if k < 5 or k > 8:
            return True
    return False

zad_a([9, 4, 3, 5, 7, 9, 4, 2, 1, 5])
print(zad_b([9, 4, 3, 5, 7, 9, 4, 2, 1, 5]))
zad_c([9, 4, 3, 5, 7, 9, 4, 2, 1, 5])
if zad_d([9, 4, 3, 5, 7, 9, 4, 2, 1, 5]): print("TAK")
else: print("NIE")
print(zad_e([9, 4, 3, 5, 7, 9, 4, 2, 1, 5]))
if zad_f([9, 4, 3, 5, 7, 9, 4, 2, 1, 5]): print("TAK")
else: print("NIE")
