# szyfr Cezara

def szyfruj(tekst, alfabet, klucz):
    wynik = ''
    dlT, dlA = len(tekst), len(alfabet)
    for i in range(dlT):
        for j in range(dlA):
            if tekst[i] == alfabet[j]:
                wynik += alfabet[(j + klucz) % dlA]
    return wynik

print(szyfruj('KRYPTOANALIZA', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3))
