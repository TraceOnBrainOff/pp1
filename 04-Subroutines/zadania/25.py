imiona = ["Janek", "Ania", "Wojtek", "Zosia"]
def imieIstnieje(imie, t=imiona):
    for a in t:
        if imie == a:
            print("Istnieje")
            return
    print("Nie istnieje")

imieIstnieje("Wojtek")