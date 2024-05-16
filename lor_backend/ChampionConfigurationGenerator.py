import numpy as np
import random
import json
import os
from typing import Dict, List, Tuple, Union
from pprint import pprint
from django.conf import settings


class ChampionConfigurationGenerator:

    BOOTS_NAME: List[str] = [
        "berserker's_greaves",
        "ionian_boots_of_lucidity",
        "plated_steelcaps",
        "mercury's_treads",
        "sorcerer's_shoes",
        "boots_of_swiftness",
        "mobility_boots",
    ]

    SUPPORT_ITEMS: List[str] = [
        "bloodsong",
        "celestial_opposition",
        "dream_maker",
        "solstice_sleigh",
        "zaz'zak's_realmspike",
    ]

    JUNGLE_ITEMS: List[str] = [
        "gustwalker_hatchling",
        "mosstomper_seedling",
        "scorchclaw_pup",
    ]

    UNIQUE_PASSIVES: List[List[str]] = [
        [
            "lord_dominik's_regards",
            "mortal_reminder",
            "serylda's_grudge",
            "black_cleaver",
            "terminus",
        ],
        ["titanic_hydra", "ravenous_hydra", "stridebreaker", "profane_hydra"],
        ["fimbulwinter", "muramana", "seraph's_embrace"],
        ["cryptobloom", "void_staff", "terminus", "guinsoo's_rageblade"],
        ["essence_reaver", "lich_bane", "trinity_force", "iceborn_gauntlet"],
        ["infinity_edge", "navori_quickblades"],
        ["trailblazer", "dead_man's_plate"],
        ["seraph's_embrace", "shieldbow", "maw_of_malmortius", "sterak's_gage"],
    ]

    def __init__(self):
        self.assets_dir = os.path.join(settings.BASE_DIR, "static")

        self.champions_json_path = os.path.join(self.assets_dir, "champions.json")
        self.items_json_path = os.path.join(self.assets_dir, "items.json")
        self.runes_json_path = os.path.join(self.assets_dir, "runes.json")
        self.summoner_spells_json_path = os.path.join(self.assets_dir, "summoners.json")

        self.champion_data = self.load_json(self.champions_json_path)
        self.item_data = self.load_json(self.items_json_path)
        self.rune_data = self.load_json(self.runes_json_path)
        self.summoner_spell_data = self.load_json(self.summoner_spells_json_path)

    def load_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("File {} not found".format(file_path))
            return {}

    def generate_random_champion_configuration_with_url(
        self,
        champion_configuration: Dict[str, str] = None,
        allowedChampionList: List[str] = None,
        lanes_available: List[str] = ["top", "jungle", "middle", "bottom", "support"],
    ) -> Dict[str, Dict[str, str]]:
        if champion_configuration is None:
            champion_configuration = self.generate_random_champion_configuration(
                allowedChampionList, lanes_available
            )
        return self.champion_to_url(champion_configuration)

    def generate_random_champion_configuration(
        self,
        allowedChampionList: List[str] = None,
        lanes_available: List[str] = ["top", "jungle", "middle", "bottom", "support"],
    ) -> Dict[str, str]:
        name: str = self.get_random_champion_name(allowedChampionList)
        spell_to_max: int = self.get_random_spell_to_max()
        lane: str = self.get_random_lane(lanes_available)
        items: List[str] = self.get_random_items(name, lane)
        starting_item: str = self.get_random_starting_item(lane)
        summoner_spells: List[str] = self.get_random_summoner_spells(lane)
        runes: Tuple[str, List[str], str, List[str], List[str]] = (
            self.get_random_runes()
        )

        champion_configuration: Dict[str, Union[int, str]] = {
            "name": name,
            "role": lane,
            "spell_to_max": int(spell_to_max),
            "summoner_spell_1": summoner_spells[0],
            "summoner_spell_2": summoner_spells[1],
            "rune_main_tree": runes[0],
            "rune_main_keystone": runes[1][0],
            "rune_main_1": runes[1][1],
            "rune_main_2": runes[1][2],
            "rune_main_3": runes[1][3],
            "rune_secondary_tree": runes[2],
            "rune_secondary_1": runes[3][0],
            "rune_secondary_2": runes[3][1],
            "rune_shard_1": runes[4][0],
            "rune_shard_2": runes[4][1],
            "rune_shard_3": runes[4][2],
            "item_1": items[0],
            "item_2": items[1],
            "item_3": items[2],
            "item_4": items[3],
            "item_5": items[4],
            "item_6": items[5],
            "starter_item": starting_item,
        }

        return champion_configuration

    def get_rune_icon(self, slot_index, rune_index):
        runes = self.rune_data["Shards"]["slots"][slot_index]["runes"]
        for rune in runes:
            if rune["key"] == rune_index:
                return rune["icon"]
        return None

    def champion_to_url(
        self, current_champion: Dict[str, str]
    ) -> Dict[str, Dict[str, str]]:
        champion_configuration: Dict[str, Dict[str, str]] = {
            "name": current_champion["name"],
            "icon": f"https://ddragon.leagueoflegends.com/cdn/14.8.1/img/champion/{current_champion['name']}.png",
            "role": [
                current_champion["role"],
                f"https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/{current_champion['role']}.png",
            ],
            "spell_to_max": [
                current_champion["spell_to_max"],
                self.champion_data[current_champion["name"]]["spells"][
                    int(current_champion["spell_to_max"])
                ],
            ],
            "summoner_spell_1": [
                current_champion["summoner_spell_1"],
                self.summoner_spell_data[current_champion["summoner_spell_1"]]["icon"],
            ],
            "summoner_spell_2": [
                current_champion["summoner_spell_2"],
                self.summoner_spell_data[current_champion["summoner_spell_2"]]["icon"],
            ],
            "rune_main_tree": [
                current_champion["rune_main_tree"],
                self.rune_data[current_champion["rune_main_tree"]]["icon"],
            ],
            "rune_main_keystone": [
                current_champion["rune_main_keystone"],
                self.rune_data[current_champion["rune_main_tree"]]["slots"][0]["runes"][
                    0
                ]["icon"],
            ],
            "rune_main_1": [
                current_champion["rune_main_1"],
                self.rune_data[current_champion["rune_main_tree"]]["slots"][1]["runes"][
                    0
                ]["icon"],
            ],
            "rune_main_2": [
                current_champion["rune_main_2"],
                self.rune_data[current_champion["rune_main_tree"]]["slots"][2]["runes"][
                    0
                ]["icon"],
            ],
            "rune_main_3": [
                current_champion["rune_main_3"],
                self.rune_data[current_champion["rune_main_tree"]]["slots"][3]["runes"][
                    0
                ]["icon"],
            ],
            "rune_secondary_tree": [
                current_champion["rune_secondary_tree"],
                self.rune_data[current_champion["rune_secondary_tree"]]["icon"],
            ],
            "rune_secondary_1": [
                current_champion["rune_secondary_1"],
                self.rune_data[current_champion["rune_secondary_tree"]]["slots"][1][
                    "runes"
                ][0]["icon"],
            ],
            "rune_secondary_2": [
                current_champion["rune_secondary_2"],
                self.rune_data[current_champion["rune_secondary_tree"]]["slots"][2][
                    "runes"
                ][0]["icon"],
            ],
            "rune_shard_1": [
                current_champion["rune_shard_1"],
                next(
                    (
                        rune["icon"]
                        for rune in self.rune_data["Shards"]["slots"][0]["runes"]
                        if rune["key"] == current_champion["rune_shard_1"]
                    ),
                    None,
                ),
            ],
            "rune_shard_2": [
                current_champion["rune_shard_2"],
                next(
                    (
                        rune["icon"]
                        for rune in self.rune_data["Shards"]["slots"][1]["runes"]
                        if rune["key"] == current_champion["rune_shard_2"]
                    ),
                    None,
                ),
            ],
            "rune_shard_3": [
                current_champion["rune_shard_3"],
                next(
                    (
                        rune["icon"]
                        for rune in self.rune_data["Shards"]["slots"][2]["runes"]
                        if rune["key"] == current_champion["rune_shard_3"]
                    ),
                    None,
                ),
            ],
            "item_1": [
                current_champion["item_1"],
                self.item_data[current_champion["item_1"]]["icon"],
            ],
            "item_2": [
                current_champion["item_2"],
                self.item_data[current_champion["item_2"]]["icon"],
            ],
            "item_3": [
                current_champion["item_3"],
                self.item_data[current_champion["item_3"]]["icon"],
            ],
            "item_4": [
                current_champion["item_4"],
                self.item_data[current_champion["item_4"]]["icon"],
            ],
            "item_5": [
                current_champion["item_5"],
                self.item_data[current_champion["item_5"]]["icon"],
            ],
            "item_6": [
                current_champion["item_6"],
                self.item_data[current_champion["item_6"]]["icon"],
            ],
            "starter_item": [
                current_champion["starter_item"],
                self.item_data[current_champion["starter_item"]]["icon"],
            ],
        }

        if "unique_id" in current_champion:
            champion_configuration["unique_id"] = current_champion["unique_id"]

        return champion_configuration

    def get_random_champion_name(
        self, allowedChampionList: List[str] = None
    ) -> Dict[str, str]:
        filtered_champion_ids = list(self.champion_data.keys())

        if allowedChampionList:
            filtered_champion_ids = [
                champion_id
                for champion_id in filtered_champion_ids
                if champion_id in allowedChampionList
            ]

        random_champion_id = np.random.choice(filtered_champion_ids)
        return self.champion_data[random_champion_id]["name"]

    def get_random_spell_to_max(self) -> int:
        return np.random.choice([0, 1, 2])

    def get_random_lane(self, lanes_available: List[str]) -> str:
        # lowercase the lane names and return
        lanes_available = [lane.lower() for lane in lanes_available]
        return np.random.choice(lanes_available)

    def get_random_summoner_spells(self, lane: str) -> List[str]:
        if lane == "jungle":
            return [
                "smite",
                np.random.choice(
                    [
                        spell
                        for spell in self.summoner_spell_data.keys()
                        if spell != "smite"
                    ]
                ),
            ]
        else:
            # Exclude smite for non-junglers
            summoner_spells = [
                spell for spell in self.summoner_spell_data.keys() if spell != "smite"
            ]
            return list(np.random.choice(summoner_spells, size=2, replace=False))

    def get_random_runes(self) -> Tuple[str, List[str], str, List[str], List[str]]:
        primary_tree = np.random.choice(
            [tree for tree in self.rune_data.keys() if tree != "Shards"]
        )
        primary_tree_runes = self.rune_data[primary_tree]["slots"]
        primary_runes = [
            np.random.choice(slot["runes"])["key"] for slot in primary_tree_runes
        ]

        secondary_tree = np.random.choice(
            [
                tree
                for tree in self.rune_data.keys()
                if tree != "Shards" and tree != primary_tree
            ]
        )
        secondary_tree_runes = self.rune_data[secondary_tree]["slots"]
        secondary_runes = [
            np.random.choice(slot["runes"])["key"] for slot in secondary_tree_runes[1:]
        ]
        secondary_runes.pop(random.randint(0, len(secondary_runes) - 1))

        shards = [
            np.random.choice(slot["runes"])["key"]
            for slot in self.rune_data["Shards"]["slots"]
        ]

        return primary_tree, primary_runes, secondary_tree, secondary_runes, shards

    def get_random_items(self, name: str, lane: str) -> List[str]:
        item_names: List[str] = []

        # No boots if she's under 16 years and 10 months old
        if name != "Cassiopeia":
            item_names.append(np.random.choice(self.BOOTS_NAME))

        if lane == "support":
            support_item = np.random.choice(self.SUPPORT_ITEMS)

            item_names.append(support_item)

        legendary_items = [
            item
            for item in self.item_data.keys()
            if self.item_data[item].get("last_upgrade", False)
            and item not in self.SUPPORT_ITEMS
        ]

        while len(item_names) < 6:
            item = random.choice(legendary_items)

            if (
                item in item_names
                or item in self.BOOTS_NAME
                or item in self.SUPPORT_ITEMS
            ):
                continue

            for group in self.UNIQUE_PASSIVES:
                if any(other_item in group for other_item in item_names):
                    continue

            item_names.append(item)
        return item_names

    def get_random_starting_item(self, lane) -> str:
        if lane == "jungle":
            return np.random.choice(self.JUNGLE_ITEMS)
        elif lane == "support":
            return "world_atlas"
        else:
            return np.random.choice(
                [
                    item
                    for item in self.item_data.keys()
                    if self.item_data[item].get("is_starter", False)
                    and item not in self.JUNGLE_ITEMS
                    and item != "world_atlas"
                ]
            )
