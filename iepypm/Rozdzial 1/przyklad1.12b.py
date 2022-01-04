def zad_a(T):
    s = 0
    for k in T:
        s += k
    return s    

def zad_b(T):
    s = 1
    for k in T:
        if k < 6:
            s *= k
    return s    

print("zad_a (lista) = ", zad_a([3, 4, 5, 5, 7, 9, 4, 2, 1]))
print("zad_b (lista) = ", zad_b([3, 4, 5, 5, 7, 9, 4, 2, 1]))

print("zad_a (krotka) = ", zad_a((3, 4, 5, 5, 7, 9, 4, 2, 1)))
print("zad_b (krotka) = ", zad_b((3, 4, 5, 5, 7, 9, 4, 2, 1)))





