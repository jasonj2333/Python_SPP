#liniowe przeszukiwanie ciagu liczbowego z wartownikiem

def szukaj (T, szukana):
    n=len(T)
    i=0
    T.insert(n,szukana)
    while T[i]!=szukana:
        i+=1
    if i<n:    
        return True
    return False

#print(szukaj([7,5,6,4,5,3,4,8,2,3],2))

