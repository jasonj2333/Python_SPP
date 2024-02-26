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
        
u1 = Ulamek(10, 30)
u2 = Ulamek(1, 2)
u1.wyswietl()
u1.skroc()
u1.wyswietl()
u2.wyswietl()


