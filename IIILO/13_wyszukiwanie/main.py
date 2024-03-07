# bubbleSort(array)
#   for i <- 1 to indexOfLastUnsortedElement-1
#     if leftElement > rightElement
#       swap leftElement and rightElement
# end bubbleSort

names = []

with open('names.txt') as f:
    for line in f:
        names.append(line.strip())

# Dana jest lista nieuporządkowana 100 osób (nazwisko imię) wczytana z pliku names.txt
# Twoim zadaniem jest wyszukanie sprawdzenie czy ponizsze nazwiska znajdują się na wczytanej liście.
# Nazwiska do wyszukania:
#     - Tomasz Kowalski
#     - Turner Connor
#     - Donald Trump
#     - MacLeod Heather
#     - Welch Kimberly
#     - Anna Jantar
#     - Wilson Erica
# Jezeli tak to wypisz komunikat np. Wilson Erica została znaleziona na pozycji X.
# Jezeli nie to wypisz komunikat np. Wilson Erica nie została znaleziona na liście.

# Utwórz program wykorzystujący optymalny algorytm do tego zadania, jeśli uznasz to za 
# konieczne mozesz uporządkować listę przed wyszukiwaniem.
# Załoz, ze w przyszłości będzie wykorzystywał/a napisany program do kolejnych wyszukiwań.

n = len(names)

def znajdz(wartosc: int) -> int:
    for index in range(n):
        if names[index] == wartosc:
            return index
    return -1

def znajdz_w(wartosc: int) -> int:
    names.append(wartosc)
    i = 0
    while names[i] != wartosc:
        i += 1
    if i < n: return i
    
    return -1

def znajdz_b(wartosc: int) -> int:
    poczatek = 0
    koniec = n - 1
    
    while poczatek <= koniec:
        srodek = (poczatek + koniec) // 2
        if names[srodek] == wartosc:
            return srodek
        else:
            if names[srodek] > wartosc:
                koniec = srodek - 1
            else:
                poczatek = srodek + 1
    return -1

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
        
bubbleSort(names)
print(names)
print(znajdz_b("Wilson Eric"))