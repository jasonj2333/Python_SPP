#sortowanie babelkowe

def sortuj (T):
    n=len(T)
    for j in range(n-1,0,-1):
        for i in range(j):
            if T[i]>T[i+1]:
                T[i],T[i+1]=T[i+1],T[i]
    return T    

#print(sortuj([9,8,7,0,5,4,3,2]))

