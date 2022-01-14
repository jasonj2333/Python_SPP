#zmienna o nazwie tekst do której przypisyjemy znakiem = ciąg znaków w " " lub ' '
tekst = "Ola ma kota Tolka, a kot Tolek ma Panią Olę"
szukany = "kot"

print(tekst) #wyświetl tekst przechowywany w zmiennej tekst
print(tekst[0]) #wyświetla literę o indeksie 0 (pierwsza litera) z ciągu przechowywanego w zmiennej tekst
print(tekst[3:7]) #wyświetla litery o indeksach od 3 do 7 (bez 7)
print(tekst[:9]) #od początku 0 do 9 (bez 9)
print(tekst[4:-2]) #od początku 4 do 2 od końca (bez niego)
print(tekst[4:-2:3]) #od początku 4 do 2 od końca (bez niego) co trzeci znak
print(tekst[-5]) #5 znak od końca (spacja to też znak)
print(tekst[::-1]) #wyświetl tekst od końca

print(tekst.lower()) #zamień wszystkie litery na małe
print(tekst.upper()) #zamień wszystkie litery na duże
print(tekst.title()) #zamień pierwsze litery wszystkich wyrazów na duże
print(tekst.capitalize()) #zamień pierwszą literę tekstu na dużą
print(szukany in tekst) #sprawdź czy ciąg zapisany w zmiennej szukany znajduje się w tekście przychowywanym w zmiennej tekst
print(tekst.find(szukany)) # znajdź szukany w tekst i podaj indeks elementu od którego ciąg szukany występuje w tekst (1 wystąpienie)