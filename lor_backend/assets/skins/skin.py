import json

with open("champion_details.json", "r") as f:
    champion_details = json.load(f)

with open("champions.json", "r") as f:
    champions_data = json.load(f)

# merge the two dictionaries by adding the details to the champions
for detail in champion_details:
    for champion in champions_data:
        if detail == champion:
            champions_data[champion].update(champion_details[detail])

# the following keys should not be list but string: release year, resources, gender
for champion in champions_data:
    for key in champions_data[champion]:
        if key == "release year" or key == "resources" or key == "gender":
            #  check if it's a list
            if isinstance(champions_data[champion][key], list):
                # make realease year a int, else a string
                if key == "release year":
                    champions_data[champion][key] = int(champions_data[champion][key][0])
                else:
                    champions_data[champion][key] = champions_data[champion][key][0]

# save the merged dictionary to updated json
with open("champions_updated.json", "w") as f:
    json.dump(champions_data, f, indent=4)