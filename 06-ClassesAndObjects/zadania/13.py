class TV():
    # konstruktor obiektu (metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.state = False # zachowania obiektu (metody)
        self.channel = 1
        self.channels = []
    def on(self):
        self.state = True
    def off(self):
        self.state = False
    def show_status(self):
        print(self.state)
        if self.state == True:
            print(self.channel)
    def new_channel(self,newCh):
        self.channel = newCh
    def new_channel_set(self,channelList):
        self.channels= channelList
    def show_channels(self):
        print(self.channels)        

a = TV()
a.show_status()
a.on()
a.show_status()
a.show_channels()
a.new_channel_set(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox"])
a.show_channels()
a.off()