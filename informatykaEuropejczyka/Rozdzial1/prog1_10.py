#algorytm rekurencyjny - przeszukiwanie binarne ciagu uporzadkowanego

def szukaj (T, lewy, prawy, szukana):
    if lewy<=prawy:
        srodek=(lewy+prawy)//2
        if T[srodek]==szukana:
            return srodek
        if T[srodek]<szukana:
            return szukaj(T,srodek+1,prawy,szukana)
        return szukaj(T,lewy,srodek-1,szukana)
    return -1
   
#print(szukaj([-8,-7,-6,-2,0,2,3,4,5,7,8,10,12,13,17,19],0,15,13))

