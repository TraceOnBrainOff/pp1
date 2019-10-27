pesel = "93021707231" #[0], [1] to ostatnie dwie cyfry roku,  [2],[3] to zakodowany miesiac, [4],[5] to dzien
plec = int(pesel[10])
if plec%2!=0:
    plec = "mezczyzna"
else:
    plec = "kobieta"

offsetStulecia = 0
stulecieIndex = 0
stulecia = [1900, 2000, 2100, 2200, 1800] #2200 ma mniejszy offset niz 1800 bo polacy to zaprogramowali???
stulecieIdentifier = int(pesel[2]+pesel[3]) #3 i 4 litera (identifier stulecia + zaszywrowany miesiac)
done = False
miesiac = 0
rok = 0 #musze nauczyc sie klas, powaznie, to wyglada zle
while not done:
    for i in range(1,13):
        if (stulecieIdentifier-offsetStulecia)==i:
            dzien = int(pesel[4] + pesel[5])
            miesiac = i
            rok = stulecia[stulecieIndex] + int(pesel[0]+pesel[1])
            done = True
    stulecieIndex += 1
    offsetStulecia += 20
    
print("Plec:", plec)
print("Wiek:", 2018-rok) #yea it's cool