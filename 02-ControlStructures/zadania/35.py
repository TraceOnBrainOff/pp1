import math
a = int(input("Podaj A: "))
b = int(input("Podaj B: "))
c = int(input("Podaj C: "))

delta = b*b - 4 * a * c
if delta>=0:
    rDelta = math.sqrt(delta)
    x1 = (-b+rDelta)/(2*a)
    x2 = (-b-rDelta)/(2*a)
    print(x1, x2) #jak jest ==0 to obydwie sa takie same to ok
else:
    print("delta mniejsza od 0")