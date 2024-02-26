#algorytm rekurencyjny rozwiazujacy zagadke wiez Hanoi

def oblicz (n, a, b, c):
    if n>0:
        oblicz(n-1,a,c,b)
        print(a," na ",b)
        oblicz(n-1,c,b,a)

#oblicz(6,'A','B','C')
        
