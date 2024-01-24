tekst1 = "kajak"
tekst2 = "kajak"

def takie_same(t1, t2):
    i = 0
    dl1 = len(t1)
    dl2 = len(t2)
    
    while i < dl1 and i < dl2 and t1[i] == t2[i]:
        i += 1
    return i == dl1 and i == dl2

print( takie_same(tekst1, tekst2) ) 