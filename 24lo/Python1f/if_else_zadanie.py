# Poproś użytkownika o podanie liczby większej od 5 (i mniejszej od 100)
# Jeżeli podana liczba jest poprawna to wypisz:
#     Brawo! Otrzymujesz 3 * liczba zł
# W przeciwnym razie wypisz:
#     Chyba nie za bardzo umiesz liczyć
    
liczba = int( input("Podaj liczbę: ") )

if liczba > 5 and liczba < 100:
    nagroda = 3 * liczba
    print(f"Brawo! Otrzymujesz {nagroda} zł")
    #print("Brawo...", 3 * liczba, "zł")
else:
    print("Chyba nie za bardzo umiesz liczyć")