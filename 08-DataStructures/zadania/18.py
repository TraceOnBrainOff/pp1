import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__)) # the vscode python extension sucks

with open(os.path.abspath(os.path.join(dir_path, "film.json"))) as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)
