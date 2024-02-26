#algorytm Euklidesa wykorzystujacy operacje reszty z dzielenia - iteracja

def nwd (a, b):
    while b>0:
        r=a%b
        a=b
        b=r
    return a    

#print(nwd(32,44))

