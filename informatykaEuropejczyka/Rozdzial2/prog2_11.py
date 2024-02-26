#badanie, czy liczba jest pierwsza

def sprawdz (n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#print(sprawdz(61))


