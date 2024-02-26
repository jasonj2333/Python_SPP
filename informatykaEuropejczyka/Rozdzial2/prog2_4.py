#algorytm Euklidesa wykorzystujacy operacje reszty z dzielenia - rekurencja

def nwd (a, b):
    if b==0:
        return a
    return nwd(b,a%b)

#print(nwd(32,44))

