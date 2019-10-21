a = range(1,51,2) #nieparzyste
b = range(2,51,2) #parzyste, ten sam len!

sumaP = 0
sumaNP = 0
for e in a:
    sumaP+=e
    
for r in b:
    sumaNP+=r
    
print(sumaP, sumaNP)