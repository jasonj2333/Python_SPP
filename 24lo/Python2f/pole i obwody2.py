def menu():
    print("Program oblicza pole i obwód figur")
    print("1. Pole prostokąta")
    print("2. Obwód prostokąta")
    print("3. Pole kwadratu")
    print("4. Obwód kwadratu")
    opcja = input("Wybierz jedną z opcji: ")
    oblicz(opcja)
    
def oblicz(opcja):
    zwroc = ""
    if opcja == '1':
        bok1 = int( input("Podaj 1 bok: ") )
        bok2 = int( input("Podaj 2 bok: ") )
        wynik = pole_prostokata(bok1, bok2)
        zwroc = f"Pole prostokąta o bokach {bok1}, {bok2} wynosi {wynik}"
    elif opcja == '2':
        bok1 = int( input("Podaj 1 bok: ") )
        bok2 = int( input("Podaj 2 bok: ") )
        wynik = obwod_prostokata(bok1, bok2)
        zwroc = f"Obwód prostokąta o bokach {bok1}, {bok2} wynosi {wynik}"
    elif opcja == '3':
        bok1 = int( input("Podaj bok: ") )
        wynik = pole_kwadratu(bok1)
        zwroc = f"Pole kwadratu o boku {bok1} wynosi {wynik}"
    
    print(zwroc)
    
def pole_prostokata(a, b):
    return a * b

def obwod_prostokata(a, b):
    return 2 * a + 2 * b

def pole_kwadratu(a):
    return pole_prostokata(a, a)

def obwod_kwadratu(a):
    return obwod_prostokata(a, a)

##################################################
menu()