r = 50
lista = []
for i in range(2,r):
    toJoin = True
    for j in range(2,i): 
        if i%j==0:
            toJoin = False
    if toJoin == True:
        lista.append(str(i))
print(', '.join(lista))