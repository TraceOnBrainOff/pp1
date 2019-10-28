lista = []
with open('C:/Users/JUNK/Desktop/School/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        lista.append(int(line))

suma = 0
for i in lista:
    suma += i

print(suma)