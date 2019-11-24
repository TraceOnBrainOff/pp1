import math
def czytajWspolczynniki():
    wspolczynniki = []
    while len(wspolczynniki) < 3:
        wspolczynniki.append(int(input("Podaj współczynnik "+ str(len(wspolczynniki))+": ")))
    return wspolczynniki

def obliczDelte(wspolczynniki):
    return wspolczynniki[1]**2 - 4*wspolczynniki[0]*wspolczynniki[2]

def obliczPierwiastki(wspolczynniki, delta):
    if delta < 0:
        print("Delta mniejsza od 0")
        return []
    elif delta == 0:
        return [(-wspolczynniki[0])/(2*wspolczynniki[1])]
    elif delta > 0:
        a = (-wspolczynniki[1]-math.sqrt(delta))/(wspolczynniki[0]*2)
        b = (-wspolczynniki[1]+math.sqrt(delta))/(wspolczynniki[0]*2)
        return [a,b]
    
def wyswietlPierwiastki(pierwiastki):
    print("Pierwiastki kwadratowe: ")
    for i in pierwiastki:
        print(i)