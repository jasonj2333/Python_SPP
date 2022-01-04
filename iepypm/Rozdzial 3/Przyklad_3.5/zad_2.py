def zad_2(a):
    b, b1 = 0, 0
    for i in range(2, a // 2 + 1):
        if a % i == 0: b += i
    for i in range(2, b // 2 + 1): 
        if b % i == 0: b1 += i
    if a == b1: print(b)
    else: print("NIE")

zad_2(75)







