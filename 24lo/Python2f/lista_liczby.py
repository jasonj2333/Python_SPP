liczby = []
n = 5

def wprowadz(n):
    for i in range(n):
        liczba = int( input("Podaj liczbę: ") )
        liczby.append(liczba)

def szukaj_liniowo(szukana, n):
    for i in range(n):
        if liczby[i] == szukana:
            return i
    return -1

wprowadz(n)
indeks = szukaj_liniowo(0, n)
if indeks != -1:
    print(f"Szukany element znaleziono na pozycji {indeks}")
else:
    print("Szukanego elementu nie znaleziono na liście")