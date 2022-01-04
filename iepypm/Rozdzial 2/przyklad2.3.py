# wyznaczanie maksimum w n-elementowym ciągu liczb

def oblicz1(T):
    n = len(T)
    maksimum = T[0]
    for i in range(1, n):
        if T[i] > maksimum:
            maksimum = T[i]
    return maksimum    

def oblicz2(T):
    maksimum = T[0]
    for k in T:
        if k > maksimum:
            maksimum = k
    return maksimum

print(oblicz1([5, 3, 4, 2, 8, 7, 6, 1, 0, 9]))
print(oblicz2([5, 3, 4, 2, 8, 7, 6, 1, 0, 9]))
