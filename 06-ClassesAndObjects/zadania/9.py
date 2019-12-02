class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.name = 'UEK' # zachowania obiektu (metody)
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self, name):
        self.fullname = name

a = University()
a.print_fullname()
a.set_fullname("U a e")
a.print_fullname()