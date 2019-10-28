plik = open('numbers.txt')
plik2 = open('evennumbers.txt', 'w')
for line in plik:
    a = int(line)
    if a%2==0:
        plik2.write(line)
plik.close()
plik2.close()