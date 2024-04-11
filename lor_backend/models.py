from django.db import models


class Champion(models.Model):
    unique_id = models.IntegerField(primary_key=True, default=0)

    name = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=50, default="")

    spell_to_max = models.CharField(max_length=100, default="")

    summoner_spell_1 = models.CharField(max_length=100, default="")
    summoner_spell_2 = models.CharField(max_length=100, default="")

    rune_main_tree = models.CharField(max_length=100, default="")
    rune_main_keystone = models.CharField(max_length=100, default="")
    rune_main_1 = models.CharField(max_length=100, default="")
    rune_main_2 = models.CharField(max_length=100, default="")
    rune_main_3 = models.CharField(max_length=100, default="")

    rune_secondary_tree = models.CharField(max_length=100, default="")
    rune_secondary_1 = models.CharField(max_length=100, default="")
    rune_secondary_2 = models.CharField(max_length=100, default="")

    rune_shard_1 = models.CharField(max_length=100, default="")
    rune_shard_2 = models.CharField(max_length=100, default="")
    rune_shard_3 = models.CharField(max_length=100, default="")

    item_1 = models.CharField(max_length=100, default="")
    item_2 = models.CharField(max_length=100, default="")
    item_3 = models.CharField(max_length=100, default="")
    item_4 = models.CharField(max_length=100, default="")
    item_5 = models.CharField(max_length=100, default="")
    item_6 = models.CharField(max_length=100, default="")

    starter_item = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
