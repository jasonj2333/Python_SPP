suma = 0
ilosc = 5

for i in range(ilosc):
    liczba = int(input("Podaj liczbę: "))
    suma += liczba

srednia = suma / ilosc

print(f"Średnia z podanych liczb wynosi: {srednia}")