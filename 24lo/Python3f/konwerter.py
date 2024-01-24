def bin_to_dec():
    print("Konwerter liczb")
    liczba = input("Podaj liczbę binarną: ")

    waga = 1
    suma = 0

    for cyfra in range(len(liczba)-1, -1, -1):
        suma = suma + int(liczba[cyfra]) * waga
        waga = waga * 2

    print(suma)

#bin_to_dec()
    
def dec_to_bin():
    wynik = ''
    liczba = int( input("Podaj liczbę dziesiętną: ") )
    while liczba > 0:
        reszta = liczba % 2
        wynik = str(reszta) + wynik
        liczba = liczba // 2
    print(wynik)
    
dec_to_bin()
        
