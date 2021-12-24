from math import *

def pierwsza(n):
    if n < 2 or n % 2 == 0: return False
    pom = int(sqrt(n))
    for i in range(3, pom + 1, 2):
        if n % i == 0: return False
    return True      

def oblicz(s):
    suma = 0
    for i in range(len(s) - 1):
        suma += ord(s[i])
    return suma     

def rosnacy(s):
    for i in range(len(s) - 2):
        if s[i] >= s[i + 1]: return False
    return True     

def sortujslowa(lista):
    n = len(lista)   
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

def zad_a_b():
    dane = open("napis.txt", "r")
    wyniki = open("zadanie5.txt", "w")
    a = 0
    wyniki.write('b)\n')
    for s in dane:
        if pierwsza(oblicz(s)):
            a += 1
        if rosnacy(s):
            wyniki.write(s)
    wyniki.write('\na)\n' + str(a) + '\n')
    dane.close()
    wyniki.close()

def zad_c():    
    dane = open("napis.txt", "r")
    wyniki = open("zadanie5.txt", "a")
    wyniki.write('\nc)\n')
    lista = dane.readlines()
    sortujslowa(lista)
    n = len(lista)
    for i in range(2, n):
        if lista[i - 1] == lista[i - 2] and lista[i -1] != lista[i]:
            wyniki.write(lista[i - 1])
    dane.close()        
    wyniki.close()

zad_a_b()
zad_c()
