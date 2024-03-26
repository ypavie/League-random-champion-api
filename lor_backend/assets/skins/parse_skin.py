# [
#     {
#       "id": -1,
#       "name": "None",
#       "alias": "None",
#       "squarePortraitPath": "/lol-game-data/assets/v1/champion-icons/-1.png",
#       "roles": [
        
#       ]
#     },
#     {

import json
from pprint import pprint

CHAMPION_NAMES = ["Annie", "Olaf", "Galio", "Twisted Fate", "Xin Zhao", "Urgot", "LeBlanc", "Vladimir", "Fiddlesticks", "Kayle", "Master Yi", "Alistar", "Ryze", "Sion", "Sivir", "Soraka", "Teemo", "Tristana", "Warwick", "Nunu & Willump", "Miss Fortune", "Ashe", "Tryndamere", "Jax", "Morgana", "Zilean", "Singed", "Evelynn", "Twitch", "Karthus", "Cho'Gath", "Amumu", "Rammus", "Anivia", "Shaco", "Dr. Mundo", "Sona", "Kassadin", "Irelia", "Janna", "Gangplank", "Corki", "Karma", "Taric", "Veigar", "Trundle", "Swain", "Caitlyn", "Blitzcrank", "Malphite", "Katarina", "Nocturne", "Maokai", "Renekton", "Jarvan IV", "Elise", "Orianna", "Wukong", "Brand", "Lee Sin", "Vayne", "Rumble", "Cassiopeia", "Skarner", "Heimerdinger", "Nasus", "Nidalee", "Udyr", "Poppy", "Gragas", "Pantheon", "Ezreal", "Mordekaiser", "Yorick", "Akali", "Kennen", "Garen", "Leona", "Malzahar", "Talon", "Riven", "Kog'Maw", "Shen", "Lux", "Xerath", "Shyvana", "Ahri", "Graves", "Fizz", "Volibear", "Rengar", "Varus", "Nautilus", "Viktor", "Sejuani", "Fiora", "Ziggs", "Lulu", "Draven", "Hecarim", "Kha'Zix", "Darius", "Jayce", "Lissandra", "Diana", "Quinn", "Syndra", "Aurelion Sol", "Kayn", "Zoe", "Zyra", "Kai'Sa", "Seraphine", "Gnar", "Zac", "Yasuo", "Vel'Koz", "Taliyah", "Camille", "Akshan", "Bel'Veth", "Braum", "Jhin", "Kindred", "Zeri", "Jinx", "Tahm Kench", "Briar", "Viego", "Senna", "Lucian", "Zed", "Kled", "Ekko", "Qiyana", "Vi", "Aatrox", "Nami", "Azir", "Yuumi", "Samira", "Thresh", "Illaoi", "Rek'Sai", "Ivern", "Kalista", "Bard", "Rakan", "Xayah", "Ornn", "Sylas", "Neeko", "Aphelios", "Rell", "Pyke", "Vex", "Yone", "Sett", "Lillia", "Gwen", "Renata Glasc", "Nilah", "K'Sante", "Smolder", "Milio", "Hwei", "Naafiri"]

# {
#     "1000": {
#       "id": 1000,
#       "isBase": true,
#       "name": "Annie",
#       "splashPath": "/lol-game-data/assets/v1/champion-splashes/1/1000.jpg",
#       "uncenteredSplashPath": "/lol-game-data/assets/v1/champion-splashes/uncentered/1/1000.jpg",
#       "tilePath": "/lol-game-data/assets/v1/champion-tiles/1/1000.jpg",
#       "loadScreenPath": "/lol-game-data/assets/ASSETS/Characters/Annie/Skins/Base/AnnieLoadScreen.jpg",
#       "skinType": "",
#       "rarity": "kNoRarity",
#       "isLegacy": false,
#       "splashVideoPath": null,
#       "collectionSplashVideoPath": null,
#       "featuresText": null,
#       "chromaPath": null,
#       "emblems": null,
#       "regionRarityId": 0,
#       "rarityGemPath": null,
#       "skinLines": null,
#       "skinAugments": null,
#       "description": null
#     },
#     "1001": {
#       "id": 1001,
#       "isBase": false,
#       "name": "Goth Annie",
#       "splashPath": "/lol-game-data/assets/v1/champion-splashes/1/1001.jpg",
#       "uncenteredSplashPath": "/lol-game-data/assets/v1/champion-splashes/uncentered/1/1001.jpg",
#       "tilePath": "/lol-game-data/assets/v1/champion-tiles/1/1001.jpg",
#       "loadScreenPath": "/lol-game-data/assets/ASSETS/Characters/Annie/Skins/Skin01/AnnieLoadScreen_1.jpg",
#       "skinType": "",
#       "rarity": "kNoRarity",
#       "isLegacy": false,
#       "splashVideoPath": null,
#       "collectionSplashVideoPath": null,
#       "featuresText": null,
#       "chromaPath": null,
#       "emblems": null,
#       "regionRarityId": 0,
#       "rarityGemPath": null,
#       "skinLines": [
#         {
#           "id": 110
#         }
#       ],
#       "skinAugments": null,
#       "description": "Her mother is dead. Her father is dead. But Annie remains, seeing beauty in the dark."
#     },

# open skinlines.json
with open("skins.json", "r", encoding="utf-8") as f:
    skins = json.load(f)

champion_skins = {}
for key, value in skins.items():
    path = value["loadScreenPath"] # /lol-game-data/assets/ASSETS/Characters/Annie/Skins/Skin01/AnnieLoadScreen_1.jpg
    # get champion name
    champion_name = path.split("/")[5]
    
    skinslines = value["skinLines"]
    # convert to an array of ids in a one liner
    skinlines = [skinline["id"] for skinline in skinslines] if skinslines else []

    # duplicate the skinlines inside the champion_skins dict
    if champion_name not in champion_skins:
        champion_skins[champion_name] = []
    champion_skins[champion_name] += skinlines

pprint(champion_skins)

# open skinlines.json
with open("skinlines.json", "r", encoding="utf-8") as f:
    skins = json.load(f)

# [
#     {
#       "id": 0,
#       "name": "",
#       "description": ""
#     },
#     {
#       "id": 1,
#       "name": "World Champions: 2011",
#       "description": "Congratulations to your Worlds winners for 2011: Fnatic!"
#     },
#     {
#       "id": 2,
#       "name": "World Champions: 2012",
#       "description": "Congratulations to your Worlds winners for 2012: Taipei Assassins!"
#     },

skinlines = {}

# go through each skinlines, use the name as the key and store the name of every champion that has that skinline, using the id and the skinline and ids from champion_skins
for skinline in skins:
    name = skinline["name"]
    id = skinline["id"]
    skinlines[name] = [champion_name for champion_name, skinline_ids in champion_skins.items() if id in skinline_ids]

pprint(skinlines)

# save to skins.json
with open("skinlines.json", "w", encoding="utf-8") as f:
    json.dump(skinlines, f, ensure_ascii=False, indent=4) 
