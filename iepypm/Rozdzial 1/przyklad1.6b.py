def zad_b(n):
    k = -4
    s = 0
    for i in range(n):
    #for i in range(1, n + 1, 1):
        s += k
        k += 5
    return s    
    
print(zad_b(4))
