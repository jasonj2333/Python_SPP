def znak_na_kod(znak):
    return ord(znak.upper()) - ord('A')

def kod_na_znak(kod):
    return chr(kod + ord('A'))

def zaszyfruj(napis, klucz):
    wynik = ""
    for znak in napis:
        kod = znak_na_kod(znak)
        kod_znaku_zaszyfrowany = (kod + klucz) % 26
        wynik += kod_na_znak(kod_znaku_zaszyfrowany)
    return wynik

def deszyfruj(szyfrogram, klucz):
    return zaszyfruj(szyfrogram, 26-klucz)

szyfrogram = zaszyfruj("matematyka", 3)
jawny = deszyfruj(szyfrogram, 3)
print(szyfrogram)
print(jawny)