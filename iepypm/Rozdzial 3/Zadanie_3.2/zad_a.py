def przestepny(rok):
    if rok % 4 == 0: pom = True
    else: pom = False
    if rok > 1582 and rok % 100 == 0 and rok % 400: pom = False
    return pom

def zad_a():
    dtygodnia = input("podaj dzień tygodnia: ")
    rok = int(input("podaj rok: "))
    if dtygodnia == "poniedziałek": dtyg = 0
    elif dtygodnia == "wtorek": dtyg = 1
    elif dtygodnia == "środa": dtyg = 2
    elif dtygodnia == "czwartek": dtyg = 3
    elif dtygodnia == "piątek": dtyg = 4
    elif dtygodnia == "sobota": dtyg = 5
    elif dtygodnia == "niedziela": dtyg = 6
# kalendarz juliański
    if rok < 1583:
        dni = 242
        for i in range(1581, rok - 1, -1):
            if przestepny(i): dni += 366
            else: dni += 365
        p = (dni % 7 + dtyg + 1) % 7
    else:
# kalendarz gregoriański
        dni=106
        for i in range(1583, rok):
            if przestepny(i): dni += 366
            else: dni += 365
        p = (7 - dni % 7 + dtyg + 1) % 7

    if przestepny(rok): ostatni = 29
    else: ostatni = 28
    while p <= ostatni:
        if p > 0: print(p, ".02.", rok)
        p += 7
 
zad_a()


