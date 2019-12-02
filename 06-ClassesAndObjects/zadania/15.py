class TV():
    # konstruktor obiektu (metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.state = False # zachowania obiektu (metody)
        self.channel = 1
        self.channels = []
        self.volume = 0
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
            print(str.format("Stan: {}, Kanał: {} ({}), Głośność: {}", self.state, self.channel, currCh, self.volume))
        else:
            print(self.state)
    def new_channel(self,newCh):
        self.channel = newCh
    def new_channel_set(self,channelList):
        self.channels= channelList
    def show_channels(self):
        print(self.channels)
    def incVolume(self):
        if self.volume < 10:
            self.volume += 1
    def decVolume(self):
        if self.volume > 0:
            self.volume -= 1

a = TV()
a.on()
for i in range(11):
    a.incVolume()
    a.show_status()
for i in range(11):
    a.decVolume()
    a.show_status()