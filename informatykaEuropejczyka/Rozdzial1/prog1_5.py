#algorytm obliczajacy iloczyn n kolejnych liczb naturalnych: 3, 4, 5, 6... (n>0)

def iloczyn (n):
    s=1
    i=3
    while i<=n+2:
        s*=i
        i+=1
    return s    
    
#print(iloczyn(4))

