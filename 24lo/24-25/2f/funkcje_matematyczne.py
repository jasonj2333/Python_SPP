def pole_prostokata(a, b):
    wynik = a * b
    return wynik

print( pole_prostokata(5,7) )

pokoj1 = pole_prostokata(2,3)
pokoj2 = pole_prostokata(3,3)
pokoj3 = pole_prostokata(4,2)
mieszkanie = pokoj1 + pokoj2 + pokoj3
print(f"Pole powierzchni mieszkania wynosi {mieszkanie}")

def obwod_prostokata(a, b):
    return 2*a + 2*b

print( obwod_prostokata(3,7) )

def modul(a):
    if a < 0:
        return -a
    else:
        return a

print( modul(-7) )
print( modul(4) )
    

