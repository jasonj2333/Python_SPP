#algorytm Euklidesa wykorzystujacy operacje odejmowania - rekurencja

def nwd (a, b):
    if a==b:
        return a
    if a>b:
        return nwd(a-b,b)
    return nwd(a,b-a)

#print(nwd(32,44))

