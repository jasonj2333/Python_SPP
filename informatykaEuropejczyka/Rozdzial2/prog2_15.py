#algorytm sprawdzajacy, czy wszystkie elementy ciagu sa wieksze od 5

def szukaj (T):
    n=len(T)
    for i in range(n):
        if T[i]<=5:
            return False
    return True

def szukaj2 (T):
    for k in T:
        if k<=5:
            return False
    return True

#print(szukaj([7,5,6,4,5,3,4,1,8,3]))
#print(szukaj2([7,5,6,4,5,3,4,1,8,3]))
