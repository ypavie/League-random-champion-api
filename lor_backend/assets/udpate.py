import json
from pprint import pprint
# Open the JSON file
with open('champions.json', 'r') as json_file:
    champions = json.load(json_file)

# {
    # "Tristana": {
    #     "id": "Tristana",
    #     "key": "18",
    #     "name": "Tristana",
    #     "icon": "https://ddragon.leagueoflegends.com/cdn/13.17.1/img/champion/Tristana.png",
    #     "class": [
    #         "Marksman",
    #         "Assassin"
    #     ],
    #     "spells": [
    #         "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/spell/TristanaQ.png",
    #         "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/spell/TristanaW.png",
    #         "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/spell/TristanaE.png",
    #         "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/spell/TristanaR.png"
    #     ],
    #     "region": [
    #         "Bandle City"
    #     ],
    #     "gender": "Female",
    #     "positions": [
    #         "Bottom",
    #         "Middle"
    #     ],
    #     "species": [
    #         "Yordle"
    #     ],
    #     "range type": [
    #         "Ranged"
    #     ],
    #     "release year": 2009,
    #     "mana source": "Mana"
    # },

for key, value in champions.items():
    if value['mana source'] != 'Mana':
        value['mana source'] = 'Manaless'

# Save the updated JSON file
with open('champions2.json', 'w') as json_file:
    json.dump(champions, json_file, indent=4)