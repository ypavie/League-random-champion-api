from typing import List
from pprint import pprint
import unittest
from unittest.mock import patch
from ChampionConfigurationGenerator import ChampionConfigurationGenerator

class TestChampionConfigurationGenerator(unittest.TestCase):
    
    def setUp(self):
        self.championConfigurationGenerator = ChampionConfigurationGenerator()


    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_champion_name', return_value="Pantheon")
    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_spell_to_max', return_value=0)
    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_lane', return_value="jungle")
    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_items', return_value=["ionian_boots_of_lucidity", "rylai's_crystal_scepter", "sunfire_aegis", "nashor's_tooth", "runaan's_hurricane", "void_staff"])
    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_starting_item', return_value="mosstomper_seedling")
    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_summoner_spells', return_value=["smite", "exhaust"])
    @patch('ChampionConfigurationGenerator.ChampionConfigurationGenerator.get_random_runes', return_value=("Inspiration", ["Unsealed Spellbook", "Triple Tonic", "Minion Dematerializer", "Time Warp Tonic"], "Precision", ["Legend Bloodline", "Last Stand"], ["Attack Speed", "Scaling Health", "Flat Health"]))
    def test_generate_random_champion_configuration(self, mock_runes, mock_summoner_spells, mock_starting_item, mock_items, mock_lane, mock_spell_to_max, mock_champion_name):
        allowed_champion_list = ["Champion1", "Champion2"]
        lanes_available = ["top", "jungle", "mid", "adc", "support"]

        champion_configuration = self.championConfigurationGenerator.generate_random_champion_configuration(
            allowedChampionList=allowed_champion_list,
            lanes_available=lanes_available
        )

        self.assertEqual(champion_configuration["name"], "Pantheon")
        self.assertEqual(champion_configuration["role"], "jungle")
        self.assertEqual(champion_configuration["spell_to_max"], 0)
        self.assertEqual(champion_configuration["summoner_spell_1"], "smite")
        self.assertEqual(champion_configuration["summoner_spell_2"], "exhaust")
        self.assertEqual(champion_configuration["rune_main_tree"], "Inspiration")
        self.assertEqual(champion_configuration["rune_main_keystone"], "Unsealed Spellbook")
        self.assertEqual(champion_configuration["rune_main_1"], "Triple Tonic")
        self.assertEqual(champion_configuration["rune_main_2"], "Minion Dematerializer")
        self.assertEqual(champion_configuration["rune_main_3"], "Time Warp Tonic")
        self.assertEqual(champion_configuration["rune_secondary_tree"], "Precision")
        self.assertEqual(champion_configuration["rune_secondary_1"], "Legend Bloodline")
        self.assertEqual(champion_configuration["rune_secondary_2"], "Last Stand")
        self.assertEqual(champion_configuration["rune_shard_1"], "Attack Speed")
        self.assertEqual(champion_configuration["rune_shard_2"], "Scaling Health")
        self.assertEqual(champion_configuration["rune_shard_3"], "Flat Health")
        self.assertEqual(champion_configuration["item_1"], "ionian_boots_of_lucidity")
        self.assertEqual(champion_configuration["item_2"], "rylai's_crystal_scepter")
        self.assertEqual(champion_configuration["item_3"], "sunfire_aegis")
        self.assertEqual(champion_configuration["item_4"], "nashor's_tooth")
        self.assertEqual(champion_configuration["item_5"], "runaan's_hurricane")
        self.assertEqual(champion_configuration["item_6"], "void_staff")
        self.assertEqual(champion_configuration["starter_item"], "mosstomper_seedling")


    def test_get_random_spell_to_max(self):
        spell: int = self.championConfigurationGenerator.get_random_spell_to_max()
        self.assertIn(spell, [0, 1, 2])

    @patch('numpy.random.choice')
    def test_get_random_lane(self, mock_random_choice):
        mock_random_choice.return_value = 'mid'
        lane: str = self.championConfigurationGenerator.get_random_lane(['mid', 'top', 'jungle', 'bot', 'support'])
        self.assertEqual(lane, 'mid')

    def test_get_random_summoner_spells_for_non_jungle(self):
        summs: List[str] = self.championConfigurationGenerator.get_random_summoner_spells(lane='mid')
        self.assertEqual(len(summs), 2)
        self.assertNotIn('smite', summs)
        self.assertNotEqual(summs[0], summs[1])

    def test_get_random_summoner_spells_for_jungle(self):
        summs: List[str] = self.championConfigurationGenerator.get_random_summoner_spells(lane='jungle')
        self.assertEqual(len(summs), 2)
        self.assertIn('smite', summs)
        self.assertNotEqual(summs[0], summs[1])
        summs.remove('smite')
        self.assertNotIn('smite', summs)

    def test_get_random_runes_valid_configuration_primary_tree(self):
        primary_tree, primary_runes, _, _, _ = self.championConfigurationGenerator.get_random_runes()
        rune_data = self.championConfigurationGenerator.rune_data[primary_tree]["slots"]

        for i, rune in enumerate(primary_runes):
            self.assertIn(rune, [rune["key"] for rune in rune_data[i]["runes"]])
    
    def test_get_random_runes_valid_configuration_primary_tree_and_primary_runes_match(self):
        primary_tree, primary_runes, _, _, _ = self.championConfigurationGenerator.get_random_runes()
        rune_data = self.championConfigurationGenerator.rune_data[primary_tree]["slots"]

        primary_tree = "Inspiration" if primary_tree != "Inspiration" else "Precision"
        rune_data = self.championConfigurationGenerator.rune_data[primary_tree]["slots"]

        with self.assertRaises(AssertionError):
            for i, rune in enumerate(primary_runes):
                self.assertIn(rune, [rune["key"] for rune in rune_data[i]["runes"]])

    def test_get_random_runes_valid_configuration_secondary(self):
        _, _, secondary_tree, secondary_runes, _ = self.championConfigurationGenerator.get_random_runes()
        rune_data = self.championConfigurationGenerator.rune_data[secondary_tree]["slots"]

        used_rows = set()
        for rune in secondary_runes:
            for j, slot in enumerate(rune_data):
                if rune in [rune["key"] for rune in slot["runes"]]:
                    used_rows.add(j)
                    break
        
        self.assertEqual(len(used_rows), 2)

    def test_get_random_runes_valid_configuration_shards(self):
        _, _, _, _, shards = self.championConfigurationGenerator.get_random_runes()
        rune_data = self.championConfigurationGenerator.rune_data["Shards"]["slots"]

        for i, rune in enumerate(shards):
            self.assertIn(rune, [rune["key"] for rune in rune_data[i]["runes"]])

    @patch('numpy.random.choice')
    def test_get_random_champion_name(self, mock_random_choice):
        mock_random_choice.return_value = 'Cassiopeia'
        champion: str = self.championConfigurationGenerator.get_random_champion_name()
        self.assertEqual(champion, 'Cassiopeia')

    def test_get_random_items_no_duplicates(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='non_cassiopeia', lane='mid')
        self.assertEqual(len(set(items)), len(items))

    def test_get_random_items_unique_passives_2_duplicates_removed(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='non_cassiopeia', lane='mid')
        unique_passives: List[List[str]] = self.championConfigurationGenerator.UNIQUE_PASSIVES
        
        items.pop()
        items.pop()
        items.append(unique_passives[0][0])
        items.append(unique_passives[0][1])

        with self.assertRaises(AssertionError):
            for item in items:
                for group in unique_passives:
                    if item in group:
                        self.assertFalse(any(other_item in group for other_item in items if other_item != item))
                        break

    def test_get_random_items_total_items(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='non_cassiopeia', lane='mid')
        self.assertEqual(len(items), 6)

    def test_get_random_items_non_cassiopeia(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='non_cassiopeia', lane='mid')
        boots: List[str] = self.championConfigurationGenerator.BOOTS_NAME
        self.assertEqual(len([item for item in items if item in boots]), 1)
    
    def test_get_random_items_cassiopeia(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='Cassiopeia', lane='mid')
        boots: List[str] = self.championConfigurationGenerator.BOOTS_NAME
        self.assertEqual(len([item for item in items if item in boots]), 0)

    def test_get_random_items_support(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='non_cassiopeia', lane='support')
        support_items: List[str] = self.championConfigurationGenerator.SUPPORT_ITEMS
        self.assertEqual(len([item for item in items if item in support_items]), 1)

    def test_get_random_items_non_support(self):
        items: List[str] = self.championConfigurationGenerator.get_random_items(name='non_cassiopeia', lane='mid')
        support_items: List[str] = self.championConfigurationGenerator.SUPPORT_ITEMS
        self.assertEqual(len([item for item in items if item in support_items]), 0)

    @patch('numpy.random.choice')
    def test_get_random_starting_item_jungle(self, mock_random_choice):
        mock_random_choice.return_value = 'scorchclaw_pup'
        item: str = self.championConfigurationGenerator.get_random_starting_item(lane='jungle')
        self.assertEqual(item, 'scorchclaw_pup')

    def test_get_random_starting_item_support(self):
        item: str = self.championConfigurationGenerator.get_random_starting_item(lane='support')
        self.assertEqual(item, 'world_atlas')

    @patch('numpy.random.choice')
    def test_get_random_starting_item_other_lane(self, mock_random_choice):
        mock_random_choice.return_value = 'berserker\'s_greaves'
        item = self.championConfigurationGenerator.get_random_starting_item('top')
        self.assertIn(item, self.championConfigurationGenerator.BOOTS_NAME)

if __name__ == '__main__':
    unittest.main()
