#ogolny problem plecakowy - algorytm zachlanny

def pakujPlecak (W, C, waga):
    n=len(W)
    K=[]
    wynik=0
    for i in range(n):
        K.append(waga//C[i])
        waga-=K[i]*C[i]
        wynik+=W[i]*K[i]
    return wynik, K

#print(pakujPlecak([8,3,1,2,1],[4,2,1,3,7],11))

