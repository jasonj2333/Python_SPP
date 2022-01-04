def zad_b(n):
    for i in range(2, n):
        while n % i == 0: 
            print(i)
            n //= i

zad_b(36)





