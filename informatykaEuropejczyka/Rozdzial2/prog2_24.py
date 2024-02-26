#jednoczesne znajdowanie minimalnego i maksymalnego elementu - iteracja

def oblicz (T):
    n=len(T)
    if n%2:
        dl=n-2
    else:
        dl=n-1
    if T[0]<=T[1]:
        minimum=T[0] 
        maksimum=T[1] 
    else:
        minimum=T[1]
        maksimum=T[0]
    i=2
    while i<dl:
        if T[i]<=T[i+1]:
            if T[i]<minimum:
                minimum=T[i]
            if T[i+1]>maksimum:
                maksimum=T[i+1]
        else:
            if T[i+1]<minimum:
                minimum=T[i+1]
            if T[i]>maksimum:
                maksimum=T[i]
        i+=2
    if n%2:
        if T[n-1]<minimum:
            minimum=T[n-1]
        if T[n-1]>maksimum:
            maksimum=T[n-1]
    return minimum, maksimum 

#print(oblicz([2,3,4,7,5,4,9,0,1,2]))


