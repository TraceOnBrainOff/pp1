import re
st = "To be, or not to be, that is the question"

a = re.findall('[aeiouy]', st)
print(a)