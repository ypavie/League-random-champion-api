import json
from pprint import pprint
    
with open("items.json", "r") as f:
    items = json.load(f)
    
starter_items = [
    "dark_seal",
    "doran's_blade",
    "doran's_ring",
    "doran's_shield",
    "world_atlas",
    "corrupting_potion",
    "cull",
]

for key, value in items.items():
    items[key]["is_starter"] = key in starter_items

with open("items2.json", "w") as f:
    json.dump(items, f, indent=4)

