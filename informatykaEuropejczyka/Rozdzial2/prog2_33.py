#sortowanie tekstu przez wybor

def sortuj (s):
    dl=len(s)
    s=list(s)
    for i in range(dl-1):
        k=i
        for j in range(i+1,dl):
            if s[j]<s[k]:
                k=j
        s[k],s[i]=s[i],s[k]
    s=''.join(s)
    return s

#print(sortuj("zxcvbnmas"))

