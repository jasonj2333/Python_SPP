#sortowanie przez scalanie - rekurencja

def scalaj (T, lewy, prawy):
    n=len(T)
    pom=[]
    for i in range(n):
        pom.append(T[i])
    srodek=(lewy+prawy)//2
    i=lewy
    i_lewy=lewy
    i_prawy=srodek+1
    while i_lewy<=srodek and i_prawy<=prawy:
        if pom[i_lewy]<pom[i_prawy]:
            T[i]=pom[i_lewy]
            i_lewy+=1
        else:
            T[i]=pom[i_prawy]
            i_prawy+=1
        i+=1
    if i_lewy>srodek:
        while i_prawy<=prawy:
            T[i]=pom[i_prawy]
            i_prawy+=1
            i+=1
    else:
        while i_lewy<=srodek:
            T[i]=pom[i_lewy]
            i_lewy+=1
            i+=1

def sortuj (T, lewy, prawy):
    srodek=(lewy+prawy)//2;
    if lewy<srodek:
        sortuj(T,lewy,srodek)
    if srodek+1<prawy:
        sortuj(T,srodek+1,prawy)
    scalaj(T,lewy,prawy)

def sortujprzezscalanie (T):
    n=len(T)
    sortuj(T,0,n-1)
    return T

#print(sortujprzezscalanie([9,8,7,0,3,4,5,2,1]))



