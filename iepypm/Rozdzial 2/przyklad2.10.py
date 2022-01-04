# sortowanie przez wybór

def sortuj(T):
    n = len(T)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if T[j] < T[k]:
                k = j
        T[k], T[i] = T[i], T[k]
    return T    

print(sortuj([1, 8, 6, 0, 5, 4, 3, 7]))


