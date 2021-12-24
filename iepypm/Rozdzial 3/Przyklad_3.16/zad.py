from math import *

dane = open("dane.txt", "r")
wyniki = open("wyniki6.txt", "w")

def zad_1(K):
    maksimum, minimum = K[0][0], K[0][0]
    for i in range(200):
        for j in range(320):
            if K[i][j] < minimum: minimum = K[i][j]
            elif K[i][j] > maksimum: maksimum = K[i][j]
    wyniki.write('1)\n' + str(maksimum) + '\n' + str(minimum) + '\n')
    # print("najjaśniejszy piksel = ", maksimum)
    # print("najciemniejszy piksel = ", minimum)

def zad_2(K, i):
    for j in range(160):
        if K[i][j] != K[i][320 - j - 1]:
            return True
    return False
    
def zad_3(K):
    ilosc = 0
    for i in range(200):
        for j in range(320):
            if i + 1 < 200 and fabs(K[i][j] - K[i + 1][j]) > 128: ilosc += 1
            elif i - 1 >= 0 and fabs(K[i][j] - K[i - 1][j]) > 128: ilosc += 1
            elif j + 1 < 320 and fabs(K[i][j] - K[i][j + 1]) > 128: ilosc += 1
            elif j - 1 >= 0 and fabs(K[i][j] - K[i][j - 1]) > 128: ilosc += 1
    wyniki.write('\n3)\n' + str(ilosc) + '\n')
    # print('zad3 = ', ilosc)

def zad_4(K):
    linia_max = 0
    for j in range(320):
        linia_kolumna = 0
        for i in range(199):
            licznik = 1
            while i < 199 and K[i][j] == K[i + 1][j]:
                licznik += 1
                i += 1
            if licznik > linia_kolumna:
                linia_kolumna = licznik
        if linia_kolumna > linia_max:
            linia_max = linia_kolumna
    wyniki.write('\n4)\n' + str(linia_max))
    # print('zad4 = ', linia_max)

def zad():    
    K = [[0 for col in range(320)] for row in range(200)]
    DANE = dane.readlines()
    i = 0
    for linia in DANE:
        j = 0
        for pole in linia.split():
            K[i][j] = int(pole)
            j += 1
        i += 1    
    zad_1(K)
    ilosc = 0
    for i in range(200):
        if zad_2(K, i):
            ilosc += 1
    # print('zad2 = ',ilosc)
    wyniki.write('\n2)\n' + str(ilosc) + '\n')
    zad_3(K)
    zad_4(K)
    dane.close()        
    wyniki.close()

zad()

