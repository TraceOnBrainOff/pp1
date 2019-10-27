cyfry = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec", "dziesiec"]
a = 300
b = str(a)
result = ""
for i in range(len(b)):
    result += cyfry[int(b[i])] + " "

print(result)