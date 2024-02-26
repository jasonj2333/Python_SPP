#algorytm obliczajacy sume liczb wczytywanych z klawiatury nie wiekszych od 50

def suma ():
    s=0
    a=0
    while a <= 50:
        s+=a
        a=float(input("podaj liczbe rzeczywista: "))
    return s

#print(suma())

