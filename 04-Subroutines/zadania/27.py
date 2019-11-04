import re

st = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."

def liczSamogloski(st=st):
    a = re.findall('[aeiouyąęó]', st)
    print(len(a)/len(st))

liczSamogloski()