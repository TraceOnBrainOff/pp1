dni = ["Pn", "Wt", "Sr", "Cz", "Pt", "Sb", "Nd"]
nrDniaTygodnia = 2
limitM = 30
currDzien = -nrDniaTygodnia+1
currLine = 0
while currDzien < 31:
    toPrint = ""
    for i in range(15): #rysowanie
        if currLine == 0: #narysuj header
            if i%2==0:
                toPrint += " | "
            else:
                toPrint += dni[int(i/2)]
        else: #rysuj dni
            if i%2==0:
                toPrint += " | "
            else:
                if currDzien > 0 and currDzien < 31:
                    if currDzien < 10:
                        toPrint += " " # dodaj spacje zeby nie rozjechalo sie
                    toPrint += str(currDzien)
                else:
                    toPrint += "  "
                currDzien += 1
    currLine += 1
    print(toPrint)
                
            