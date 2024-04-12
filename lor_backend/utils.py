import json
import random
import numpy as np
import os
from typing import List, Dict, Tuple
from pprint import pprint
from django.conf import settings

def generate_random_runes(rune_data: Dict[str, Dict[str, List[Dict[str, List[str]]]]]) -> Tuple[str, List[str], str, List[str], List[str]]:
    """
    Generate a random set of runes for a primary and secondary tree,
    along with shards, based on provided rune data.

    Parameters:
        rune_data (dict): A dictionary containing information about rune trees and slots.

    Returns:
        tuple: A tuple containing the selected primary tree, primary runes,
               secondary tree, secondary runes, and shards.

    Usage:
        - Provide the 'rune_data' dictionary with the necessary rune information.
        - Call this function to obtain a random set of runes for a character.
    """
    primary_tree = np.random.choice([tree for tree in rune_data.keys() if tree != "Shards"])
    primary_tree_runes = rune_data[primary_tree]["slots"]
    primary_runes = [np.random.choice(slot["runes"])["key"] for slot in primary_tree_runes]

    secondary_tree = np.random.choice([tree for tree in rune_data.keys() if tree != "Shards" and tree != primary_tree])
    secondary_tree_runes = rune_data[secondary_tree]["slots"]
    secondary_runes = [np.random.choice(slot["runes"])["key"] for slot in secondary_tree_runes[1:]]
    secondary_runes.pop(random.randint(0, len(secondary_runes)-1))

    shards = [
        np.random.choice(slot["runes"])["key"]
        for slot in rune_data["Shards"]["slots"]
    ]

    return primary_tree, primary_runes, secondary_tree, secondary_runes, shards


def generate_random_items(item_data: Dict[str, Dict[str, bool]], name: str, lane: str) -> List[str]:
    item_names: List[str] = []

    passives_to_exclude: List[str] = [
        ["lord_dominik's_regards", "mortal_reminder", "serylda's_grudge", "black_cleaver", "terminus"],
        ["titanic_hydra", "ravenous_hydra", "stridebreaker", "profane_hydra"],
        ["fimbulwinter", "muramana", "seraph's_embrace"],
        ["cryptobloom", "void_staff", "terminus", "guinsoo's_rageblade"],
        ["essence_reaver", "lich_bane", "trinity_force", "iceborn_gauntlet"],
        ["infinity_edge", "navori_quickblades"],
        ["trailblazer", "dead_man's_plate"],
        ["seraph's_embrace", "shieldbow", "maw_of_malmortius", "sterak's_gage"],
    ]

    boots_names: List[str] = [
        "berserker's_greaves",
        "ionian_boots_of_lucidity",
        "plated_steelcaps",
        "mercury's_treads",
        "sorcerer's_shoes",
        "boots_of_swiftness",
        "mobility_boots"
    ]

    support_items: List[str] = [
        "bloodsong",
        "celestial_opposition",
        "dream_maker",
        "solstice_sleigh",
        "zaz'zak's_realmspike",
    ]

    # No boots if she's under 16 years and 10 months old
    if name != "Cassiopeia":
        item_names.append(np.random.choice(boots_names))
    
    if lane == "support":
        support_item = np.random.choice(support_items)
        item_names.append(support_item)
    
    legendary_items = [item for item in item_data.keys() if item_data[item].get("last_upgrade", False) and item not in support_items]

    while len(item_names) < 6:
        item = random.choice(legendary_items)

        if item in item_names or item in boots_names or item in support_items:
            continue

        for group in passives_to_exclude:
            if any(other_item in group for other_item in item_names):
                continue
            
        item_names.append(item)

    if lane == "jungle":
        jungle_items = [
            "gustwalker_hatchling",
            "mosstomper_seedling",
            "scorchclaw_pup",
        ]
        item_names.append(np.random.choice(jungle_items))
    else:
        starter_item = np.random.choice([item for item in item_data.keys() if item_data[item].get("is_starter", False)])
        item_names.append(starter_item)

    return item_names


def get_random_champion(champion_data: Dict[str, Dict[str, str]], allowedChampionList: List[str]) -> str:
    filtered_champion_ids = list(champion_data.keys())
    
    if allowedChampionList:
        filtered_champion_ids = [champion_id for champion_id in filtered_champion_ids if champion_id in allowedChampionList]

    random_champion_id = np.random.choice(filtered_champion_ids)
    return champion_data[random_champion_id]["name"]


def get_random_spell_to_max() -> int:
    return np.random.randint(0, 3)


def get_random_lane(lanes_available: List[str]) -> str:
    return np.random.choice(lanes_available)


def get_random_summoner_spells(lane: str, summoner_spell_data: Dict[str, Dict[str, bool]]) -> List[str]:
    if lane == "jungle":
        return ["smite", np.random.choice([spell for spell in summoner_spell_data.keys() if spell != "smite"])]
    else:
        # Exclude smite for non-junglers
        summoner_spells = [
            spell for spell in summoner_spell_data.keys() if spell != "smite"]
        return list(np.random.choice(summoner_spells, size=2, replace=False))


def get_random_runes(rune_data: Dict[str, Dict[str, List[Dict[str, List[str]]]]]) -> Tuple[str, List[str], str, List[str], List[str]]:
    return generate_random_runes(rune_data)


def get_random_items(item_data: Dict[str, Dict[str, bool]], name: str, lane: str) -> List[str]:
    return generate_random_items(item_data, name, lane)


def generate_random_match_data(champion_data: Dict[str, Dict[str, str]], allowedChampionList: List[str], lanes_available: str, summoner_spell_data: Dict[str, Dict[str, bool]], rune_data: Dict[str, Dict[str, List[Dict[str, List[str]]]]], item_data: Dict[str, Dict[str, bool]]) -> Dict[str, str]:
    name = get_random_champion(champion_data, allowedChampionList)
    spell_to_max = get_random_spell_to_max()
    lane = get_random_lane(lanes_available)
    items = get_random_items(item_data, name, lane)
    summoner_spells = get_random_summoner_spells(lane, summoner_spell_data)
    runes = get_random_runes(rune_data)

    return {
        "name": name,
        "role": lane,
        "spell_to_max": spell_to_max,
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
        "starter_item": items[6],
    }


def generate_random_champion(allowedChampionList: List[str] = None, lanes_available = ["top", "jungle", "mid", "adc", "support"]) -> Dict[str, str]:
    assets_dir = os.path.join(settings.BASE_DIR, 'lor_backend', 'assets')
    champions_json_path = os.path.join(assets_dir, 'champions.json')
    items_json_path = os.path.join(assets_dir, 'items.json')
    runes_json_path = os.path.join(assets_dir, 'runes.json')
    summoner_spells_json_path = os.path.join(assets_dir, 'summoners.json')

    try:
        with open(champions_json_path, 'r') as champions_json, \
                open(items_json_path, 'r') as items_json, \
                open(runes_json_path, 'r') as runes_json, \
                open(summoner_spells_json_path, 'r') as summoner_spells_json:

            champion_data = json.load(champions_json)
            item_data = json.load(items_json)
            rune_data = json.load(runes_json)
            summoner_spell_data = json.load(summoner_spells_json)

            return generate_random_match_data(champion_data, allowedChampionList, lanes_available, summoner_spell_data, rune_data, item_data)

    except FileNotFoundError:
        print("File not found")
        return None, None, None, None, None, None

def champion_to_url(current_champion: Dict[str, Dict[str, str]]) -> str:
    assets_dir = os.path.join(settings.BASE_DIR, 'lor_backend', 'assets')
    champions_json_path = os.path.join(assets_dir, 'champions.json')
    items_json_path = os.path.join(assets_dir, 'items.json')
    runes_json_path = os.path.join(assets_dir, 'runes.json')
    summoner_spells_json_path = os.path.join(assets_dir, 'summoners.json')

    try:
        with open(champions_json_path, 'r') as champions_json, \
                open(items_json_path, 'r') as items_json, \
                open(runes_json_path, 'r') as runes_json, \
                open(summoner_spells_json_path, 'r') as summoner_spells_json:

            champion_data = json.load(champions_json)
            item_data = json.load(items_json)
            rune_data = json.load(runes_json)
            summoner_spell_data = json.load(summoner_spells_json)
            roles = {
                "top": "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/top.png",
                "jungle": "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/jungle.png",
                "mid": "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/middle.png",
                "adc": "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/bottom.png",
                "support": "https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/support.png",
            }

            champion_with_urls = {}

            champion_with_urls["name"] = current_champion["name"].replace(" ", "")
            
            champion_with_urls["icon"] = champion_data[champion_with_urls["name"]]["icon"]

            champion_with_urls["role"] = [current_champion["role"], roles[current_champion["role"]]]

            current_spell_to_max = ["Q", "W", "E"][int(current_champion["spell_to_max"])]
            current_spell_to_max_url = champion_data[champion_with_urls["name"]]["spells"][int(current_champion["spell_to_max"])]
            champion_with_urls["spell_to_max"] = [
                current_spell_to_max,
                current_spell_to_max_url,
            ]

            champion_with_urls["summoner_spell_1"] = [
                current_champion["summoner_spell_1"],
                summoner_spell_data[current_champion["summoner_spell_1"]]["icon"],
            ]

            champion_with_urls["summoner_spell_2"] = [
                current_champion["summoner_spell_2"],
                summoner_spell_data[current_champion["summoner_spell_2"]]["icon"],
            ]
            
            champion_with_urls["rune_main_tree"] = [
                current_champion["rune_main_tree"],
                rune_data[current_champion["rune_main_tree"]]["icon"],
            ]

            champion_with_urls["rune_main_keystone"] = [
                current_champion["rune_main_keystone"],
                next(rune["icon"] for rune in rune_data[current_champion["rune_main_tree"]]["slots"][0]["runes"] if rune["key"] == current_champion["rune_main_keystone"]),
            ]

            champion_with_urls["rune_main_1"] = [
                current_champion["rune_main_1"],
                next(rune["icon"] for rune in rune_data[current_champion["rune_main_tree"]]["slots"][1]["runes"] if rune["key"] == current_champion["rune_main_1"]),
            ]

            champion_with_urls["rune_main_2"] = [
                current_champion["rune_main_2"],
                next(rune["icon"] for rune in rune_data[current_champion["rune_main_tree"]]["slots"][2]["runes"] if rune["key"] == current_champion["rune_main_2"]),
            ]

            champion_with_urls["rune_main_3"] = [
                current_champion["rune_main_3"],
                next(rune["icon"] for rune in rune_data[current_champion["rune_main_tree"]]["slots"][3]["runes"] if rune["key"] == current_champion["rune_main_3"]),
            ]

            champion_with_urls["rune_secondary_tree"] = [
                current_champion["rune_secondary_tree"],
                rune_data[current_champion["rune_secondary_tree"]]["icon"],
            ]

            matched_secondary_runes = []

            for slot in range(4):
                for rune in rune_data[current_champion["rune_secondary_tree"]]["slots"][slot]["runes"]:
                    if rune["key"] == current_champion["rune_secondary_1"] or rune["key"] == current_champion["rune_secondary_2"]:
                        matched_secondary_runes.append(rune["icon"])

                if len(matched_secondary_runes) == 2:
                    break

            champion_with_urls["rune_secondary_1"] = [
                current_champion["rune_secondary_1"],
                matched_secondary_runes[0] if len(matched_secondary_runes) >= 1 else None
            ]

            champion_with_urls["rune_secondary_2"] = [
                current_champion["rune_secondary_2"],
                matched_secondary_runes[1] if len(matched_secondary_runes) == 2 else None
            ]

            champion_with_urls["rune_shard_1"] = [
                current_champion["rune_shard_1"],
                next(rune["icon"] for rune in rune_data["Shards"]["slots"][0]["runes"] if rune["key"] == current_champion["rune_shard_1"]),
            ]

            champion_with_urls["rune_shard_2"] = [
                current_champion["rune_shard_2"],
                next(rune["icon"] for rune in rune_data["Shards"]["slots"][1]["runes"] if rune["key"] == current_champion["rune_shard_2"]),
            ]

            champion_with_urls["rune_shard_3"] = [
                current_champion["rune_shard_3"],
                next(rune["icon"] for rune in rune_data["Shards"]["slots"][2]["runes"] if rune["key"] == current_champion["rune_shard_3"]),
            ]
            

            champion_with_urls["item_1"] = [
                current_champion["item_1"],
                item_data[current_champion["item_1"]]["icon"],
            ]

            champion_with_urls["item_2"] = [
                current_champion["item_2"],
                item_data[current_champion["item_2"]]["icon"],
            ]

            champion_with_urls["item_3"] = [
                current_champion["item_3"],
                item_data[current_champion["item_3"]]["icon"],
            ]

            champion_with_urls["item_4"] = [
                current_champion["item_4"],
                item_data[current_champion["item_4"]]["icon"],
            ]
            
            champion_with_urls["item_5"] = [
                current_champion["item_5"],
                item_data[current_champion["item_5"]]["icon"],
            ]

            champion_with_urls["item_6"] = [
                current_champion["item_6"],
                item_data[current_champion["item_6"]]["icon"],
            ]

            champion_with_urls["starter_item"] = [
                current_champion["starter_item"],
                item_data[current_champion["starter_item"]]["icon"],
            ]

            champion_with_urls["unique_id"] = current_champion["unique_id"]
            return champion_with_urls

    except FileNotFoundError:
        print("File not found")
        return {}
