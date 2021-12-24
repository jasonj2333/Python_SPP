def zad_2(A, p):
    pierwsza, druga = 0, 0
    for j in A:
        if j % p != 0:
            if j > pierwsza:
                druga = pierwsza
                pierwsza = j
            elif j > druga: druga = j
    S = pierwsza * druga
    return S
 
print(zad_2([6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18], 7))
print(zad_2([4, 34, 16, 8, 6, 22, 14, 12, 2, 7], 2))
print(zad_2([15, 12, 10, 6, 5, 1], 5))
print(zad_2([7, 5, 11, 33], 3))


