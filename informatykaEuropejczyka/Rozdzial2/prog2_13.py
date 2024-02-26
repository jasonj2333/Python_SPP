#liniowe przeszukiwanie ciagu liczbowego

def szukaj (T, szukana):
    i=0
    n=len(T)
    while i<n and T[i]!=szukana:
        i+=1
    if i==n:
        return False
    return True

def szukaj2 (T, szukana):
    if szukana in T:
        print("TAK")
    else:
        print("NIE")

#print(szukaj([7,5,6,4,5,3,4,8,2,3],2))
#szukaj2([7,5,6,4,5,3,4,8,2,3],2)

