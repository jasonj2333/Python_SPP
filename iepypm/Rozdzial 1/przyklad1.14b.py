def zad_a (T):
    for P in T:
        print(P)

def zad_b (T):
    s = 0
    for P in T:
        for k in P:
            if k % 3:
                s += k
    return s
              
zad_a([[2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]])
print("suma = ", zad_b([[2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]]))

