file = open('numbers.txt', 'r')
lista = []

for line in file:
    lista.append(int(line))

lista.sort()
for i in lista:
    print(i)