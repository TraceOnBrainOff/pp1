limit = 50
predkosc = 73

if predkosc > limit:
    _ = predkosc - limit
    if _ <= 10:
        print("Mandat (zl):", _*5)
    else:
        print("Mandat (zl):", _*15) #w definicji zadania jest blad