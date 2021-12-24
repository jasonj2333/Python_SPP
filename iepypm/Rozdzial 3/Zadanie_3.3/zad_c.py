def zad_c(n):
    s = ''
    while n > 0:
        if n % 2 == 0: s = 'B' + s
        else: s = 'C' + s
        n //= 2       
    return s 

print(zad_c(16))







