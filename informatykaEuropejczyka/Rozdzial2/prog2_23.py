#sortowanie przez zliczanie

def sortuj (T, m):
    n=len(T)
    P=[]
    for i in range(m):
        P.append(0)
    for i in T:
        P[i]+=1
    k=0
    for i in range(m):
        for j in range(P[i],0,-1):
            T[k]=i
            k+=1
    return T    

#print(sortuj([4,3,3,4,0,2,1,4],5))

