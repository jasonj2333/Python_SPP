suma = 0

for i in range(7): #[0,1,2,3,4,5,6]
    liczba = int( input("Podaj liczbę: ") )
    suma = suma + liczba
    #suma += liczba
print(f"Suma podanych liczb wynosi: {suma}")