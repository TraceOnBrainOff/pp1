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
        if self.state == True:
            currCh = ""
            if self.channel > len(self.channels):
                currCh = "Nieznany"
            else:
                currCh = self.channels[self.channel-1]
            print(str.format("Stan: {}, Kanał: {} ({})", self.state, self.channel, currCh))
        else:
            print(self.state)
    def new_channel(self,newCh):
        self.channel = newCh
    def new_channel_set(self,channelList):
        self.channels= channelList
    def show_channels(self):
        print(self.channels)        

a = TV()
a.on()
a.new_channel_set(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "TV4", "Eska"])
for i in range(1,9):
    a.new_channel(i)
    a.show_status()