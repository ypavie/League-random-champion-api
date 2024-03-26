import json

with open("skinlines.json", "r") as f:
    skinlines = json.load(f)

with open("possible_values.json", "r") as f:
    possible_values = json.load(f)

keys = list(skinlines.keys())

possible_values["Skinlines"] = keys

for pv in possible_values:
    # order asc
    possible_values[pv].sort()

with open("possible_values.json", "w") as f:
    json.dump(possible_values, f, indent=4)