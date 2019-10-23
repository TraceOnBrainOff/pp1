imienia = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]
najdluzszy = 0
index = 0
currIndex = 0


for imie in imienia:
    if len(imie)>najdluzszy:
        najdluzszy = len(imie)
        index = currIndex
    currIndex = currIndex + 1
    
print(imienia[index])