class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.name = 'UEK' # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name

a = University()
a.set_name("Aaa")
a.print_name()