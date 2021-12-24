def zad_b():
    a, b, c = 3, -2, 10
    if a + b < c:
        a *= 2
        b -= 1
        if c > 0:
            c += a
        else:
            c += b
    else: c += a * b  
    return a, b, c
    
print(zad_b())
