#algorytm obliczajacy sume n kolejnych liczb naturalnych: 1, 2, ..., n

def suma (n):
    if n>=0:
        s=n*(n+1)/2
        print("s = ",s)
    else: print("n < 1")

#suma(5)
