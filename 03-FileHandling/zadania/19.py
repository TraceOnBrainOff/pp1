plik = open('universities.txt', 'r')
lista = []
for line in plik:
    lista.append(line)

lista.sort()
plik.close()

plik2 = open('universities2.txt', 'w')
for uni in lista:
    plik2.write(uni)

plik2.close()

