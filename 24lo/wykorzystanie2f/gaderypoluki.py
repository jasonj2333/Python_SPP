szyfr = "GADERYPOLUKI"
#szyfr = 'MALINOWEBUTY'

tekst = "Dzisiaj mamy skrócone lekcje"

def szyfruj(tekst, szyfr):
    szyfrogram = ""
    for znak in tekst:
        poz = szyfr.find(znak.upper())
        if poz == -1:
            szyfrogram += znak.upper()
        elif poz % 2 == 0:
            szyfrogram += szyfr[poz + 1]
        else:
            szyfrogram += szyfr[poz - 1]
    return szyfrogram

szyfrogram = szyfruj(tekst, szyfr)
print(szyfrogram)
jawny = szyfruj(szyfrogram, szyfr)
print(jawny)
