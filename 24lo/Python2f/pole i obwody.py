def menu():
    print("Wybierz jedną z opcji")
    print("1. Pole prostokąta")
    print("2. Obwod prostokąta")
    print("3. Pole kwadratu")
    print("4. Obwód kwadratu")
    opcja = input("Co wybierasz: ")
    oblicz(opcja)
    
def oblicz(opcja):
    wynik = ""
    if(opcja == '1'):
        bok1 = int( input("Podaj 1 bok: ") )
        bok2 = int( input("Podaj 2 bok: ") )
        wynik = f"Pole prostokąta o bokach {bok1}, {bok2} wynosi {pole_prostokata(bok1, bok2)}"
    elif(opcja == '2'):
        bok1 = int( input("Podaj 1 bok: ") )
        bok2 = int( input("Podaj 2 bok: ") )
        wynik = f"Obwod prostokąta o bokach {bok1}, {bok2} wynosi {obwod_prostokata(bok1, bok2)}"
    elif(opcja == '3'):
        bok1 = int( input("Podaj bok: ") )
        wynik = f"Pole kwadratu o boku {bok1} wynosi {pole_kwadratu(bok1)}"
    elif(opcja == '4'):
        bok1 = int( input("Podaj bok: ") )
        wynik = f"Obwód kwadratu o boku {bok1} wynosi {obwod_kwadratu(bok1)}"
    
    print(wynik)
    
def pole_prostokata(a, b):
    return a * b

def obwod_prostokata(a, b):
    return 2 * a + 2 * b

def pole_kwadratu(a):
    return pole_prostokata(a, a)

def obwod_kwadratu(a):
    return obwod_prostakata(a, a)

menu()