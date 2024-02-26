#szyfrowanie metoda kolumnowa

def szyfruj (tekst, klucz):
    n,dl=len(klucz),len(tekst)
    if dl%n:
        m=dl//n+1
    else:
        m=dl//n
    tablica=[[0 for col in range(n)] for row in range(m)]    
    k=0
    for i in range(m):
        for j in range(n):
            if k<dl:
                tablica[i][j]=tekst[k]
                k+=1
            else:
                tablica[i][j]='\0'
    wynik=''
    for k in range(n):
        l=klucz[k]
        for i in range(m):
            if tablica[i][l]!='\0':
                wynik+=tablica[i][l]
    return wynik

#print(szyfruj('kryptoanaliza',[2,1,4,0,3]))

