#algorytm sprawdzajacy, czy dwa slowa zlozone wylacznie z liter "X" i "Y" sa anagramami

def sprawdz (s1, s2):
    dl=len(s1)
    if dl!=len(s2):
        return False
    else:
        T1=[0, 0]
        T2=[0, 0]
        for i in range(dl):
            if s1[i]=='X':
                T1[0]+=1
            else:
                T1[1]+=1
            if s2[i]=='X':
                T2[0]+=1
            else:
                T2[1]+=1
        if T1[0]!=T2[0]:
            return False
    return True    

#print(sprawdz('XYYXY','YYXXX'))

