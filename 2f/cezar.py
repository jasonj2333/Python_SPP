tekst = "matematyka"

def szyfruj(tekst, klucz=3):
    szyfrogram = ""
    for znak in tekst:
        kod = (ord(znak.upper()) - ord('A') + klucz) % 26
        szyfrogram += chr(kod + ord('A'))
    return szyfrogram

def deszyfruj(szyfrogram, klucz):
    return szyfruj(szyfrogram, 26-klucz)

szyfrogram = szyfruj(tekst, 6)
print(szyfrogram)
jawny = deszyfruj(szyfrogram, 6)
print(jawny)

szyfrogram = szyfruj("bardzo lubie szyfrowac", 13)
print(szyfrogram)
jawny = deszyfruj(szyfrogram, 13)
print(jawny)