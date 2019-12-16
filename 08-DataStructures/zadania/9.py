osoba = {
    "imie": "Marek",
    "nazwisko": "Banach",
    "wiek": 25,
    "hobby": ["programowanie","wycieczki"],
    "student": True,
    "telefon":{"stacjonarny":"2233","komorkowy":"7788"}
}
print(osoba)
print(osoba['nazwisko'])
print(osoba['hobby'])
osoba['nazwisko'] = "Nowak"
osoba['student'] = False
osoba['plec'] = "mezczyzna"
osoba['hobby'].append("rower")
osoba['telefon']['sluzbowy'] = 3131
print(osoba)