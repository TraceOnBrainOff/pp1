d = {
    "Java":61,
    "Python": 47,
    "JavaScript":37,
    "C++":32,
    "C#":26,
    "Ruby":18,
    "Perl":14,
    "PHP":14,
    "C":9,
    "Android":7
}
def rysujWykres(d):
    a = d.keys()
    longestKey = 0
    for key in a:
        if len(key) > longestKey:
            longestKey = len(key)
    for key in a:
        toPrint = ""
        for i in range(longestKey-len(key)):
            toPrint+=" " #padding
        toPrint+=key + ": " + "#"*d[key]
        print(toPrint)

rysujWykres(d)