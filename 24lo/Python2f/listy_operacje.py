pracownicy = ["Anna Nowak"]
pracownicy.append("Krzysztof Nowak") #dodawanie elementu na końcu
pracownicy.insert(1, "Wojciech Tomaszewski") #wstawianie pod dany indeks

nowi_pracownicy = ["Tytus de Zoo", "Tomek Atomek"]
pracownicy.extend(nowi_pracownicy) #rozszerzanie listy o inną listę
print(pracownicy)

pracownicy.remove("Krzysztof Nowak") #usuwanie danej wartości
pracownicy.pop(1) #usuwanie po indeksach, jeżeli pusty to usuwamy ostatnie element
#pracownicy.clear() #wyczeszczenie listy
print(pracownicy)