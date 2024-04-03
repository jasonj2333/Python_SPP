liczba = int( input("Podaj liczbę: ") )

#Instrukcje zagnieżdżone
if liczba > 0:
    print("Liczba jest dodatnia")
else:
    if liczba == 0:
        print("Twoja liczba to zero")
    else:
        print("Liczba jest ujemna")
        
#Warunki wielokrotne
if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba == 0:
    print("Twoja liczba to zero")
else:
    print("Liczba jest ujemna")
    