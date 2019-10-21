import random
a = random.randrange(6)
pl = int(input("Podaj numer: "))
if a == pl:
    print("True")
else:
    print("False")
print(str.format("Komputer wyrzucil {}", a))