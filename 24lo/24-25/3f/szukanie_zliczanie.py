tekst = "Coraz bliżej święta."
szukany_znak = " "

def zlicz_znaki(tekst, szukany_znak):
    licznik = 0
    for litera in tekst:
        if litera == szukany_znak:
            licznik += 1
    return licznik

print( zlicz_znaki(tekst, szukany_znak) )
print( zlicz_znaki("Matematyka", "a") )

print(tekst[6])
#tekst[6] = "B"

def zamien_znak(tekst, szukany_znak, nowy_znak):
    nowy_tekst = ""
    for litera in tekst:
        if litera == szukany_znak:
            litera = nowy_znak
        nowy_tekst += litera
    return nowy_tekst

print( zamien_znak(tekst, szukany_znak, "-") )
print( zamien_znak("Matematyka", "a", "A") )
        
        
        
        
    
    