def zad_a(T, m):
    for i in range(m):
        print(T[i])

def zad_b(T, m, n):
    s = 0
    for i in range(m):
        for j in range(n):
            if T[i][j] % 3:
                s += T[i][j]
    return s

def zad_c(T, m, n):
    for i in range(m):
        for j in range(n):
            if i != j:
                T[i][j] -= 3
        print(T[i])
               
zad_a([[2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]], 3)
print("suma = ", zad_b([[2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]], 3, 4))
zad_c([[2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]], 3, 4)

