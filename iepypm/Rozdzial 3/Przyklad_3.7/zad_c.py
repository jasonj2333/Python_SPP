def oblicz(A, p):
    n = len(A)
    w = A[0]
    for i in range(1, n):
        w = w * p + A[i]
    return w    

print(oblicz([1, 0, 1, 1, 1, 0, 1], 2))
print(oblicz([1, 1, 2], 3))
print(oblicz([4, 5, 6], 8))

