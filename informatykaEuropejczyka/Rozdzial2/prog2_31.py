#ogolny problem plecakowy - programowanie dynamiczne

def pakujPlecak(W,C,waga):
    n=len(W)
    Wartosci=[[0 for col in range(waga+1)] for row in range(n+1)]
    Numery=[[0 for col in range(waga+1)] for row in range(n+1)]
    for i in range(1,waga+1):
        Wartosci[0][i],Numery[0][i]=0,0
    for i in range(1,n+1):
        Wartosci[i][0],Numery[i][0]=0,0
    for i in range(1,n+1):
        for j in range(1,waga+1):
            if j >= C[i-1] and Wartosci[i-1][j] < Wartosci[i][j-C[i-1]]+W[i-1]:
                Wartosci[i][j],Numery[i][j]=Wartosci[i][j-C[i-1]]+W[i-1],i
            else:
                Wartosci[i][j],Numery[i][j]=Wartosci[i-1][j],Numery[i-1][j]
#odczytanie wynikow
    wynik=Wartosci[n][waga];
    K=[]
    for i in range(n+1):
        K.append(0)
    while Numery[n][waga]>0:
        K[Numery[n][waga]]+=1
        waga-=C[Numery[n][waga]-1]
    print("wartosc plecaka:",wynik)
    print("zapakowane przedmioty:")
    for i in range(1,n+1):
        print(i,":  ilosc=",K[i],"  wartosc=",W[i-1],"  waga=",C[i-1],"\n")                
    return Wartosci[1:], Numery[1:]

#print(pakujPlecak([8,3,1,2,1],[4,2,1,3,7],11))





