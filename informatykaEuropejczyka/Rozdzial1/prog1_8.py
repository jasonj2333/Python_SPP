#algorytm rekurencyjny wyznaczajacy n-ty element ciagu Fibonacciego

def oblicz (n):
    if n==1 or n==2:
        return 1
    return oblicz(n-1)+oblicz(n-2)

#print(oblicz(7))

