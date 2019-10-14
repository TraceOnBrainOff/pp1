#Zamiana wartości przy pomocy pomocniczej zmiennej
x = 7
y = 34
z = x
x = y
y = z

#Basic arithmetic b, f, h
print("\nBasic Arithmetic:::")
a = [5, 1, 8, 6, 3]
b = 0
for n in a:
    b = b + n*n
    
print(b)

print(a[0]%3)

print(a[2]>>4)

#Arrays
print("\nArrays:::")
imiona = ['James', 'Charles', 'Dude']
for imie in imiona:
    print(imie)

print("")
print(imiona[0])
print(imiona[len(imiona)-1])

#str.format()
print("\nstr.format():::")
lcz = 2
print(str.format("Wartosc liczby to {}, a {} to jej druga potega", lcz, lcz*lcz))

#Ogarnac str.format w pythonie!!! Zad dom: Wszystkie polecenia w pdf zrobic, od 20 zapisac na gicie. Ogarnac 02 before class