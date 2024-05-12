# League random champion API

API inspired by [Ultimate Bravery](https://ultimate-bravery.net/) to generate random champion builds.
Currently supporting patch 14.6.1.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ypavie/League-random-champion-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd League-random-champion-api
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open a web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the League of Randoms application.

3. Generate Random Combinations:
    - You can make a POST request to the `/random_champion` endpoint with optional parameters `allowedChampionList` and `lanes` to specify champions and lanes to filter from.

4. Enjoy the Challenge:
    - Follow the instructions provided for the generated combination and apply them in your League of Legends matches.

## Endpoints

- `GET /champion/<int:id>`: Retrieve a specific champion configuration by ID.

    Example response:
    ```json
    {
    "name": "Lulu",
    "icon": "https://ddragon.leagueoflegends.com/cdn/14.8.1/img/champion/Lulu.png",
    "role": [
        "mid",
        "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/mid.png"
    ],
    "spell_to_max": [
        "1",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/spell/LuluW.png"
    ],
    "summoner_spell_1": [
        "teleport",
        "https://ddragon.leagueoflegends.com/cdn/13.16.1/img/spell/SummonerTeleport.png"
    ],
    "summoner_spell_2": [
        "barrier",
        "https://ddragon.leagueoflegends.com/cdn/13.16.1/img/spell/SummonerBarrier.png"
    ],
    "rune_main_tree": [
        "Precision",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7201_Precision.png"
    ],
    "rune_main_keystone": [
        "Fleet Footwork",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/PressTheAttack/PressTheAttack.png"
    ],
    "rune_main_1": [
        "Triumph",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Overheal.png"
    ],
    "rune_main_2": [
        "Legend Bloodline",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LegendAlacrity/LegendAlacrity.png"
    ],
    "rune_main_3": [
        "Coup De Grace",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/CoupDeGrace/CoupDeGrace.png"
    ],
    "rune_secondary_tree": [
        "Sorcery",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7202_Sorcery.png"
    ],
    "rune_secondary_1": [
        "Mana flowBand",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/NullifyingOrb/Pokeshield.png"
    ],
    "rune_secondary_2": [
        "Scorch",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/Transcendence/Transcendence.png"
    ],
    "rune_shard_1": [
        "Adaptive Force",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/StatMods/StatModsAdaptiveForceIcon.png"
    ],
    "rune_shard_2": [
        "Movement Speed",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/StatMods/StatModsMovementSpeedIcon.png"
    ],
    "rune_shard_3": [
        "Tenacity and Slow Resist",
        "https://ddragon.leagueoflegends.com/cdn/img/perk-images/StatMods/StatModsTenacityIcon.png"
    ],
    "item_1": [
        "ionian_boots_of_lucidity",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/3158.png"
    ],
    "item_2": [
        "immortal_shieldbow",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/6673.png"
    ],
    "item_3": [
        "stormrazor",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/3095.png"
    ],
    "item_4": [
        "runaan's_hurricane",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/3085.png"
    ],
    "item_5": [
        "bloodthirster",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/3072.png"
    ],
    "item_6": [
        "cosmic_drive",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/4629.png"
    ],
    "starter_item": [
        "cull",
        "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/item/1083.png"
    ],
    "unique_id": 252525
    ```

- `GET /data/<str:file>`: Retrieve data files (e.g., champions, items) in JSON format.

- `POST /random_champion`: Generate a random champion configuration. Accepts optional parameters for allowed champions and available lanes.

    Example request:
    ```json
    {
        "allowedChampionList": ["Ahri", "Annie", "Lulu"],
        "lanes": ["mid", "top"]
    }
    ```

    Example response:
    ```json
    {
        "name": "Lulu",
        "icon": "https://ddragon.leagueoflegends.com/cdn/14.8.1/img/champion/Lulu.png",
        "role": [
            "mid",
            "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/mid.png"
        ],
        "...": ["..."]
    }
    ```


## License

This project is licensed under the [MIT License](LICENSE).

League-random-champion-api is not endorsed by Riot Games and does not reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games and all associated properties are trademarks or registered trademarks of Riot Games, Inc

## Acknowledgements

League of Randoms is inspired by the Ultimate Bravery game mode.
