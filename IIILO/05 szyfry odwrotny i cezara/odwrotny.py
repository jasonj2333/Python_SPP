tekst_jawny = "Informatyka jest fajna"
tekst_jawny = input("Podaj tekst do zaszyfrowania/odszyfrowania: ")

#wersja 1
def szyfr_odwrotny_v1(tekst):
    dlugosc_tekstu = len(tekst)
    i = dlugosc_tekstu-1
    szyfrogram = ""

    while i >= 0:
        szyfrogram += tekst[i]
        i-=1

    return szyfrogram

#wersja 2
def szyfr_odwrotny_v2(tekst):
    szyfrogram = ""

    for znak in reversed(tekst):
        szyfrogram += znak

    return szyfrogram

## Przykładowe użycie
print(szyfr_odwrotny_v1(tekst_jawny)) #wersja 1
print(szyfr_odwrotny_v2(tekst_jawny)) #wersja 2
print(tekst_jawny[::-1]) #wbudowany mechanizm Pythona

