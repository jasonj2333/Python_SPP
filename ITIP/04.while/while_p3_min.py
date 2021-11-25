# Dane:
#     Liczba naturalna: n > 0 (liczba wczytywanych wartości)
# Wynik:
#     Najmniejsza z liczb rzeczywistych wprowadzonych z klawiatury: minimum
#     
# Lista kroków:
#     1. Wczytaj liczbę k
#     2. Przypisz minimum = k
#     3. Jeśli n = 1, wypisz minimum i zakończ algorytm
#     4. Wczytaj liczbę k
#     5. Zmiejsz n o 1
#     6. Jeśli k < mniejsze od minimum przejdź do kroku 2, w przeciwnym razie wypadku
#        przejdź do kroku 3






n = 5       
k = float(input('Podaj liczbę: '))
minimum = k
while n > 1:
    k = float(input('Podaj liczbę: '))
    if k < minimum:
        minimum = k
    n -= 1
    
print(f"Minimum to: {minimum}")