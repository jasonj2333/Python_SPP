def zad_d(liczba):
    if liczba > 4 and liczba < 767:
        W = [0 for row in range(11)]
        i = 0
        l = liczba
        while l != 0:
            W[i] = l % 2
            l //= 2
            i += 1
        print(liczba, "(10) = ", W[::-1], "(2)")
        suma = 0;
        for j in W:
            suma += j;
        if W[i - 2] == 0 and suma % 2 == 0: print("otwarte")
        else: print("zamknięte")
    else: print("zamknięte")

zad_d(766)
