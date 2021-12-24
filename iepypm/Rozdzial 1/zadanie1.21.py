# sortowanie listy napisów metodą bąbelkową

def sortujslowa(s):
    lista = s.split()
    n = len(lista)   
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

print(sortujslowa("9876 123 76547 4343 898 2345"))

