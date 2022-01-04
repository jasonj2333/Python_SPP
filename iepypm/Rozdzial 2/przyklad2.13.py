# sortowanie szybkie - rekurencja

def sortuj(T, lewy, prawy):
    i, j = lewy, prawy
    srodek = T[(lewy + prawy) // 2]
    while i <= j:
        while T[i] < srodek:
            i += 1
        while T[j] > srodek:
            j -= 1
        if i <= j:
            T[i], T[j] = T[j], T[i]
            i, j = i + 1, j - 1
    if lewy < j:
        sortuj(T, lewy, j)
    if prawy > i:
        sortuj(T, i, prawy)

def sortujszybko(T):
    n = len(T)
    sortuj(T, 0, n - 1)
    return T

print(sortujszybko([9, 8, 7, 6, 5, 4, 2, 1, 0]))

