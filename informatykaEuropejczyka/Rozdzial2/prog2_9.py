#wyznaczanie wartosci wielomianu schematem Hornera - iteracja

def oblicz (A, n, x):
    w=A[0]
    for i in range(1,n+1):
        w=w*x+A[i]
    return w    

#print(oblicz([2,4,-3,7],3,3))

