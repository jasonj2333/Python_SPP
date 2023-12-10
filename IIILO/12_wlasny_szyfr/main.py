#Wlasny szyfr nr_znaku * klucz - klucz
#Zaimplementuj własny szyfr symetryczny:
#Algorytm szyfrowania - znak_szyfrogramu = nr_znaku * klucz - klucz
#Do kodowania znaków liczbami wykorzystaj tablicę znaków ASCII/UNICODE
#Poszczególne liczby reprezentujące znaki w szyfrogramie rozdzielaj znakiem #
#Może ci się przydać:
# - ord(znak)
# - chr(liczba)
# - string.split(separator)

jawny = "Szyfrowanie własnym szyfrem"

def szyfruj(tekst, klucz):
    szyfrogram = ""
    for znak in tekst:
        liczba = ord(znak) * klucz - klucz
        szyfrogram += str(liczba) + "#"
    return szyfrogram

def deszyfruj(szyfrogram, klucz):
    jawny = ""
    szyfrogram = szyfrogram.split("#")
    for znak in szyfrogram:
        if znak != "":
            liczba = int((int(znak) + klucz) / klucz)
            jawny += chr(liczba)
    return jawny
    

szyfrogram = szyfruj(jawny, 5)
print(szyfrogram)
jawny = deszyfruj(szyfrogram, 5)
print(jawny)