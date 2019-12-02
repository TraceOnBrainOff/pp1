class TV():
    # konstruktor obiektu (metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.state = False # zachowania obiektu (metody)
        self.channel = 1
    def on(self):
        self.state = True
    def off(self):
        self.state = False
    def show_status(self):
        print(self.state)
        if self.state == True:
            print(self.channel)

a = TV()
a.show_status()
a.on()
a.show_status()
a.off()
a.show_status()