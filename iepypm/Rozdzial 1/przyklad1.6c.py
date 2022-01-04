def zad_c(n):
    k = -1
    s = 1
    for i in range(n):
    #for i in range(1, n + 1, 1):
        s *= k
        k *= -2
    return s    
    
print(zad_c(3))

