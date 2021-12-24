def zad_b(k):
    if k == 0: return 1
    else:
        r = k % 4
        if r == 0: return 6
        elif r == 1: return 2
        elif r == 2: return 4
        elif r == 3: return 8
    
print(zad_b(11))

