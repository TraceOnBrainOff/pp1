file = open('shoppinglist.txt', 'a')
a = input("Podaj nowy item: ")
file.write(a+"\n") #trzeba dodać newline'a
file.close()