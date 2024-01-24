tekst = "matematyka"
szukany_znak = "a"
nowy_znak = "X"

def zlicz_znaki(tekst, szukany_znak):
    licznik = 0
    for znak in tekst:
        if znak == szukany_znak:
            licznik += 1
    return licznik

print( zlicz_znaki(tekst, szukany_znak) )

def zamien_znaki(tekst, szukany_znak, nowy_znak):
    nowy_tekst = ""
    for znak in tekst:
        if znak == szukany_znak:
            znak = nowy_znak
        nowy_tekst += znak
    return nowy_tekst

print( zamien_znaki(tekst, szukany_znak, nowy_znak) )
        
    