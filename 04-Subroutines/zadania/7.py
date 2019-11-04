def showPhone():
    a = 0
    for i in range(3):
        toPrint = ""
        for j in range(3):
            a += 1
            toPrint += str(a) + " "
        print(toPrint)

showPhone()