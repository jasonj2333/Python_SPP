#wyznaczanie minimum z n liczb wczytywanych na biezaco z klawiatury

def oblicz (n):
    k=float(input("podaj liczbę: "))
    minimum=k
    while n>1:
        k=float(input("podaj liczbę: "))
        if k<minimum:
            minimum=k
        n-=1
    return minimum    

#print(oblicz(5))

