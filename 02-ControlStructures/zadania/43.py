a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = int(input("Podaj trzecia liczbe: "))

lista = [a,b,c]
lista.sort()

print("Liczby w kolejności rosnącej: ", lista[0], lista[1], lista[2])