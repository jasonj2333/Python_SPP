import turtle as t

def fragment(bok):
    t.fd(bok/3); t.rt(60)
    t.fd(bok/3); t.lt(120)
    t.fd(bok/3); t.rt(60)
    t.fd(bok/3)
    
def gwiazda(bok):
    for i in range(4):
        fragment(bok)
        t.lt(90)
        
gwiazda(200)
    
    