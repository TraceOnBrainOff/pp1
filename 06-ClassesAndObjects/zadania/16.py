class Book():
    # konstruktor obiektu (metoda __init__)
    def __init__(self): # cechy obiektu (pola)
        self.isOpen = False # zachowania obiektu (metody)
        self.author = "Jan Kowalski"
        self.pageCount = 60
        self.currentPage = 1
        self.title = "A b c"
    def showState(self):
        print(str.format("Open: {}, Title: {}, Page count: {}, Current page: {}", self.isOpen, self.title, self.pageCount, self.currentPage))
    def incPage(self):
        if self.currentPage < self.pageCount and self.isOpen:
            self.currentPage += 1
        elif self.isOpen == False:
            print("Book is closed")
    def decPage(self):
        if self.currentPage > 1 and self.isOpen:
            self.currentPage -= 1
        elif self.isOpen == False:
            print("Book is closed")
    def openB(self):
        self.isOpen = True
    def closeB(self):
        self.isOpen = False

a = Book()
a.openB()
a.showState()
for i in range(11):
    a.incPage()
a.showState()
a.closeB()
for i in range(11):
    a.decPage()
a.showState()