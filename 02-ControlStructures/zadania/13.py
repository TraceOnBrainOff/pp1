def A(x,y):
    if x==0 and y==0:
        print("Srodek ukladu")
        return
    if x==0:
        print("Znajduje sie na osi X")
        return
    if y==0:
        print("Znajduje sie na osi Y")
        return
    if x>0 and y>0:
        print("Pierwsza")
    if x<0 and y>0:
        print("Druga")
    if x<0 and y<0:
        print("Trzecia")
    if x>0 and y<0:
        print("Czwarta")

x = int(input("X: "))
y = int(input("Y: "))

A(x,y)