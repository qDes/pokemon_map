# Generated by Django 2.2.3 on 2019-11-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_pokemon_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='title',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_ru',
            field=models.TextField(blank=True),
        ),
    ]
