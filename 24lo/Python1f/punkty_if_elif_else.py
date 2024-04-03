# Zapytaj użytkownika o ilość punktów z testu.
# Zapisz to do zmiennej punkty
# 
# Jeżeli punkty < 20 to wypisz "Niestety nie zdałeś"
# Jeżeli punkty < 40 to wypisz "Ocena 2"
# Jeżeli punkty < 60 to wypisz "Ocena 3"
# Jeżeli punkty < 80 to wypisz "Ocena 4"
# Jeżeli punkty < 90 to wypisz "Ocena 5"
# Jeżeli punkty <= 100 to wypisz "Ocena 6"
# W przeciwnym razie "Coś chyba pomyliłeś"
# punkty = int( input("Podaj liczbę punktów z testu: " ) )

if punkty < 20:
    print("Niestety nie zdałeś")
elif punkty < 40:
    print("Ocena 2")
elif punkty < 60:
    print("Ocena 3")
elif punkty < 80:
    print("Ocena 4")
elif punkty < 90:
    print("Ocena 5")
elif punkty <= 100:
    print("Ocena 6")
else:
    print("Coś chyba pomyliłeś")

