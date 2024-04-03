wycieczka = ["Tomek", "Ala", "Grzesiek"]

wycieczka.clear()

def dodaj():
    imie = ""
    print("Wpisz 0 jeżeli chcesz zakończyć")
    while imie != '0':
        imie = input("Podaj imię: ")
        wycieczka.append(imie)
    wycieczka.pop() #usuń ostatni element

def wypisz():
    wycieczka.sort()
    for imie in wycieczka:
        print(imie)
        
dodaj()
wypisz()