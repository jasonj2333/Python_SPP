def zad_c(n):
    B = [[0 for col in range(n + 1)] for row in range(n + 1)]
    for i in range(n + 1):
        B[i][i] = 1
        B[i][0] = 1
    for i in range (2, n + 1):
        for j in range(1, i):
            B[i][j] = B[i - 1][j - 1] + B[i - 1][j];  
    for i in range(n + 1):
        print(B[i])

zad_c(5)


