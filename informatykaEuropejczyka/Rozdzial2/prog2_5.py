#algorytm Euklidesa wykorzystujacy operacje odejmowania - iteracja

def nwd (a, b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a    
    return a    

#print(nwd(32,44))

