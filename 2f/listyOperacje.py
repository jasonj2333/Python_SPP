liczby = [5, 12, 3, 5, 122, 78, 23321, 2, 21, 4, 8, 34, "Ania"]
liczby.append(0)
liczby.pop(1) #usuwana po indeksie
liczby.remove(5) #usuwa po wartosci
liczby.insert(0, 333) #dodaje wartosc w miejsce podanego indeksu
print(liczby)
n = len(liczby)
print(n)

def szukaj(szukana, lista):
    for i in range(len(lista)):
        if szukana == lista[i]:
            return i
    return -1

indeks = szukaj(21, liczby)
if  indeks == -1:
    print("Liczby nie znaleziono na liście")
else:
    print(f"Liczbę znaleziono pod indeksem {indeks}")
    
#liczby.clear() #usuwa elementy z listy
litery = ["a", "b", "c"]
liczby.extend(litery)
nowa_lista = liczby + litery
print(liczby)
print(nowa_lista)