def zad_4(mk, n, MASA, CENA):
    K = [0 for row in range(n + 1)]
    w = 0
    i = 0     
    while i <= n and mk > 0:
        if MASA[i] <= mk: 
            K[i] = 1
            mk -= MASA[i]
            w += CENA[i]
        i += 1   
    for i in range(n):
        print("nr ", i + 1, " = ", K[i])
    print("wartość zabawek = ", w)
    
zad_4(10, 7, [8, 4, 1, 2, 3, 5, 1], [320, 152, 37, 70, 99, 155, 30])





