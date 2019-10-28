a = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]

plik = open('newCSV.csv', 'w')
plik.write("Imie,Nazwisko,Email\n")

for arr in a:
    b = ""
    for i in range(len(arr)):
        if i!=2:
            b+=arr[i]+","
        else:
            b+=arr[i]+"\n"
    plik.write(b)
plik.close()