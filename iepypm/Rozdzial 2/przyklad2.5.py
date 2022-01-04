# liniowe przeszukiwanie ciągu liczbowego

def szukaj1(T, szukana):
    i = 0
    n = len(T)
    while i < n and T[i] != szukana:
        i += 1
    if i == n:
        return False
    return True

def szukaj2(T, szukana):
    if szukana in T:
        return True
    else:
        return False

def szukaj3(T, szukana):
    return szukana in T

print(szukaj1([7, 5, 6, 4, 5, 3, 4, 8, 2, 3], 8))
print(szukaj2([7, 5, 6, 4, 5, 3, 4, 8, 2, 3], 9))
print(szukaj3([7, 5, 6, 4, 5, 3, 4, 8, 2, 3], 8))

