liczba = -6
licznik = 0

while liczba != 0:
    liczba = int( input("Podaj liczbę: ") )
    if liczba % 3 == 0 and liczba !=0:
        licznik += 1

print(f"Podałeś {licznik} liczb podzielnych przez 3")
        
        