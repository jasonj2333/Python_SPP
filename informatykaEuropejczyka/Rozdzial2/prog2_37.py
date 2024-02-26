#szyfrowanie metoda plotowa - wysokosc 3

def szyfruj (tekst):
    wynik=''
    dl=len(tekst)
    for i in range(0,dl,4):
        wynik+=tekst[i]
    for i in range(1,dl,2):
        wynik+=tekst[i]
    for i in range(2,dl,4):
        wynik+=tekst[i]
    return wynik

#print(szyfruj('kryptoanaliza'))

