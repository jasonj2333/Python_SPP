def dopelnij(napis, znak, liczba_znakow):
    wynik = napis
    for i in range(len(napis), liczba_znakow):
        wynik += znak
    return wynik

def liczba_znakow_z_dopelnieniem(napis, liczba_kolumn):
    dlugosc = len(napis)
    liczba_znakow_ostatni_wiersz = dlugosc % liczba_kolumn
    if liczba_znakow_ostatni_wiersz != 0:
        dlugosc += liczba_kolumn - liczba_znakow_ostatni_wiersz
    return dlugosc

def zaszyfruj(napis, liczba_kolumn):
    wynik = ""
    napis = dopelnij(napis, '_', liczba_znakow_z_dopelnieniem(napis, liczba_kolumn))
    dlugosc = len(napis)
    akt_pozycja = 0
    for i in range(dlugosc):
        wynik += napis[akt_pozycja]
        akt_pozycja += liczba_kolumn
        if akt_pozycja >= dlugosc:
            akt_pozycja = akt_pozycja - dlugosc + 1
    return wynik


szyfrogram = zaszyfruj('ALAMAKOTA', 4)
szyfrogram2 = 'NAWOEIWATJEERERMJAJZOŚZSEŻĆYAKNDDMI'
jawny = zaszyfruj(szyfrogram, len(szyfrogram)//4)
print(szyfrogram)
print(jawny.replace('_', ''))