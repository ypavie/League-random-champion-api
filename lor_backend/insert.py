import json
from models import Champion

# Load the JSON data
with open("assets/champions.json") as json_file:
    json_data = json.load(json_file)

    # Loop through the JSON data and create Champion instances
    for champ_id, champ_data in json_data.items():
        name = champ_data.get("name")
        icon_url = champ_data.get("icon")

        if name and icon_url:
            Champion.objects.create(name=name, image_url=icon_url)
            print(f"Created champion: {name}")

    print('Successfully loaded champions')
