# Generated by Django 2.2.3 on 2019-11-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20191121_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(null=True),
        ),
    ]
