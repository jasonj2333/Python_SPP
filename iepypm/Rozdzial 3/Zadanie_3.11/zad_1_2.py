def zad_1_2():
    dane = open("slowa.txt", "r")
    wyniki = open("wyniki4.txt", "w")
    licznik1, licznik2 = 0, 0
    for s in dane:
        zera = 0
        n = len(s) - 1
        for i in range(n):
            if s[i] == '0': zera += 1 
        if zera > n - zera: licznik1 += 1  
        if s[0] == '0':
            poprzedni = '0'
            zmiana = 0
            for i in range(1, n):
                if s[i] != poprzedni:
                    zmiana += 1
                    poprzedni = s[i]
            if zmiana == 1:
                licznik2 += 1  
    wyniki.write('1)\n' + str(licznik1) + '\n')
    wyniki.write('\n2)\n' + str(licznik2) + '\n')
    dane.close()
    wyniki.close()

zad_1_2()

