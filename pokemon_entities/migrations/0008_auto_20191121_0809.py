# Generated by Django 2.2.3 on 2019-11-21 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20191121_0808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='coordinate',
            new_name='pokemon',
        ),
    ]
