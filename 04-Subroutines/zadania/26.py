def podatek(dochod):
    if dochod <= 5000:
        return dochod*0.17
    else:
        a = 5000*0.17
        b = (dochod-5000)*0.32
        return a+b

print(podatek(6000))