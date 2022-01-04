from mylib import variable_type

#liczba całkowita - int
liczba_int = 5

#liczba zmiennoprzecinkowa - float
liczba_float = 2.78

#ciąg znaków - string (str)
tekst = "To jest tekst"

#zmienna logiczna - bool (True/False)
koniec = True

#krotka - tuple
krotka = (128, 67, 89) #niezmienna lista - struktura indeksowana np. krotka[2] - indeksujemy od 0

#lista - list - struktura indeksowana np. lista[2] - indeksujemy od 0
lista = [1, 7, "Tomek"] #może zawierać elementy różnych typów

#slownik - dict
slownik = {
        'Niepolomice' : 16,
        'Krakow' : 19
    }

#zbiór - set
zbior = {1, 12, "Tomek"}
#w zbiorze nie ma duplikatów (dwóch takich samych elementów), nie ma też kolejności elementów

#print(type(liczba))

variable_type(liczba_float)
