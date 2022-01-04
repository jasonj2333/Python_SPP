def zad_2(n):
    lp = 0
    while (n):
        lp += n % 2
        n //= 2
    return lp

print(zad_2(18))







