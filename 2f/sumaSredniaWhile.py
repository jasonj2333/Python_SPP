suma = 0
liczba = -1
licznik = 0

while liczba != 0:
    liczba = int(input("Podaj liczbę różną od 0. Wpisanie 0 kończy program."))
    if liczba != 0:
        licznik += 1
    suma += liczba


print(f"Suma wynosi: {suma}")
if licznik > 0:
    srednia = suma / licznik
    print(f"Średnia wynosi: {srednia}")