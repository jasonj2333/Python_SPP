# algorytm sprawdzający, czy wszystkie elementy ciągu są większe od 5

def szukaj1(T):
    n = len(T)
    for i in range(n):
        if T[i] <= 5:
            return False
    return True

def szukaj2(T):
    for k in T:
        if k <= 5:
            return False
    return True

print(szukaj1([7, 9, 6, 8, 7, 7, 11, 9, 8, 8]))
print(szukaj2([7, 9, 6, 8, 7, 7, 11, 9, 8, 1]))

