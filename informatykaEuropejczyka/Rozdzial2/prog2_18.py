#wyznaczanie maksimum w n elementowym ciagu liczb

def oblicz (T):
    n=len(T)
    maksimum=T[0]
    for i in range(1,n):
        if T[i]>maksimum:
            maksimum=T[i]
    return maksimum    

#print(oblicz([5,3,4,2,8,7,6,1,0,9]))

