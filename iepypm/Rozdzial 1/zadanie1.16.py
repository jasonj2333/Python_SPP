def zad (m, n):
    T = [[0 for col in range(n)] for row in range(m)]
    for i in range(m):
        for j in range(n):
            T[i][j] = i * 5 + j * 2 + 1
        print(T[i])
      
zad(4, 3)


