def zad_c(a, n):
    p = a
    while n > 1:
        p *= p
        n //= 2
    return p    
        
print(zad_c(2, 4))
