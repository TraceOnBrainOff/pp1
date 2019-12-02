def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def prt(self):
        print(self.licznik/self.mianownik)
    def simplify(self):
        a = nwd(self.licznik, self.mianownik)
        self.licznik = self.licznik/a
        self.mianownik = self.mianownik/a