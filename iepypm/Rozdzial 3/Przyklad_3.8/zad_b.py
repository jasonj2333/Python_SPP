def zad_b(A, B, n, p):
    C = [0 for row in range(n + 1)]
    dalej = 0
    for i in range(n, -1, -1):
        pom = A[i] + B[i] + dalej
        C[i] = pom % p
        dalej = pom // p
    return C    

print(zad_b([0, 1, 2, 2, 2], [0, 1, 0, 1, 1], 4, 4))
print(zad_b([0, 1, 2, 3, 2], [0, 2, 2, 0, 1], 4, 4))
print(zad_b([0, 2, 0, 0, 1, 2], [0, 0, 1, 2, 2, 1], 5, 3))

