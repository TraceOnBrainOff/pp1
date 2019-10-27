w = int(input("Podaj wage: "))
h = int(input("Podaj wzrost: "))/100
BMI = w/(h**2)

print("Wskaznik BMI: ", BMI)
if BMI > 18.5 and BMI < 25:
    print("Waga prawidlowa")