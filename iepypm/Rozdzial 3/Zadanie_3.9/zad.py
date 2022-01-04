def palindrom(s):
    return s == s[::-1]

def przepisz():
    dane = open("dane.txt", "r")
    wyniki = open("zadanie4.txt", "w")
    for k in dane:
        if palindrom(str(k.rstrip())): 
            # print(k)
            wyniki.write(k)
    dane.close()
    wyniki.close()

przepisz()

 
