tekst = "Dzisiaj mamy skrócone lekcje"
szukany_znak = ' '

def zlicz_znaki(tekst, znak):
    licznik = 0
    for litera in tekst:
        if litera == znak:
            licznik += 1
    return licznik

def zamien_znak(tekst, szukany_znak, nowy_znak):
    nowy_tekst = ''
    for litera in tekst:
        if litera == szukany_znak:
            litera = nowy_znak
        nowy_tekst += litera
    return nowy_tekst

print( zlicz_znaki(tekst, szukany_znak) )
print( zamien_znak(tekst, szukany_znak, "_") )


