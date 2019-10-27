done = False
lista = []
while not done:
    a = int(input("Podaj liczbe: "))
    if a!=0:
        lista.append(a)
    else:
        suma = 0
        for liczba in lista:
            suma += liczba
        srednia = suma/len(lista)
        print("REZULTAT: Liczb = {}, Suma = {}, Srednia = {}".format(len(lista), suma, srednia))
        
    