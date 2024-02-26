#konwersja systemu dziesietnego na dwojkowy

def oblicz (liczba):
    W=[]
    while liczba>0:
        W=[liczba%2]+W
        liczba//=2
    return W    

#print(oblicz(14))

