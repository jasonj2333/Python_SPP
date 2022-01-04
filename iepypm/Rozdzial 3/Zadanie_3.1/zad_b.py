def zad_b(n):
    if n == 1: ss = 1
    else: 
        ss = 1 + n
        i = n - 1
        while i > 1:
            ss = 1 + i * ss
            i -= 1
    return ss;
    
print(zad_b(4))

