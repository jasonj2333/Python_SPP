#konwersja systemu dwojkowego na dziesietny z zastosowaniem schematu Hornera - iteracja

def oblicz (A, n):
    w=A[0]
    for i in range(1,n+1):
        w=w*2+A[i]
    return w    

#print(oblicz([1,0,1,1,1,0,1],6))

