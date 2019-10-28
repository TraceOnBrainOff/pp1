plik = open('students.txt')
lineC = 0
lista = []

for line in plik:
    if lineC!=0:
        lista.append(line.split(","))
    lineC +=1

plik.close()

for a in lista:
    print(a[0], a[1], a[4])
