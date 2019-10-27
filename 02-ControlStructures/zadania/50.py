import math
liczba = 15
lista = []
while liczba != 0:
    lista.append(str(liczba%2))
    liczba = math.floor(liczba/2)
    
print("".join(reversed(lista)))