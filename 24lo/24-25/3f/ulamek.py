class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    
    def wyswietl(self):
        print(f"{self.licznik}/{self.mianownik}")
        
    def nwd(self):
        a, b = self.licznik, self.mianownik
        while b != 0:
            a, b = b, a % b
        return a
    
    def skroc(self):
        nwd = self.nwd()
        self.licznik = self.licznik // nwd
        self.mianownik = self.mianownik // nwd
        
    def dodaj(self, u2):
        wynik = Ulamek(self.licznik * u2.mianownik + u2.licznik * self.mianownik, self.mianownik * u2.mianownik)
        return wynik

u1 = Ulamek(10, 20)
u1.skroc()
u1.wyswietl()

u2 = Ulamek(6,86)
u2.skroc()
u2.wyswietl()

u3 = u1.dodaj(u2)
u3.skroc()
u3.wyswietl()
