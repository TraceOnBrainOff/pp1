a = 4
b = 15

for i in range(a):
    if i==0 or i==a-1:
        toPrint = ""
        for j in range(b):
            toPrint = toPrint + "*"
        print(toPrint)
    else:
        toPrint = "*"
        for j in range(b-2):
            toPrint = toPrint + " "
        toPrint = toPrint + "*"
        print(toPrint)
        