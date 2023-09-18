# Generated by Django 4.2.4 on 2023-09-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lor_backend', '0002_champion_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='item_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='item_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='item_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='item_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='item_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='item_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='role',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_main_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_main_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_main_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_main_keystone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_main_tree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_secondary_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_secondary_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_secondary_tree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_shard_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_shard_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='rune_shard_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='spell_to_max',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='summoner_spell_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='champion',
            name='summoner_spell_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='champion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
