# Generated by Django 2.2.3 on 2019-11-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='pokemons'),
        ),
    ]
