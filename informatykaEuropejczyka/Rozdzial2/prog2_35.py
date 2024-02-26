#algorytm realizujacy naiwne wyszukiwanie wzorca w tekscie

def szukaj (s, wzorzec):
    dlT,dlW=len(s),len(wzorzec)
    T=[]
    if dlW>dlT:
        return False
    n=0
    for i in range(dlT-dlW+1):
        for j in range(i,i+dlW):
            if s[j]!=wzorzec[j-i]:
                break
        if j+1==i+dlW:
            T.append(i)
            n+=1
    if n==0:
        return False
    return n, T

#print(szukaj('karykatura','ka'))

