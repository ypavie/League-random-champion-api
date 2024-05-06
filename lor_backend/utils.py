import json
import random
import numpy as np
import os

from django.conf import settings


def generate_random_runes(rune_data):
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
    primary_tree = np.random.choice(
        [tree for tree in rune_data.keys() if tree != "Shards"])
    primary_tree_runes = rune_data[primary_tree]["slots"]
    primary_runes = [np.random.choice(
        slot["runes"])["key"] for slot in primary_tree_runes]

    secondary_tree = np.random.choice(
        [tree for tree in rune_data.keys() if tree != "Shards" and tree != primary_tree])
    secondary_tree_runes = rune_data[secondary_tree]["slots"]
    secondary_runes = [np.random.choice(
        slot["runes"])["key"] for slot in secondary_tree_runes[1:]]
    secondary_runes.pop(random.randint(0, len(secondary_runes)-1))

    shards = [
        np.random.choice(slot["runes"])["key"]
        for slot in rune_data["Shards"]["slots"]
    ]

    return primary_tree, primary_runes, secondary_tree, secondary_runes, shards


def generate_random_items(item_data, name):
    item_names = []

    passives_to_exclude = [
        ["Sterak's Gage", "Maw of Malmortius", "Shieldbow", "Archange's Staff"],
        ["Lord Dominik's Regards", "Mortal Reminder", "Serylda's Grudge"],
        ["Titanic Hydra", "Ravenous Hydra"],
        ["Mercurial Scimitar", "Silvermere Dawn"],
        ["Archangel's Staff", "Manamune", "Winter's Approach"]
    ]
    boots_names = [
        "berserkers_greaves",
        "ionian_boots_of_lucidity",
        "plated_steelcaps",
        "mercurys_treads",
        "sorcerers_shoes",
        "boots_of_swiftness"
        "mobility_boots"
    ]

    boot_item = np.random.choice(boots_names)

    # Exclude boots for Cassiopeia
    if name != "Cassiopeia":
        item_names.append(boot_item)

    # Mythic
    mythic_items = [item for item in item_data.keys()
                    if item_data[item].get("mythic", False)]
    item_names.append(random.choice(mythic_items))

    # Legendaries
    legendary_items = [item for item in item_data.keys()
                       if not item_data[item].get("mythic", False) and item_data[item].get("last_upgrade", False)]

    # Pick a random item
    while len(item_names) < 6:
        item = random.choice(legendary_items)

        # Check if the item has any conflicts with already picked items
        conflicts = False
        for group in passives_to_exclude:
            if item in item_names and any(other_item in group for other_item in item_names):
                conflicts = True
                break

        if not conflicts:
            item_names.append(item)
        else:
            legendary_items.remove(item)
    return item_names


def get_random_champion(champion_data, banned_champions_ids):
    champion_ids = [champion_data[champion]["key"]
                    for champion in champion_data]
    print(banned_champions_ids)
    champion_ids = [champion_id for champion_id in champion_ids if str(
        champion_id) not in banned_champions_ids]
    id = np.random.choice(champion_ids)
    return [champion for champion in champion_data if champion_data[champion]["key"] == id][0]


def get_random_spell_to_max():
    return np.random.randint(0, 3)


def get_random_lane(lanes_available):
    return np.random.choice(lanes_available)


def get_random_summoner_spells(lane, summoner_spell_data):
    if lane == "jungle":
        return ["smite", np.random.choice(list(summoner_spell_data.keys()))]
    else:
        # Exclude smite for non-junglers
        summoner_spells = [
            spell for spell in summoner_spell_data.keys() if spell != "smite"]
        return list(np.random.choice(summoner_spells, size=2, replace=False))


def get_random_runes(rune_data):
    return generate_random_runes(rune_data)


def get_random_items(item_data, name):
    return generate_random_items(item_data, name)


def generate_random_match_data(champion_data, banned_champions_ids, lanes_available, summoner_spell_data, rune_data, item_data):
    name = get_random_champion(champion_data, banned_champions_ids)
    spell_to_max = get_random_spell_to_max()
    lane = get_random_lane(lanes_available)
    items = get_random_items(item_data, name)
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
        "item_6": items[5]
    }


def generate_random_champion(banned_champions_ids=[], lanes_available=["top", "jungle", "mid", "adc", "support"]):
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

            return generate_random_match_data(champion_data, banned_champions_ids, lanes_available, summoner_spell_data, rune_data, item_data)

    except FileNotFoundError:
        print("File not found")
        return None, None, None, None, None, None
