
def anagram(tekst):
    szyfrogram = ""
    for znak in tekst:
        szyfrogram = znak + szyfrogram
    return szyfrogram

#Szyfrowanie
szyfrogram = anagram("bardzo lubię grać na lekcji")
print(szyfrogram)
#Deszyfrowanie
print( anagram(szyfrogram) )
        
    