#algorytm wyznaczajacy najmniejsza wspolna wielokrotnosc

def nwd (a, b):
    if a==b:
        return a
    if a>b:
        return nwd(a-b,b)
    return nwd(a,b-a)
        
def nww (a, b):
    return a*b//nwd(a,b)

#print(nww(12,8))

