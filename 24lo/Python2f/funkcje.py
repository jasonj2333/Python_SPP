import math

#definicja funkcji
#funkcja witaj() jest funkcją nie zwracająca wartości
def witaj(imie="Wacek"): #parametr imie ma wartość domyślną "Wacek"
    print(f"Cześć {imie}")

#wywołania funkcji 
witaj("Tomek")
witaj("Ania")
witaj()

#funkcja pole_prostokata(a, b) jest funkcją zwracająca dane
#posiada dwa parametry a i b
def pole_prostokata(a, b):
    if a <= 0 or b <= 0:
        return -1
    return a * b

#wywołanie funkcji pole_prostokata z argumentami 5, 7
#funkcja zwraca wartość pola lub kod błędu (-1)
#zwracaną wartość zapamiętujemy w zmiennej pole
pole = pole_prostokata(5, 7)
if pole != -1:
    print(f"Pole prostokata = {pole}")
else:
    print("To nie są boki prostokąta")

#cwiczenie 
def pole_kola(r):
    if r <= 0:
        return -1
    return math.pi * r * r

pole = pole_kola(5)
if pole != -1:
    print(f"Pole koła = {pole}")
else:
    print("Promień musi być większy od zera")
    
#cwiczenie - pole_kwadratu
def pole_kwadratu(a):
    #funkcja wywołuje wcześniej zdefiniowaną funkcje pole_prostokata()
    return pole_prostokata(a, a)

pole = pole_kwadratu(5)
print(pole)