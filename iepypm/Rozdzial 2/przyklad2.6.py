# algorytm sprawdzający, czy w ciągu znajduje się liczba podzielna przez 7

def szukaj1(T):
    n = len(T)
    for i in range(n):
        if T[i] % 7 == 0:
            return True
    return False

def szukaj2(T):
    for k in T:
        if k % 7 == 0:
            return True
    return False

print(szukaj1([7, 5, 6, 4, 5, 3, 4, 8, 2, 3]))
print(szukaj2([9, 5, 6, 4, 5, 3, 4, 8, 2, 3]))
