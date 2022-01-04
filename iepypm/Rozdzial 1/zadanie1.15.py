def zad_a(T, m):
    for i in range(m):
        print(T[i])

def zad_b(T, m):
    for i in range(m):
        T[i][1], T[i][2] = T[i][2], T[i][1]
    zad_a(T, m)
   
def zad_c(T, m, w1, w2):
    T[w1], T[w2] = T[w2], T[w1]
    zad_a(T, m)
                
zad_a([[2, 3, 4, 7], [7, 6, 4, 2], [8, 9, 4, 1]], 3)
print()
zad_b([[2, 3, 4, 7], [7, 6, 4, 2], [8, 9, 4, 1]], 3)
print()
zad_c([[2, 3, 4, 7], [7, 6, 4, 2], [8, 9, 4, 1]], 3, 0, 2)

