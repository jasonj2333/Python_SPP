# sortowanie przez wstawianie

def sortuj(T):
    n = len(T)
    for i in range(1, n):
        pom = T[i]
        k = i - 1
        while k >= 0 and T[k] > pom:
            T[k + 1] = T[k]
            k -= 1
        T[k + 1] = pom
    return T    

print(sortuj([3, 8, 2, 0, 5, 4, 1, 9]))


