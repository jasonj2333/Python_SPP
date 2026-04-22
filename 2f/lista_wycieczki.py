lista_wycieczka = []

n = int(input("Podaj liczbę uczestników wycieczki: "))

def wypelnij_liste(n):
    for i in range(n):
        imie = input("Podaj imię uczestnika wycieczki: ")
        lista_wycieczka.append(imie)

def wypisz_liste(lista):
    nr = 1
    for imie in sorted(lista):
        print(f"{nr}. {imie}")
        nr += 1
    print(f"Liczba uczestników wycieczki: {len(lista)}" )
        
wypelnij_liste(n)
#lista_wycieczka.pop() ##usuwanie ostatniego elementu z listy
wypisz_liste(lista_wycieczka)
imie = input("Podaj imię osoby do skreślenia z listy: ")
lista_wycieczka.remove(imie)
wypisz_liste(lista_wycieczka)