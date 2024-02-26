#algorytm rekurencyjny obliczajacy n! (n>=0)

def oblicz (n):
    if n==0:
        return 1
    return oblicz(n-1)*n

#print(oblicz(6))

