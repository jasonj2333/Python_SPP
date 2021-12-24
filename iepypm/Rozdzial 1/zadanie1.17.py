def zad_a(T):
    for P in T:
        print(P)

def zad_b(T):
    s = 1
    for P in T:
        for k in P:
            if k > 5:
                s *= k
    return s

def zad_c(T):
    s = 0
    for P in T:
        for k in P:
            if k != 0:
                s += 1
    return s

def zad_d(T):
    for P in T:
        for k in P:
            if k >= 20:
                return True
    return False

zad_a([[2, 3, 0, 5], [7, 6, 1, 0], [2, 9, 0, 5]])
print("iloczyn = ", zad_b([[2, 3, 0, 5], [7, 6, 1, 0], [2, 9, 0, 5]]))
print("ilość = ", zad_c([[2, 3, 0, 5], [7, 6, 1, 0], [2, 9, 0, 5]]))
if zad_d([[2, 3, 0, 5], [7, 6, 1, 0], [2, 9, 0, 5]]): print("TAK")
else: print("NIE")

