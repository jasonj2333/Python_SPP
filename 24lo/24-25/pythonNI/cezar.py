def szyfruj(tekst, klucz):
    wynik = ""
    for znak in tekst:
        kod = ord(znak.upper()) - ord('A')
        kod_szyfr = (kod + klucz) % 26
        wynik += chr(kod_szyfr + ord('A'))
    return wynik

def deszyfruj(szyfrogram, klucz):
    return szyfruj(szyfrogram, 26-klucz)

szyfrogram = szyfruj("Poniedzialek", 3)
print(szyfrogram)
jawny = deszyfruj(szyfrogram, 3)
print(jawny)
        