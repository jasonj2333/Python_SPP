# sprawdzanie, czy ciąg jest rosnący

def rosnacy(T):
    n = len(T)
    for i in range(n - 1):
        if T[i] >= T[i + 1]:
            return False
    return True    

print(rosnacy([3, 4, 5, 5, 7, 9]))

