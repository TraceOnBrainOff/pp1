plik = open('numbersinrows.txt')
lista = []

suma = 0
liczba = 0

for line in plik:
    a = line.split(",")
    liczba += len(a)
    for strNum in a:
        suma += int(strNum)

print(liczba, suma)
    

plik.close()