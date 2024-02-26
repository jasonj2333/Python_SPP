#znajdowanie lidera w zbiorze

def szukaj (T):
    n=len(T)
    lider=T[0]
    pom=1
    ilosc=0
    for i in range(1,n):
        if pom==0:
            lider=T[i]
            pom=1
        elif T[i]==lider:
            pom+=1
        else:
            pom-=1
    if pom==0:
        print("w zbiorze nie ma lidera")
    else:
        for i in range(n):
            if T[i]==lider:
                ilosc+=1
        if ilosc>n//2:
            print("liczba ",lider," jest liderem")
        else:
            print("w zbiorze nie ma lidera")
            
#szukaj([3,1,3,4,3,3,0,3])
