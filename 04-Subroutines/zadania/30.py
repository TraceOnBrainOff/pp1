import random

def parzysteZPrzedziału(r, n):
    p = 0
    np = 0
    for j in range(1, r+1):
        i = random.randrange(1, n+1)
        if i%2==0:
            p+=1
        else:
            np+=1
    print(f'Częstotliwość w przedziale <1, {n}>:\n Parzyste: {p/r}\nNieparzyste: {np/r}')

parzysteZPrzedziału(1000, 50)
