def zad_3():
    dane = open("slowa.txt", "r")
    wyniki = open("wyniki4.txt", "a")
    wyniki.write('\n3)\n')
    licznik, maks = 0, 0
    for s in dane:
        n = len(s) - 1
        for i in range(n):
            while s[i] == '1':
                i += 1 
            zera = 0
            while s[i] == '0':
                zera += 1
                i += 1
            if zera > maks:
                maks = zera
    dane.close()  
    dane = open("slowa.txt", "r")
    for s in dane:
        n = len(s) - 1
        for i in range(n):
            while s[i] == '1':
                i += 1 
            zera = 0
            while s[i] == '0':
                zera += 1
                i += 1;
            if zera == maks:
                wyniki.write(s)
                break
    wyniki.write('maks = ' + str(maks))
    dane.close();
    wyniki.close();
 
zad_3()

